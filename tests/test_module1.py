import pytest


@pytest.mark.test_extensions_import_module1
def test_extensions_import_module1(parse):

    # import sys
    # import importlib

    # from pathlib import Path

    extensions = parse("extensions")
    assert extensions.success, extensions.message

    sys_import = extensions.imports("sys")
    assert sys_import, "Are you importing `sys`?"

    assert False


# sys_import_exists = extensions.select_import("sys")
# importlib_import_exists = extensions.select_import("importlib")
# pathlib_import, pathlib_import_exists = extensions.select("from pathlib import Path")

# assert sys_import_exists, "Are you importing `sys`?"
# assert importlib_import_exists, "Are you importing `importlib`?"
# assert pathlib_import_exists, "Are you importing `Path` from `pathlib`?"


"""
@pytest.mark.test_extensions_sys_path_module1
def test_extensions_sys_path_module1(parse):

    # def load_module(directory, name):
    #     sys.path.insert(0, directory)

    extensions = parse("extensions")
    assert extensions.success, extensions.message

    print(extensions.fd("load_module").e("args.args.arg").n)
    load_module, load_module_exists = extensions.select(
        "def load_module(directory, name): ??", False
    )

    # body = load_module[0]["body"]

    # print(
    #     extensions.match_collection(
    #         {
    #             "value.type": "Call",
    #             "value.func.value.value.id": "sys",
    #             "value.func.value.attr": "path",
    #             "value.func.attr": "insert",
    #             "value.args.0.value": 0,
    #             "value.args.1.id": "directory",
    #         },
    #         body,
    #     )
    # )

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
"""
