import math

def format(num, alwaysShowDecimals = True, notation = "MixedScientific"):
    if notation == "MixedScientific":
        if num < 1e33:
            return add_suffix(num, alwaysShowDecimals)
        else:
            return format_scientific(num, alwaysShowDecimals)
    elif notation == "Scientific":
        return format_scientific(num, alwaysShowDecimals)


def format_scientific(num, alwaysShowDecimals = True):
    if alwaysShowDecimals:
        return "{:.2E}".format(num).replace("E+", "e")
    else:
        return "{:.2E}".format(num).replace("E+", "e").replace(".00", "")


def add_suffix(num, alwaysShowDecimals = True):
    if num == 0:
        return alwaysShowDecimals if "0.00" else "0"
    if math.log10(num) <= 0:
        return str(num)

    exponent = math.log10(num)
    suffixIndex = math.floor(exponent / 3)

    mantissa = '{0:.2f}'.format(num / (1000 ** suffixIndex))
    mantissa = mantissa[0:mantissa.index(".") + 3]
    if not alwaysShowDecimals and mantissa.__contains__(".00"):
        mantissa = mantissa.split('.')[0]

    suffix = suffixes[suffixIndex]
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

# static string AddSuffix(BigDouble num, string[] suffixes, bool alwaysShowDecimals = true)
#         {
#             if (num == 0)
#             {
#                 return alwaysShowDecimals ? "0.00" : "0";
#             }
#             if (num.Exponent <= 0)
#             {
#                 return num.ToString("F2");
#             }
#
#             double exponent = (double)num.Exponent;
#             int suffixIndex = (int)Math.Floor(exponent / 3);
#
#             string mantissa = (num / BigDouble.Pow(1000, suffixIndex)).ToString("F2");
#             if (!alwaysShowDecimals && mantissa.Contains(".00"))
#             {
#                 mantissa = mantissa.Split('.')[0];
#             }
#
#             string suffix = suffixes[suffixIndex];
#             return (suffix != "") ? mantissa + " " + suffix : mantissa;
#         }
