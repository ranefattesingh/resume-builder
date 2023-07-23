import json
import os


def decode_json(file_path: str, file_name: str) -> dict:
        data: any
        with open(os.path.join(file_path, file_name)) as file:
            data = json.load(file)

        return data