# description: the menu for the sprint
# author: Colin G. Yetman
#date(s): 2024-08-09


import importlib

PROMGRAM_LIST = {
    0: {"name": "menu", "module": "menu"},
    1: {"name": "New Employee (driver)", "module": "driver"},
    2: {"name": "Company Revenues", "module": "companyRevenues"},
    3: {"name": "Company Expenses", "module": "companyExpenses"},
    4: {"name": "Track Car rentals", "module": "trackCar"},
    5: {"name": "Record Employee Payment", "module": "recordEmployeePayment"},
    6: {"name": "Company Profit listing", "module": "companyProfitList"},
    7: {"name": "Driver Financial listing", "module": "driverFinancialList"},
    8: {"name": "Corporate Summary Report", "module": "corporateSummaryReport"},
    9: {"name": "Exit Program", "module": None}
}
PROMGRAM_LIST[0]
def main():
    print(f"\nProgram Menu")
    print(f"-" * 16)
    for key, value in PROMGRAM_LIST.items():
        print(f"{key}. {value['name']}");
    
    while True:
        choice = int(input("Enter a number between 1 and 9: "));
        if choice > 9 or choice < 1:
            print("Not a valid option, Please select between 1 and 9.")
        else:
            break

    if choice in PROMGRAM_LIST:
        program = PROMGRAM_LIST[choice];

        if program["module"] is not None:
            module = importlib.import_module(program["module"]);
            module.main()
        else:
            print("Exiting Program...")
            exit(0)
    else:
        print("Please choose a number between 1 and 9.")

if __name__ == "__main__":
    main()