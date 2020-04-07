import re
import pytest

import redbaron


@pytest.mark.test_hooks_base_class_module2
def test_hooks_base_class_module2(parse):

    # _callbacks = {}

    assert False


@pytest.mark.test_hooks_valid_extension_function_module2
def test_hooks_valid_extension_function_module2(parse):

    # def register(hook, order=0):
    #     def register_callback(func):

    #         return func

    #     return register_callback

    assert False


@pytest.mark.test_hooks_parse_function_module2
def test_hooks_parse_function_module2(parse):
    #         _callbacks.setdefault(hook, {}).setdefault(order, []).append(func)
    assert False


@pytest.mark.test_hooks_read_function_module2
def test_hooks_read_function_module2(parse):

    # def event(hook, *args):
    #     for order in sorted(_callbacks.get(hook, {})):
    #         for func in _callbacks[hook][order]:
    #             func(*args)

    assert False


@pytest.mark.test_hooks_write_function_module2
def test_hooks_write_function_module2(parse):

    # def filter(hook, value, *args):
    #     for order in sorted(_callbacks.get(hook, {})):
    #         for func in _callbacks[hook][order]:
    #             value = func(value, *args)
    #     return value

    assert False
