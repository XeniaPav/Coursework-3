import json
def open_file():
    """
    Открытие и чтение файла
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        operation = []
        file_json = json.load(file)
        for i in file_json:
            operation.append(i)
        return operation

print(open_file())
