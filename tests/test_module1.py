import re

# import past
import pmast
import pytest
import redbaron


@pytest.mark.test_extensions_import_module1
def test_extensions_import_module1(parse):

    # import sys
    # import importlib

    # from pathlib import Path

    assert False


@pytest.mark.test_extensions_sys_path_module1
def test_extensions_sys_path_module1(parse):

    # def load_module(directory, name):
    #     sys.path.insert(0, directory)

    assert False


@pytest.mark.test_extensions_import_pop_module1
def test_extensions_import_pop_module1(parse):

    #     importlib.import_module(name)
    #     sys.path.pop(0)

    assert False


@pytest.mark.test_extensions_load_directory_module1
def test_extensions_load_directory_module1(parse):

    # def load_directory(directory):
    #     for path in directory.rglob("*.py"):
    #         load_module(directory.as_posix(), path.stem)

    assert False


@pytest.mark.test_extensions_load_bundled_module1
def test_extensions_load_bundled_module1(parse):

    # def load_bundled():
    #     directory = Path(__file__).parent / "extensions"
    #     load_directory(directory)

    assert False


@pytest.mark.test_site_load_bundled_module1
def test_site_load_bundled_module1(parse):

    # from ssg import extensions
    # extensions.load_bundled()

    assert False
