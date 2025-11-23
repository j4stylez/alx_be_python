task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        priority_msg = "high priority task"
    case "medium":
        priority_msg = "medium priority task"
    case "low":
        priority_msg = "low priority task"
    case _:
        priority_msg = "task with an unknown priority"

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_msg} that requires immediate attention today!")
else:
    print(f"Reminder: '{task}' is a {priority_msg}. Consider completing it when you have free time.")


