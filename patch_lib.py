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


class Add:
    def execute(self, document: dict, command: dict):

        path = self._get_path(command)
        path_value = self._get_document_path_value(document, path)
        new_value = command.get("value")

        pattern = re.compile("/")
        if pattern.search(path):
            path_keys = re.split(pattern, path)

            for index, key in enumerate(path_keys):
                value = None
                if len(path_keys) >= index + 1:
                    value = new_value

                document[key] = {path_keys[index + 1]: value}

                if len(path_keys) >= index + 1:
                    return document

            return document

        if path_value and isinstance(path_value, list):
            path_value.append(new_value)
            return document

        document[path] = new_value

        return document

    def _get_path(self, command: dict):
        return command.get("path")

    def _get_document_path_value(self, document: dict, path: str):
        return document.get(path)
