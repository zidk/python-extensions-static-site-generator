import re
import pytest

import redbaron


@pytest.mark.test_site_path_import_module1
def test_site_path_import_module1(parse):
    pass


@pytest.mark.test_site_class_module1
def test_site_class_module1(parse):
    pass


@pytest.mark.test_site_create_dir_function_module1
def test_site_create_dir_function_module1(parse):
    pass


@pytest.mark.test_site_create_dir_mkdir_module1
def test_site_create_dir_mkdir_module1(parse):
    pass


@pytest.mark.test_site_build_function_module1
def test_site_build_function_module1(parse):
    pass


@pytest.mark.test_site_path_rglob_module1
def test_site_path_rglob_module1(parse):
    pass


@pytest.mark.test_ssg_imports_module1
def test_ssg_imports_module1(parse):
    pass


@pytest.mark.test_ssg_main_command_module1
def test_ssg_main_command_module1(parse):
    pass


@pytest.mark.test_ssg_build_call_module1
def test_ssg_build_call_module1(parse):
    pass


@pytest.mark.test_ssg_typer_run_module1
def test_ssg_typer_run_module1(parse):
    pass
