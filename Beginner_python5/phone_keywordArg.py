def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=47, area=123, first=9028, last=6040)

print(phone_num)
