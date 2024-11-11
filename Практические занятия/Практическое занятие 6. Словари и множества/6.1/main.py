countries_and_capitals = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Германия": "Берлин",
    "США": "Вашингтон",
    "Италия": "Рим",
}

for country, capital in countries_and_capitals.items():
    print(f"{country}: {capital}")

country = input("Введите название страны: ")
print(f"Столицу страны {country}: {countries_and_capitals.get(country, 'Неизвестно')}")

sorted_countries = sorted(countries_and_capitals.items())
for country, capital in sorted_countries:
    print(f"{country}: {capital}")
