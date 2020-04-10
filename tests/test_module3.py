import pytest


@pytest.mark.test_menu_imports_module3
def test_menu_imports_module3(parse):

    # from ssg import hooks, parsers

    # files = []

    assert False


@pytest.mark.test_menu_collect_files_module3
def test_menu_collect_files_module3(parse):

    # @hooks.register("collect_files")
    # def collect_files(source, site_parsers):
    #     valid = lambda p: not isinstance(p, parsers.ResourceParser)

    assert False


@pytest.mark.test_menu_for_build_list_module3
def test_menu_for_build_list_module3(parse):

    #     for path in source.rglob("*"):
    #         for parser in list(filter(valid, site_parsers)):
    #             if parser.valid_file_ext(path.suffix):
    #                 files.append(path)

    assert False


@pytest.mark.test_menu_generate_menu_module3
def test_menu_generate_menu_module3(parse):

    # @hooks.register("generate_menu")
    # def generate_menu(html, ext):
    #     template = '<li><a href="{}{}">{}</a></li>'

    assert False


@pytest.mark.test_menu_lambda_module3
def test_menu_lambda_module3(parse):

    #     menu_item = lambda name, ext: template.format(name, ext, name.title())

    assert False


@pytest.mark.test_menu_names_module3
def test_menu_names_module3(parse):

    #     menu = "\n".join([menu_item(path.stem, ext) for path in files])

    assert False


@pytest.mark.test_menu_list_template_module3
def test_menu_list_template_module3(parse):

    #     return "<ul>\n{}<ul>\n{}".format(menu, html)

    assert False


@pytest.mark.test_site_collect_files_event_module3
def test_site_collect_files_event_module3(parse):

    #        hooks.event("collect_files", self.source, self.parsers)

    assert False


@pytest.mark.test_parsers_md_menu_filter_module3
def test_parsers_md_menu_filter_module3(parse):

    #        filtered = hooks.filter("generate_menu", html, self.base_ext)
    #        self.write(path, dest, filtered)

    assert False


@pytest.mark.test_parsers_rst_menu_filter_module3
def test_parsers_rst_menu_filter_module3(parse):

    #        filtered = hooks.filter("generate_menu", html["html_body"], self.base_ext)
    #        self.write(path, dest, filtered)

    assert False
