# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(INPUT_FILENAME, razdel=',', line_terminator='\n') -> None:

    list = []

    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csvfile:  # TODO считать содержимое csv файла
        reader = csv.DictReader(csvfile, delimiter=razdel)

        for row in reader:
            list.append(row)

    json_output = json.dumps(list, indent=4, ensure_ascii=False)

    return json_output

print(task(INPUT_FILENAME))
# if __name__ == '__main__':
#     # Нужно для проверки
#     task(INPUT_FILENAME)
#
#     with open(OUTPUT_FILENAME) as output_f:
#         for line in output_f:
#             print(line, end="")
