import ast
import pmast
import pytest
import json

# from pmast import ast_type, Pattern, PatternDispatch
# from box import Box
from astpretty import pprint
from .past.template import Template
from pathlib import Path


# pm = PatternDispatch()
# container = Box({"functions": {}, "classes": {}})
# with open(Path.cwd() / "ssg" / "content.py", "r") as file:
#     source = file.read()
# tree = ast.parse(source)
#
#
# @pm("ClassDef")
# def on_class(data, cd):
#     data.classes[cd.name] = cd


# @pm("FunctionDef")
# def on_function(data, fd):
#     pprint(fd)
    # data.functions[fd.name] = {}
    # data.functions[fd.name].args = [arg.arg for arg in fd.args.args]
    # data.functions[fd.name].body = fd.body


# @pytest.mark.test_pmast_example
# def test_pmast_example(parse):
#     data = pm.dispatch(tree, container)
#     assert False



@pytest.mark.test_past_example
def test_past_example(parse):
    with open(Path.cwd() / "ssg" / "content.py", "r") as file:
        source = file.read()

    matches = Template("def load(cls, string): ??").query(source)
    for match in matches:
        print(match)

    assert False
