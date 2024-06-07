replacements = {
    "+": "1",
    "ě": "2",
    "š": "3",
    "č": "4",
    "ř": "5",
    "ž": "6",
    "ý": "7",
    "á": "8",
    "í": "9",
    "é": "0",
    "Ě": "2",
    "Š": "3",
    "Č": "4",
    "Ř": "5",
    "Ž": "6",
    "Ý": "7",
    "Á": "8",
    "Í": "9",
    "É": "0"
}

while True:
    input_str = input("Zadejte ID čipu: ")
    print("ID čipu je:", input_str)

    for old, new in replacements.items():
        input_str = input_str.replace(old, new)

    print("ID čipu po úpravě: ", input_str)