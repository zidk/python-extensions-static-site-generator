import pytest
import json


@pytest.mark.test_stats_imports_module4
def test_stats_imports_module4(parse):

    # import time

    # from ssg import hooks, parsers

    # start_time = None
    # total_written = 0

    stats = parse("stats")
    assert stats.success, stats.message

    time_import = stats.imports("time")
    assert time_import, "Are you importing `time`?"

    hooks_import = stats.from_imports("ssg", "hooks")
    assert hooks_import, "Are you importing `hooks` from `ssg`?"

    start_time = (
        stats.assigns()
        .match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "start_time",
                "value_type": "Constant",
                "value_value": "nil",
            }
        )
        .exists()
    )
    assert start_time, "Are you creating a variable called `start_time` set to `None`?"

    total_written = (
        stats.assigns()
        .match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "total_written",
                "value_type": "Constant",
                "value_value": 0,
            }
        )
        .exists()
    )
    assert (
        total_written
    ), "Are you creating a variable called `total_written` set equal to `0`?"


@pytest.mark.test_stats_register_start_build_module4
def test_stats_register_start_build_module4(parse):

    # @hooks.register("start_build")
    # def start_build():
    #     global start_time
    #     start_time = time.time()

    stats = parse("stats")
    assert stats.success, stats.message

    start_build = stats.defines("start_build")
    start_build_exists = start_build.exists()
    assert start_build_exists, "Are you defining a function called `start_build`?"

    decorator = (
        start_build.decorators()
        .match(
            {
                "0_type": "Call",
                "0_func_type": "Attribute",
                "0_func_value_type": "Name",
                "0_func_value_id": "hooks",
                "0_func_attr": "register",
                "0_args_0_type": "Constant",
                "0_args_0_value": "start_build",
            }
        )
        .exists()
    )
    assert (
        decorator
    ), 'Has the `start_build` function been decorated with `@hooks.register()` passing in `"start_build"`?'

    start_time_global = start_build.globals("start_time")
    assert (
        start_time_global
    ), "Are you using the `global` keyword to bring `start_time` in to scope in the `start_build` function?"

    start_time = (
        start_build.assign_()
        .match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "start_time",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Name",
                "value_func_value_id": "time",
                "value_func_attr": "time",
            }
        )
        .exists()
    )
    assert (
        start_time
    ), "Are you creating a variable called `start_time` and setting it equal to `time.time()`?"


@pytest.mark.test_stats_register_written_module4
def test_stats_register_written_module4(parse):

    # @hooks.register("written")
    # def written():
    #     global total_written
    #     total_written = total_written + 1

    stats = parse("stats")
    assert stats.success, stats.message

    written = stats.defines("written")
    written_exists = written.exists()
    assert written_exists, "Are you defining a function called `written`?"

    decorator = (
        written.decorators()
        .match(
            {
                "0_type": "Call",
                "0_func_type": "Attribute",
                "0_func_value_type": "Name",
                "0_func_value_id": "hooks",
                "0_func_attr": "register",
                "0_args_0_type": "Constant",
                "0_args_0_value": "written",
            }
        )
        .exists()
    )
    assert (
        decorator
    ), 'Has the `written` function been decorated with `@hooks.register()` passing in `"written"`?'

    total_written_global = written.globals("total_written")
    assert (
        total_written_global
    ), "Are you using the `global` keyword to bring `total_written` in to scope in the `written` function?"

    print(json.dumps(written.assign_().n, indent=2))
    total_written = (
        written.assign_()
        .match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "total_written",
                "value_type": "BinOp",
                "value_left_type": "Name",
                "value_left_id": "total_written",
                "value_op": "#<Add>",
                "value_right_type": "Constant",
                "value_right_value": 1,
            }
        )
        .exists()
    )
    assert (
        total_written
    ), "Are you creating a variable called `total_written` and assigning it `total_written` plus `1`?"


@pytest.mark.test_stats_register_stats_module4
def test_stats_register_stats_module4(parse):

    # @hooks.register("stats")
    # def stats():
    #     final_time = time.time() - start_time

    stats = parse("stats")
    assert stats.success, stats.message

    stats_def = stats.defines("stats")
    stats_def_exists = stats_def.exists()
    assert stats_def_exists, "Are you defining a function called `stats`?"

    decorator = (
        stats_def.decorators()
        .match(
            {
                "0_type": "Call",
                "0_func_type": "Attribute",
                "0_func_value_type": "Name",
                "0_func_value_id": "hooks",
                "0_func_attr": "register",
                "0_args_0_type": "Constant",
                "0_args_0_value": "stats",
            }
        )
        .exists()
    )
    assert (
        decorator
    ), 'Has the `stats` function been decorated with `@hooks.register()` passing in `"stats"`?'

    final_time = (
        stats_def.assigns()
        .match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "final_time",
                "value_type": "BinOp",
                "value_left_type": "Call",
                "value_left_func_type": "Attribute",
                "value_left_func_value_type": "Name",
                "value_left_func_value_id": "time",
                "value_left_func_attr": "time",
                "value_op_type": "Sub",
                "value_right_type": "Name",
                "value_right_id": "start_time",
            }
        )
        .exists()
    )
    assert (
        final_time
    ), "Are you creating a variable called `final_time` and assigning it `time.time()` minus `start_time`?"


@pytest.mark.test_stats_average_time_module4
def test_stats_average_time_module4(parse):

    #     average = final_time / total_written if total_written else 0

    stats = parse("stats")
    assert stats.success, stats.message

    stats_def = stats.defines("stats")
    stats_def_exists = stats_def.exists()
    assert stats_def_exists, "Are you defining a function called `stats`?"

    average = (
        stats_def.assigns()
        .match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "average",
                "value_type": "IfExp",
                "value_test_type": "Name",
                "value_test_id": "total_written",
                "value_body_type": "BinOp",
                "value_body_left_type": "Name",
                "value_body_left_id": "final_time",
                "value_body_op_type": "Div",
                "value_body_right_type": "Name",
                "value_body_right_id": "total_written",
                "value_orelse_type": "Constant",
                "value_orelse_value": 0,
            }
        )
        .exists()
    )
    assert (
        average
    ), "Are you creating a variable called `average` set equal to `final_time` divided by `total_written if total_written else 0`?"


@pytest.mark.test_stats_report_module4
def test_stats_report_module4(parse):

    #     report = "Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"

    stats = parse("stats")
    assert stats.success, stats.message

    stats_def = stats.defines("stats")
    stats_def_exists = stats_def.exists()
    assert stats_def_exists, "Are you defining a function called `stats`?"

    report = (
        stats_def.assigns()
        .match(
            {
                "type": "Assign",
                "targets_0_type": "Name",
                "targets_0_id": "report",
                "value_type": "Constant",
                "value_value": "Converted: {} \u00b7 Time: {:.2f} sec \u00b7 Avg: {:.4f} sec/file",
            }
        )
        .exists()
    )
    assert (
        report
    ), 'Are you creating a variable called `report` set equal to `"Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"`?'


@pytest.mark.test_stats_print_report_module4
def test_stats_print_report_module4(parse):

    #     print(report.format(total_written, final_time, average))

    stats = parse("stats")
    assert stats.success, stats.message

    stats_def = stats.defines("stats")
    stats_def_exists = stats_def.exists()
    assert stats_def_exists, "Are you defining a function called `stats`?"

    print_report = (
        stats_def.calls()
        .match(
            {
                "type": "Expr",
                "value_type": "Call",
                "value_func_type": "Name",
                "value_func_id": "print",
                "value_args_0_type": "Call",
                "value_args_0_func_type": "Attribute",
                "value_args_0_func_value_type": "Name",
                "value_args_0_func_value_id": "report",
                "value_args_0_func_attr": "format",
                "value_args_0_args_0_type": "Name",
                "value_args_0_args_0_id": "total_written",
                "value_args_0_args_1_type": "Name",
                "value_args_0_args_1_id": "final_time",
                "value_args_0_args_2_type": "Name",
                "value_args_0_args_2_id": "average",
            }
        )
        .exists()
    )
    assert (
        print_report
    ), "Are you calling `print()` and passing in `report.format()`? Are you passing 3 values to `format()` `total_written`, `final_time`, and `average`?"


@pytest.mark.test_site_stats_events_module4
def test_site_stats_events_module4(parse):

    #     hooks.event("start_build")
    #     hooks.event("stats")

    site = parse("site")
    assert site.success, site.message

    build = site.method("build")

    hooks_event_start_build = (
        build.calls()
        .match(
            {
                "type": "Expr",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Name",
                "value_func_value_id": "hooks",
                "value_func_attr": "event",
                "value_args_0_type": "Constant",
                "value_args_0_value": "start_build",
            }
        )
        .exists()
    )

    assert (
        hooks_event_start_build
    ), 'Are you calling `hooks.event()` in the `build` method, are you passing in `"start_build"`?'

    hooks_event_stats = (
        build.calls()
        .match(
            {
                "type": "Expr",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Name",
                "value_func_value_id": "hooks",
                "value_func_attr": "event",
                "value_args_0_type": "Constant",
                "value_args_0_value": "stats",
            }
        )
        .exists()
    )

    assert (
        hooks_event_stats
    ), 'Are you calling `hooks.event()` in the `build` method, are you passing in `"stats"`?'


@pytest.mark.test_parsers_written_events_module4
def test_parsers_written_events_module4(parse):

    #     hooks.event("written")
    #     hooks.event("written")

    parsers = parse("parsers")
    assert parsers.success, parsers.message

    markdown_parse = parsers.class_("MarkdownParser").defines("parse")
    rst_parse = parsers.class_("ReStructuredTextParser").defines("parse")

    hooks_event_written_md = (
        markdown_parse.calls()
        .match(
            {
                "type": "Expr",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Name",
                "value_func_value_id": "hooks",
                "value_func_attr": "event",
                "value_args_0_type": "Constant",
                "value_args_0_value": "written",
            }
        )
        .exists()
    )

    assert (
        hooks_event_written_md
    ), 'Are you calling `hooks.event()` in the `parse` method, are you passing in `"written"`?'

    hooks_event_written_rst = (
        rst_parse.calls()
        .match(
            {
                "type": "Expr",
                "value_type": "Call",
                "value_func_type": "Attribute",
                "value_func_value_type": "Name",
                "value_func_value_id": "hooks",
                "value_func_attr": "event",
                "value_args_0_type": "Constant",
                "value_args_0_value": "written",
            }
        )
        .exists()
    )

    assert (
        hooks_event_written_rst
    ), 'Are you calling `hooks.event()` in the `parse` method, are you passing in `"written"`?'
