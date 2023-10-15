def expected_utility_without_information():
    # Supongamos que sin información adicional, la utilidad esperada es 10.
    return 10

def expected_utility_with_information():
    # Supongamos que con información adicional, la utilidad esperada es 15.
    return 15

def value_of_information():
    expected_utility_no_info = expected_utility_without_information()
    expected_utility_with_info = expected_utility_with_information()
    return expected_utility_with_info - expected_utility_no_info

voi = value_of_information()
print("Valor de la Informacion:", voi)
