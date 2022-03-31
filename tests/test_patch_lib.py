import pytest

from patch_lib import JsonPath, Add, PathError


class TestAdd:

    add = Add()

    def test_not_modified_document(self):
        json_path = JsonPath()
        document = json_path.patch_document({"test": "test"}, [])
        assert document == {"test": "test"}

    def test_add_operation_to_empty_document(self):
        assert self.add.execute({}, {"path": "foo", "value": "bar"}) == {"foo": "bar"}

    def test_add_operation_to_not_empty_document(self):
        assert self.add.execute({"test": "test"}, {"path": "foo", "value": "bar"}) == {"test": "test", "foo": "bar"}

    def test_add_operation_to_array_value(self):
        assert self.add.execute({"foo": ["baz"]}, {"path": "foo", "value": "bar"}) == {"foo": ["baz", "bar"]}

    def test_add_operation_nested_path(self):
        """incorrect operation, shouldn't create elements recursively"""
        with pytest.raises(PathError):
            self.add.execute({}, {"path": "foo/bar", "value": "baz"})

