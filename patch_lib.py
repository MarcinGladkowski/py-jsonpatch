from typing import List
import re


class PathError(Exception):
    pass


class JsonPath:

    def __init__(self) -> None:
        super().__init__()

    def patch_document(self, document: dict, commands: List[dict]):
        return document
        if "something_is_wrong":
            raise PathError('something is wrong, dude')


class Test:
    """
    Tests that the specified value is set in the document.
    If the test fails, then the patch as a whole should not apply.
    """
    def execute(self, document: dict, command: dict):
        raise RuntimeError


class Add:
    def execute(self, document: dict, command: dict):

        paths = self._get_path(command)

        if len(paths) > 1:
            for i, path in enumerate(paths):
                element = document.get(path)
                if element is None:
                    raise PathError

        path_value = self._get_document_path_value(document, paths[0])
        new_value = command.get("value")

        """Set element to exist array"""
        if path_value and isinstance(path_value, list):
            path_value.append(new_value)
            return document

        """Add single key: value"""
        document[paths[0]] = new_value


        """Set element to exist array"""
        if path_value and isinstance(path_value, list):
            path_value.append(new_value)
            return document

        return document

    def _get_path(self, command: dict) -> list:
        """with remove front slash"""

        command_path = command.get('path')

        if command_path.startswith('/'):
            command_path = command.get("path").replace('/', '', 1)

        return command_path.split('/')

    def _get_document_path_value(self, document: dict, path: str):
        return document.get(path)
