from patch_lib import JsonPath, Add, Test
import pytest


def test_test_command_raise_exception():
    with pytest.raises(RuntimeError):
        (Test()).execute({}, {})


@pytest.mark.parametrize("document, command, result", [
    ({}, {"path": "/foo", "value": "bar"}, {"foo": "bar"}),
    ({"test": "test"}, {"path": "/foo", "value": "bar"}, {"test": "test", "foo": "bar"}),
    ({"foo": ["baz"]}, {"path": "/foo", "value": "bar"}, {"foo": ["baz", "bar"]}),
    ({}, {"path": "/foo/bar", "value": "baz"}, {"foo": {"bar": "baz"}}),
    ({"test": "test"}, {"path": "/test/bar", "value": "baz"}, {"test": {"bar": "baz"}}),
    # ({}, {"path": "/foo/bar/baz", "value": "baz"}, {"foo": {"bar": {"baz": "baz"}}}),
])
def test_add_command(document, command, result):
    assert (Add()).execute(document, command) == result


def test_not_modified_document():
    json_path = JsonPath()
    document = json_path.patch_document({"test": "test"}, [])
    assert document == {"test": "test"}
