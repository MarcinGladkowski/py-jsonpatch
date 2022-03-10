from patch_lib import JsonPath, Add
import pytest


@pytest.mark.parametrize("document, command, result", [
    ({}, {"path": "foo", "value": "bar"}, {"foo": "bar"}),
    ({"test": "test"}, {"path": "foo", "value": "bar"}, {"test": "test", "foo": "bar"}),
    ({"foo": ["baz"]}, {"path": "foo", "value": "bar"}, {"foo": ["baz", "bar"]}),
    ({}, {"path": "foo/bar", "value": "baz"}, {"foo": {"bar": "baz"}})
])
def test_is_palindrome(document, command, result):
    assert (Add()).execute(document, command) == result


def test_not_modified_document():
    json_path = JsonPath()
    document = json_path.patch_document({"test": "test"}, [])
    assert document == {"test": "test"}



