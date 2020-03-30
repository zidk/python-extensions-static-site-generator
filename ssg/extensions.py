import os
import sys
import importlib


def load_module(directory: str, name: str):
    sys.path.insert(0, directory)
    importlib.import_module(name)
    sys.path.pop(0)


def load_directory(directory: str):
    for name in os.listdir(directory):
        if name.startswith("."):
            continue
        base = os.path.splitext(name)[0]
        load_module(directory, base)


def load_bundled_extensions():
    load_directory(os.path.join(os.path.dirname(__file__), "extensions"))
