temperature_units = ["celsius", "fahrenheit", "kelvin"]

def convert_temperature(value, from_temp, to_temp):
    if from_temp == to_temp:
        return value

    if from_temp == "celsius":
        celsius = value
    elif from_temp == "fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_temp == "kelvin":
        celsius = value - 273.15
    else:
        raise Exception("Unsupported temperature unit")

    if to_temp == "celsius":
        converted = celsius
    elif to_temp == "fahrenheit":
        converted = celsius * 9/5 + 32
    elif to_temp == "kelvin":
        converted = celsius + 273.15
    else:
        raise Exception("Unsupported temperature unit")

    return converted

