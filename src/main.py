from utils import masking_namb, date_conversion, sorted_file, search_success, open_file

file = open_file()
succees_file = search_success(file)
sorted_list = sorted_file(succees_file)
for i in sorted_list:  # Вывод операций
    data = date_conversion(i["date"])
    if "from" in i and "to" in i:
        namb_card = masking_namb(i["from"])
        namb_check = masking_namb(i["to"])
        print(f"{data} {i['description']}\n{namb_card} -> {namb_check}\n{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]['name']}\n")
    elif "to" in i:
        namb_check = masking_namb(i["to"])
        print(f"{data} {i['description']}\n-> {namb_check}\n{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]['name']}\n")
    else:
        print(f"{data} {i['description']}\n{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]['name']}\n")
