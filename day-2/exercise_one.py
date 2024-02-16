def main():
    two_digit_number = input("Type a two digit number: ")

    print(type(two_digit_number))

    first_digit = int(two_digit_number[0])
    second_digit = int(two_digit_number[1])

    result = int(first_digit) + int(second_digit)
    print("Result: " + str(result))


if __name__ == "__main__":
    main()
