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

        path = self._get_path(command)
        path_value = self._get_document_path_value(document, path)
        new_value = command.get("value")

        """Add single key: value"""
        document[path] = new_value


        """Set element to exist array"""
        if path_value and isinstance(path_value, list):
            path_value.append(new_value)
            return document

        return document

    def _get_path(self, command: dict) -> str:
        """
         with remove front slash
        """
        return command.get("path").replace('/', '', 1)

    def _get_document_path_value(self, document: dict, path: str):
        return document.get(path)
