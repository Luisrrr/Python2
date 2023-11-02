import math


def format(num, always_show_decimals = True, notation = "MixedScientific"):
    if notation == "MixedScientific":
        if num < 1e33:
            return add_suffix(num, always_show_decimals)
        else:
            return format_scientific(num, always_show_decimals)
    elif notation == "Scientific":
        return format_scientific(num, always_show_decimals)
    elif notation == "Time":
        return format_time(num)


def format_time(num):
    seconds = math.floor(num)
    years = math.floor(seconds / (365.25 * 24 * 3600))
    seconds -= years * 365.25 * 24 * 3600

    days = math.floor(seconds / (24 * 3600))
    seconds -= days * 24 * 3600

    hours = math.floor(seconds / 3600)
    seconds -= hours * 3600

    minutes = math.floor(seconds / 60)
    seconds -= minutes * 60

    formatted_time = ""
    if years > 0:
        formatted_time += str(years) + "y "
    if days > 0:
        formatted_time += str(days) + "d "
    if hours > 0:
        formatted_time += str(hours) + "h "
    if minutes > 0:
        formatted_time += str(minutes) + "m "

    formatted_time += str(int(seconds)) + "s"

    return formatted_time


def format_scientific(num, always_show_decimals = True):
    if always_show_decimals:
        return "{:.2E}".format(num).replace("E+", "e")
    else:
        return "{:.2E}".format(num).replace("E+", "e").replace(".00", "")


def add_suffix(num, always_show_decimals = True):
    if num == 0:
        return "0.00" if always_show_decimals else "0"
    if math.log10(num) <= 0:
        return str(num)

    exponent = math.log10(num)
    suffix_index = math.floor(exponent / 3)

    mantissa = '{0:.2f}'.format(num / (1000 ** suffix_index))
    mantissa = mantissa[0:mantissa.index(".") + 3]
    if not always_show_decimals and mantissa.__contains__(".00"):
        mantissa = mantissa.split('.')[0]

    suffix = suffixes[suffix_index]
    formatted = mantissa
    if suffix != "":
        formatted = mantissa + " " + suffix

    return formatted


suffixes = ["", "K", "M", "B", "T", "Qa", "Qt", "Sx", "Sp", "Oc", "No"]

print(format(1000))
print(format(10000000, False))
print(format(100000000))
print(format(1000000000))
print(format(2.3314e35))
print(format(2e203, False))
print(format(2e203, True))
print(format(2.12e203, False))
print(format(2.12e203, True))
print(format_time(603000012.345))
