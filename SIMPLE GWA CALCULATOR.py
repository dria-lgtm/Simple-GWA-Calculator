# Simple GWA Calculator
gwa_records = {"1st": None, "2nd": None, "3rd": None, "4th": None}

def get_letter_grade(gwa):
    if gwa >= 90: return "A"
    if gwa >= 80: return "B"
    if gwa >= 70: return "C"
    if gwa >= 60: return "D"
    return "F"

def calculate_gwa():
    n = int(input("Enter number of subjects: "))
    total = 0
    for i in range(1, n + 1):
        while True:
            grade = float(input(f"Grade for subject {i}: "))
            if 0 <= grade <= 100:
                total += grade
                break
            print("Invalid. Enter 0–100.")
    return round(total / n, 2)

def save_gwa():
    print("\nSelect Quarter: 1.1st 2.2nd 3.3rd 4.4th")
    choice = input("Choice: ")
    quarters = {"1": "1st", "2": "2nd", "3": "3rd", "4": "4th"}
    if choice in quarters:
        gwa_records[quarters[choice]] = calculate_gwa()
        print(f"GWA for {quarters[choice]} saved.")
    else:
        print("Invalid choice.")

def view_records():
    print("\n--- GWA Records ---")
    for q, g in gwa_records.items():
        if g is None:
            print(f"{q} Quarter: No record")
        else:
            print(f"{q} Quarter: {g} ({get_letter_grade(g)})")

def main_menu():
    while True:
        print("\nMenu: 1.Calculate & Save 2.View Records 3.Exit")
        choice = input("Choice: ")
        if choice == "1": save_gwa()
        elif choice == "2": view_records()
        elif choice == "3":
            print("Goodbye!")
            break
        else: print("Invalid choice.")

main_menu()
