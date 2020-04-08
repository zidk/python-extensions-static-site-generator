import pytest


from .past.template import Template
from pathlib import Path


@pytest.mark.test_past_example
def test_past_example(parse):
    with open(Path.cwd() / "ssg" / "content.py", "r") as file:
        source = file.read()

    matches = Template("def load(cls, string): ??").query(source)
    for match in matches:
        print(match)

    assert False
