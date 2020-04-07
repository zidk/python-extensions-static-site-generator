import ast
import pmast
import pytest

from pmast import ast_type, Pattern, PatternDispatch
from box import Box
from astpretty import pprint
from .past.template import Template


pm = PatternDispatch()
container = Box({"functions": {}, "classes": {}})

with open("ssg/content.py", "r") as file:
    source = file.read()

tree = ast.parse(source)


@pm("ClassDef")
def on_class(data, cd):
    data.classes[cd.name] = cd


@pm("FunctionDef")
def on_function(data, fd):
    pprint(fd)
    # data.functions[fd.name] = {}
    # data.functions[fd.name].args = [arg.arg for arg in fd.args.args]
    # data.functions[fd.name].body = fd.body


data = pm.dispatch(tree, container)



@pytest.mark.test_extensions_sys_path_module1
def test_extensions_sys_path_module1(parse):
    code = """
matches1 = ["test1", "test2", "test3"]
test1 = [match for match in matches1]
matches2 = ["test1", "test2", "test3"]
test2 = [match for match in matches2]
matches3 = ["test1", "test2", "test3"]
test3 = [match for match in matches3]
"""

    matches = Template("[? for ? in ?]").query(code)
    for match in matches:
        pprint(match)

    assert False
