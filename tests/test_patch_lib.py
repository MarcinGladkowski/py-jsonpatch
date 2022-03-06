from patch_lib import JsonPath, Add


def test_not_modified_document():
    json_path = JsonPath()
    document = json_path.patch_document({"test": "test"}, [])
    assert document == {"test": "test"}


def test_add_operation_to_empty_document():
    add = Add()
    assert add.execute({}, {"path": "foo", "value": "bar"}) == {"foo": "bar"}


def test_add_operation_to_not_empty_document():
    add = Add()
    assert add.execute({"test": "test"}, {"path": "foo", "value": "bar"}) == {"test": "test", "foo": "bar"}


def test_add_operation_to_array_value():
    add = Add()
    assert add.execute({"foo": ["baz"]}, {"path": "foo", "value": "bar"}) == {"foo": ["baz", "bar"]}


def test_add_operation_nested_path():
    add = Add()
    result = add.execute({}, {"path": "foo/bar", "value": "baz"})
    assert result == {"foo": {"bar": "baz"}}
