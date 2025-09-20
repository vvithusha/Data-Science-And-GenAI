import calendar

while True:
    print("\n📅 Calendar Maker")
    print("1. View full year calendar")
    print("2. View calendar of specific month")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        year = int(input("Enter the year: "))
        full_cal = calendar.calendar(year)
        print("\n" + full_cal)

        save = input("Do you want to save this calendar to a .txt file? (yes/no): ").lower()
        if save == "yes":
            with open(f"calendar_{year}.txt", "w") as file:
                file.write(full_cal)
            print(f"✅ Calendar saved as calendar_{year}.txt")

    elif choice == "2":
        year = int(input("Enter the year: "))
        month = int(input("Enter the month (1-12): "))

        month_cal = calendar.month(year, month)
        print("\n" + month_cal)

        save = input("Do you want to save this calendar to a .txt file? (yes/no): ").lower()
        if save == "yes":
            with open(f"calendar_{year}_{month}.txt", "w") as file:
                file.write(month_cal)
            print(f"✅ Calendar saved as calendar_{year}_{month}.txt")

    elif choice == "3":
        print("👋 Exiting Calendar Maker. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice! Please enter 1, 2, or 3.")
