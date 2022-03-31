from patch_lib import JsonPath, Add


class TestAdd:

    def test_not_modified_document(self):
        json_path = JsonPath()
        document = json_path.patch_document({"test": "test"}, [])
        assert document == {"test": "test"}

    def test_add_operation_to_empty_document(self):
        add = Add()
        assert add.execute({}, {"path": "foo", "value": "bar"}) == {"foo": "bar"}

    def test_add_operation_to_not_empty_document(self):
        add = Add()
        assert add.execute({"test": "test"}, {"path": "foo", "value": "bar"}) == {"test": "test", "foo": "bar"}

    def test_add_operation_to_array_value(self):
        add = Add()
        assert add.execute({"foo": ["baz"]}, {"path": "foo", "value": "bar"}) == {"foo": ["baz", "bar"]}

    def test_add_operation_nested_path(self):
        add = Add()
        result = add.execute({}, {"path": "foo/bar", "value": "baz"})
        assert result == {"foo": {"bar": "baz"}}
