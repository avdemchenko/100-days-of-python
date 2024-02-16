def main():
    age = input("What is your current age? ")

    years = 90 - int(age)
    months = round(years * 12)
    weeks = round(years * 52)
    days = round(years * 365)

    print(f"You have {days} days, {weeks} weeks, and {months} months left.")


if __name__ == "__main__":
    main()
