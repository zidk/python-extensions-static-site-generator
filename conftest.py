import ast
import json

import parso
import pytest

from types import GeneratorType as generator
from itertools import chain
from pathlib import Path

from tests.nodes import convert_node

from objectpath import Tree


class Parser:
    def __init__(self, file_name=None, nodes={}):

        ssg = Path.cwd() / "ssg"
        ext = ssg / "extensions"

        self.data = {
            "success": True,
            "full_path": "",
            "message": "",
            "start_pos": 0,
            "nodes": nodes,
        }

        if file_name is not None:
            path = lambda root, fn: root / "{}.py".format(fn)
            if file_name == "menu" or file_name == "stats":
                full_path = path(ext, file_name)
            elif file_name == "ssg":
                full_path = path(Path.cwd(), file_name)
            else:
                full_path = path(ssg, file_name)

            grammar = parso.load_grammar()
            module = grammar.parse(path=full_path)
            self.data["success"] = len(grammar.iter_errors(module)) == 0

        if self.data["success"]:
            self.data["message"] = "Syntax: valid"
            if file_name is not None:
                self.data["nodes"] = convert_node(ast.parse(full_path.read_text()))

        else:
            self.data["message"] = grammar.iter_errors(module)[0].message
            self.data["start_pos"] = grammar.iter_errors(module)[0].start_pos[0]

    @property
    def nodes(self):
        return self.data["nodes"]

    @property
    def n(self):
        return self.data["nodes"]

    @property
    def success(self):
        return self.data["success"]

    @property
    def message(self):
        return "{} on or around line {} in `{}`.".format(
            self.data["message"], self.data["start_pos"], self.data["full_path"]
        )

    def e(self, expr):
        return self.execute(expr)

    def execute(self, expr):
        result = Tree(self.nodes).execute("$." + expr)
        if isinstance(result, (generator, chain, map)):
            process = list(result)
            return (
                Parser(file_name=None, nodes=process[0])
                if len(process) == 1
                else Parser(file_name=None, nodes=process)
            )
        else:
            return Parser(file_name=None, nodes=result)

    def defines(self, name):
        return self.execute(
            "body[@.type is 'FunctionDef' and @.name is '{}'].(name, args)".format(name)
        )

    def imports(self, name):
        return name in self.execute("body[@.type is 'Import'].names..name").n


@pytest.fixture
def parse():
    def _parse(file_name):
        return Parser(file_name=file_name)

    return _parse
