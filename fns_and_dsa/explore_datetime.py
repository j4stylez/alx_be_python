from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days):
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Future date calculation
    days_input = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date, days_input)

if __name__ == "__main__":
    main()
