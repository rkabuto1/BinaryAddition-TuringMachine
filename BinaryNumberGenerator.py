import random
from decimal import Decimal, getcontext
getcontext().prec = 100

def generate_binary_real(min_len=30, max_len=50):
    int_len = random.randint(min_len // 2, max_len // 2)
    frac_len = random.randint(min_len // 2, max_len // 2)
    int_part = ''.join(random.choices('01', k=int_len)).lstrip('0') or '0'
    frac_part = ''.join(random.choices('01', k=frac_len))
    return f"{int_part}.{frac_part}"

def binary_to_decimal(binary_str):
    if '.' not in binary_str:
        binary_str += '.0'
    int_part, frac_part = binary_str.split('.')
    value = 0
    for i, bit in enumerate(int_part[::-1]):
        if bit == '1':
            value += 2 ** i
    for i, bit in enumerate(frac_part):
        if bit == '1':
            value += Decimal(2) ** Decimal(-(i + 1))
    return Decimal(value)

def decimal_to_binary(value):
    int_part = int(value)
    frac_part = value - int_part

    int_bin = bin(int_part)[2:] if int_part != 0 else '0'
    frac_bin = ''
    count = 0
    while frac_part != 0 and count < 100:
        frac_part *= 2
        digit = int(frac_part)
        frac_bin += str(digit)
        frac_part -= digit
        count += 1

    return f"{int_bin}.{frac_bin}" if frac_bin else f"{int_bin}.0"

def normalize_binary_output(binary_str):
    int_part, frac_part = binary_str.split('.')

    if int_part != '0':
        int_part = int_part.lstrip('0')

    frac_part = frac_part.rstrip('0')

    if not frac_part:
        frac_part = '0'

    return f"{int_part}.{frac_part}"

def generate_test_case():
    X = generate_binary_real()
    Y = generate_binary_real()

    X_dec = binary_to_decimal(X)
    Y_dec = binary_to_decimal(Y)
    Z_dec = X_dec + Y_dec

    Z_bin_raw = decimal_to_binary(Z_dec)
    Z_bin = normalize_binary_output(Z_bin_raw)

    return f"{X}#{Y}", Z_bin

if __name__ == "__main__":
    num_tests = 10  
    for i in range(num_tests):
        input_str, expected_output = generate_test_case()
        print(f"Input:    {input_str}")
        print(f"Expected: {expected_output}")
        print("-" * 60)
