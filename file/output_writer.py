import json
from typing import List


class OutputWriter:
    def __init__(self, out_path):
        self._output = out_path
        self._writer = self._get_writer()

    def write_file(self, result: List[List[int]]):
        self._writer.write_file(result)

    def _get_writer(self):
        if self._output.endswith(".json"):
            return JsonWriter(self._output)


class JsonWriter:
    def __init__(self, output_path):
        self._output = output_path

    def write_file(self, result):
        with open(self._output, "w") as f:
            f.write(json.dumps(result))
