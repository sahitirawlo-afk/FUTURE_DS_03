#5.1 1. Check whether a JSON string contains a complex object
import json

def is_complex_json(json_string):
    try:
        data = json.loads(json_string)
        return isinstance(data, (dict, list))
    except json.JSONDecodeError:
        return False

# Example usage
json_str1 = '{"name": "Naidu", "age": 30}'
json_str2 = '"Hello World"'

print("JSON 1 is complex:", is_complex_json(json_str1))
print("JSON 2 is complex:", is_complex_json(json_str2))

