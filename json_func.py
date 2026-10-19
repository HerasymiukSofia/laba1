import json


def to_json(data=None):
    """Перетворює словник у JSON-рядок."""
    data = data or {"lab": 4, "status": "done"}
    return json.dumps(data, ensure_ascii=False, indent=2)