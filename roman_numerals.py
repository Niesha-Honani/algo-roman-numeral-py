def to_roman(num):
    # write you
    output = ''
    roman_numeral_to_arabic = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    for k, v in reversed(roman_numeral_to_arabic.items()):
        evenly_divisible = num//v
        if evenly_divisible >=1:
            output += k * evenly_divisible
            num -= v * evenly_divisible

    return output
