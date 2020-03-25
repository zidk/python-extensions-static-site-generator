import sys
from pathlib import Path
from importlib import import_module


class Site:
    def __init__(self, source, dest, parsers=None, extensions=None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []
        self.extensions = extensions or []

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def load_parser(self, ext):
        for parser in self.parsers:
            if parser.valid_file_ext(ext):
                return parser

    def load_extensions(self):
        module_base = "ssg"
        module_sub = "extensions"
        module_path = Path.cwd() / module_base / module_sub

        for path in module_path.rglob("*.py"):
            if path.stem in self.extensions:
                module_name = "{}.{}.{}".format(module_base, module_sub, path.stem)
                import_module(module_name)

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            self.error(
                "No parser for the {} extension, file skipped!".format(
                    path.suffix
                )
            )

    def build(self):
        self.load_extensions()
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                self.run_parser(path)

    @staticmethod
    def error(message):
        sys.stderr.write("\x1b[1;31m{}\n".format(message))
