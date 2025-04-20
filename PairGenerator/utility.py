import json


def read_json(path):
    with open(path, "r", errors="ignore", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    with open(path, "w", errors="ignore", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
