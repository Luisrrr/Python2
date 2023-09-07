def convert(einheit1, einheit2, val):
    if einheit1 == "Celsius":
        if einheit2 == "Fahrenheit":
            val = celsius_zu_fahrenheit(val)
        elif einheit2 == "Kelvin":
            val = celsius_zu_kelvin(val)

    if einheit1 == "Fahrenheit":
        if einheit2 == "Celsius":
            val = fahrenheit_zu_celsius(val)
        elif einheit2 == "Kelvin":
            val = fahrenheit_zu_kelvin(val)

    if einheit1 == "Kelvin":
        if einheit2 == "Fahrenheit":
            val = kelvin_zu_fahrenheit(val)
        elif einheit2 == "Celsius":
            val = kelvin_zu_celsius(val)

    return val


def celsius_zu_fahrenheit(val):
    return val * (9 / 5) + 32


def celsius_zu_kelvin(val):
    return val + 273.15


def kelvin_zu_celsius(val):
    return val - 273.15


def kelvin_zu_fahrenheit(val):
    return celsius_zu_fahrenheit(kelvin_zu_celsius(val))


def fahrenheit_zu_celsius(val):
    return 5 / 9 * (val - 32)


def fahrenheit_zu_kelvin(val):
    return celsius_zu_kelvin(fahrenheit_zu_celsius(val))


print("Gültige Einheiten: Celsius, Kelvin, Fahrenheit")
val1 = int(input("Zahl die du umwandeln willst: "))
einheit = input("Die Einheit dieser Zahl ist: ")
gewuenschteEinheit = input("Gewünschte Einheit: ")

print(str(val1) + "°", einheit, "sind", convert(einheit, gewuenschteEinheit, val1), "in", gewuenschteEinheit)
