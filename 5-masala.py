data = ["salom", "dastur", 2.5, "yordam", 34, "kitob"]

translations = {
    "salom": "hello",
    "dastur": "program",
    "yordam": "help",
    "kitob": "book"
}

translated_dict = {item: translations[item] for item in data if isinstance(item, str)}

print(translated_dict)
