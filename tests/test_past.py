import ast
import pmast
from pmast import ast_type, Pattern, PatternDispatch
from box import Box
from astpretty import pprint

pm = PatternDispatch()
container = Box({
    "functions": {},
    "classes": {}
})

with open("content.py", "r") as file:
    source = file.read()

tree = ast.parse(source)

@pm('ClassDef')
def on_class(data, cd):
    data.classes[cd.name] = cd


@pm('FunctionDef')
def on_function(data, fd):
    pprint(fd)
    # data.functions[fd.name] = {}
    # data.functions[fd.name].args = [arg.arg for arg in fd.args.args]
    # data.functions[fd.name].body = fd.body

data = pm.dispatch(tree, container)