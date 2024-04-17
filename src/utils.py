import json
import datetime

def open_file():
    """
    Открытие и чтение файла
    """
    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)
def search_success(data):
    """
    Выбор успешных операций
    """
    data = [elem for elem in data if elem and elem["state"] == "EXECUTED"]
    return data

def sorted_file(data):
    """
    Сортировка по дате и выбор 5 первых операций
    """
    s_data = sorted(data, key=lambda x:x["date"], reverse=True)
    return s_data[:5]

def date_conversion(date:str):
    """
    Преобразование даты
    """
    date = date[:10]
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    new_date = date.strftime("%d.%m.%Y")
    return new_date

def masking_namb(number:str, to=True):
    """
    Маскировка карты/счёта
    """
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    voice = []
    num = []
    for i in number:
        if i in numbers:
            num.append(i)
        else:
            voice.append(i)
    if len(num) > 16:
        return f"{"".join(voice)} ** {"".join(num[-4:])}"
    else:
        return f"{"".join(voice)} {"".join(num[:4])} {"".join(num[4:6])}** **** {"".join(num[-4:])}"
