# TODO решите задачу
import json

File = "input.json"

def task() -> float:
    with open(File) as f:
        json_data = json.load(f)

    result = [item["score"] * item["weight"] for item in json_data]
    return(f"{sum(result):.3f}")


print(task())
