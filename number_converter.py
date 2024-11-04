def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def decimal_to_octal(n):
    return oct(n).replace("0o", "")

def decimal_to_hexadecimal(n):
    return hex(n).replace("0x", "").upper()

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def octal_to_decimal(octal_str):
    return int(octal_str, 8)

def hexadecimal_to_decimal(hex_str):
    return int(hex_str, 16)

def binary_to_octal(binary_str):
    decimal = int(binary_str, 2)
    return oct(decimal).replace("0o", "")

def binary_to_hexadecimal(binary_str):
    decimal = int(binary_str, 2)
    return hex(decimal).replace("0x", "").upper()

def octal_to_binary(octal_str):
    decimal = int(octal_str, 8)
    return bin(decimal).replace("0b", "")

def octal_to_hexadecimal(octal_str):
    decimal = int(octal_str, 8)
    return hex(decimal).replace("0x", "").upper()

def hexadecimal_to_binary(hex_str):
    decimal = int(hex_str, 16)
    return bin(decimal).replace("0b", "")

def hexadecimal_to_octal(hex_str):
    decimal = int(hex_str, 16)
    return oct(decimal).replace("0o", "")

def main():
    print("Number System Conversion Program")
    print("Select the type of conversion:")
    print("1. Decimal to Binary, Octal, Hexadecimal")
    print("2. Binary to Decimal, Octal, Hexadecimal")
    print("3. Octal to Binary, Decimal, Hexadecimal")
    print("4. Hexadecimal to Binary, Decimal, Octal")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        n = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(n)}")
        print(f"Octal: {decimal_to_octal(n)}")
        print(f"Hexadecimal: {decimal_to_hexadecimal(n)}")

    elif choice == '2':
        binary_str = input("Enter a binary number: ")
        print(f"Decimal: {binary_to_decimal(binary_str)}")
        print(f"Octal: {binary_to_octal(binary_str)}")
        print(f"Hexadecimal: {binary_to_hexadecimal(binary_str)}")

    elif choice == '3':
        octal_str = input("Enter an octal number: ")
        print(f"Binary: {octal_to_binary(octal_str)}")
        print(f"Decimal: {octal_to_decimal(octal_str)}")
        print(f"Hexadecimal: {octal_to_hexadecimal(octal_str)}")

    elif choice == '4':
        hex_str = input("Enter a hexadecimal number: ")
        print(f"Binary: {hexadecimal_to_binary(hex_str)}")
        print(f"Decimal: {hexadecimal_to_decimal(hex_str)}")
        print(f"Octal: {hexadecimal_to_octal(hex_str)}")

    else:
        print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
