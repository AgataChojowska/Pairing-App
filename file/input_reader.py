import json
from typing import List


class InputReader:
    def __init__(self, path):
        self._path: str = path
        self._reader = self._get_reader()

    def _get_reader(self):
        if self._path.endswith(".json"):
            return JsonReader(self._path)

    def read_input(self):
        return self._reader.read()


class JsonReader:
    def __init__(self, path):
        self._path = path

    def read(self) -> List[int]:
        with open(self._path) as json_file:
            return json.load(json_file)
