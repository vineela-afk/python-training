def convert_date(date):
    year, month, day = date.split('-')
    new_date = f"{day}-{month}-{year}"
    return new_date


date = "2023-07-07"
converted_date = convert_date(date)
print("Original date:", date)
print("Converted date:", converted_date)