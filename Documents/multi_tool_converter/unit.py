unit_factors = {
    "meters": 1,
    "feet": 0.3048,
    "kilometers": 1000,
    "miles": 1609.344,
}

def convert_units(value, from_unit, to_unit):
    if from_unit not in unit_factors or to_unit not in unit_factors:
        raise Exception("Unsupported unit")

    meters = value * unit_factors[from_unit]
    converted = meters / unit_factors[to_unit]
    return converted
