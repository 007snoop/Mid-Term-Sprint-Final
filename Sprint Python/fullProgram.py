
def menu():
    import time
    while True:
        print()
        print("HAB Taxi Services")
        print("Company Services System")
        print()
        print("1. Enter a New Employee (Driver).")
        print("2. Enter Company Revenues. (under construction)")
        print("3. Enter Company Expenses. (under construction)")
        print("4. Track Car Rentals. (under construction)")
        print("5. Record Employee Payment. (under construction)")
        print("6. Print Company Profit listing. (under construction)")
        print("7. Driver Financial Listing. ")
        print("8. Corporate Summary Report.")
        print("9. Quit program.")

        choice = input("Enter Choice (1-9): ")
        if choice == "9":
            time.sleep(2)
            print(f"Thanks for using this program. You will never leave this program.")
            break
        if choice == "1":
            driver()
        if choice == "7":
            driverFinancialListing()
        if choice == "8":
            corporateSummaryReport() 
        if choice == "3" or choice == "2" or choice == "4" or choice == "5" or choice == "6":
            underConstruction()


def underConstruction()
    while True:
        print("|--------------------------------|")
        print("|     page under construction    |")
        print("|                                |")
        print("|              please            |")
        print("|                go              |")
        print("|               away             |")
        print("|                                |")
        print("|                    signed:     |")
        print("|                         Colin  |")
        print("|--------------------------------|")
        exitCode = input(f"Page Under construction, Please enter 'back' to continue: ").title()
        if exitCode == "Back":
            break

def corporateSummaryReport():# this is luciens code. this may not work with the program, if its an issue, please comment this entire function out.
    import datetime

    # Load Defaults from Defaults.dat file
    def LoadDefaults():
        Defaults = {}
        with open("Defaults_(2).dat", "r") as File:
            for Line in File:
                Key, Value = Line.strip().split("=")
                Defaults[Key] = float(Value) if Value.replace('.', '', 1).isdigit() else int(Value)
        return Defaults

    # Save Defaults back to the file
    def SaveDefaults(Defaults):
        with open("Defaults_(2).dat", "w") as File:
            for Key, Value in Defaults.items():
                File.write(f"{Key}={Value}\n")

    # Define data structures
    Employees = []
    Revenues = []
    Expenses = []
    Rentals = []
    Payments = []

    # Function to add a new driver
    def AddDriver(Name, Address, PhoneNumber, LicenseNumber, LicenseExpiry, InsuranceCompany, PolicyNumber, OwnCar):
        DriverNumber = Defaults["NextDriverNumber"]
        Employees.append({
            "DriverNumber": DriverNumber,
            "Name": Name,
            "Address": Address,
            "PhoneNumber": PhoneNumber,
            "LicenseNumber": LicenseNumber,
            "LicenseExpiry": LicenseExpiry,
            "InsuranceCompany": InsuranceCompany,
            "PolicyNumber": PolicyNumber,
            "OwnCar": OwnCar,
            "BalanceDue": 0.0
        })
        Defaults["NextDriverNumber"] += 1
        SaveDefaults(Defaults)

    # Function to record a new revenue
    def RecordRevenue(DriverNumber, Description, Amount):
        TransactionID = Defaults["NextTransactionNumber"]
        HST = Amount * Defaults["HSTRate"]
        Total = Amount + HST
        Revenues.append({
            "TransactionID": TransactionID,
            "Date": str(datetime.date.today()),
            "Description": Description,
            "DriverNumber": DriverNumber,
            "Amount": Amount,
            "HST": HST,
            "Total": Total
        })
        for Employee in Employees:
            if Employee["DriverNumber"] == DriverNumber:
                Employee["BalanceDue"] += Total
        Defaults["NextTransactionNumber"] += 1
        SaveDefaults(Defaults)

    # Function to record an expense
    def RecordExpense(DriverNumber, Items):
        InvoiceNumber = Defaults["NextTransactionNumber"]
        Subtotal = sum(Item["Cost"] * Item["Quantity"] for Item in Items)
        HST = Subtotal * Defaults["HSTRate"]
        Total = Subtotal + HST
        Expenses.append({
            "InvoiceNumber": InvoiceNumber,
            "InvoiceDate": str(datetime.date.today()),
            "DriverNumber": DriverNumber,
            "Items": Items,
            "Subtotal": Subtotal,
            "HST": HST,
            "Total": Total
        })
        Defaults["NextTransactionNumber"] += 1
        SaveDefaults(Defaults)

    # Function to record a rental
    def RecordRental(DriverNumber, StartDate, CarNumber, Duration, IsWeekly):
        RentalID = Defaults["NextTransactionNumber"]
        RentalCost = Defaults["WeeklyRentalFee"] if IsWeekly else Defaults["DailyRentalFee"] * Duration
        HST = RentalCost * Defaults["HSTRate"]
        Total = RentalCost + HST
        Rentals.append({
            "RentalID": RentalID,
            "DriverNumber": DriverNumber,
            "StartDate": StartDate,
            "CarNumber": CarNumber,
            "Duration": Duration,
            "RentalCost": RentalCost,
            "HST": HST,
            "Total": Total
        })
        for Employee in Employees:
            if Employee["DriverNumber"] == DriverNumber:
                Employee["BalanceDue"] += Total
        Defaults["NextTransactionNumber"] += 1
        SaveDefaults(Defaults)

    # Function to record a payment
    def RecordPayment(DriverNumber, Amount, Reason, PaymentMethod):
        PaymentID = Defaults["NextTransactionNumber"]
        Payments.append({
            "PaymentID": PaymentID,
            "DriverNumber": DriverNumber,
            "Date": str(datetime.date.today()),
            "Amount": Amount,
            "Reason": Reason,
            "PaymentMethod": PaymentMethod
        })
        for Employee in Employees:
            if Employee["DriverNumber"] == DriverNumber:
                Employee["BalanceDue"] -= Amount
        Defaults["NextTransactionNumber"] += 1
        SaveDefaults(Defaults)

    # Function to generate a corporate summary report
    def GenerateCorporateSummary():
        TotalRevenues = sum(Revenue["Total"] for Revenue in Revenues)
        TotalExpenses = sum(Expense["Total"] for Expense in Expenses)
        TotalRentals = sum(Rental["Total"] for Rental in Rentals)
        TotalPayments = sum(Payment["Amount"] for Payment in Payments)
        TotalBalanceDue = sum(Employee["BalanceDue"] for Employee in Employees)
        
        Report = f"""
        Corporate Summary Report:
        -------------------------
        Total Revenues: ${TotalRevenues:.2f}
        Total Expenses: ${TotalExpenses:.2f}
        Total Rentals: ${TotalRentals:.2f}
        Total Payments: ${TotalPayments:.2f}
        Total Balance Due from Employees: ${TotalBalanceDue:.2f}
        """
        
        print(Report)


    # Initialize defaults
    global Defaults
    Defaults = LoadDefaults()

    # Main loop
    while True:
        print("1. Add Driver")
        print("2. Record Revenue")
        print("3. Record Expense")
        print("4. Record Rental")
        print("5. Record Payment")
        print("6. Generate Corporate Summary Report")
        print("7. Exit")

        Choice = input("Enter your choice: ").strip()

        if Choice == "1":
            Name = input("Enter Driver Name: ")
            Address = input("Enter Address: ")
            PhoneNumber = input("Enter Phone Number: ")
            LicenseNumber = input("Enter Driver's License Number: ")
            LicenseExpiry = input("Enter License Expiry Date (YYYY-MM-DD): ")
            InsuranceCompany = input("Enter Insurance Company: ")
            PolicyNumber = input("Enter Insurance Policy Number: ")
            OwnCar = input("Does the driver own a car? (True/False): ").strip().lower() == "true"
            AddDriver(Name, Address, PhoneNumber, LicenseNumber, LicenseExpiry, InsuranceCompany, PolicyNumber, OwnCar)

        elif Choice == "2":
            DriverNumber = int(input("Enter Driver Number: "))
            Description = input("Enter Description: ")
            Amount = float(input("Enter Amount: "))
            RecordRevenue(DriverNumber, Description, Amount)

        elif Choice == "3":
            DriverNumber = int(input("Enter Driver Number: "))
            Items = []
            while True:
                ItemNumber = input("Enter Item Number: ")
                Description = input("Enter Item Description: ")
                Cost = float(input("Enter Item Cost: "))
                Quantity = int(input("Enter Item Quantity: "))
                Items.append({"ItemNumber": ItemNumber, "Description": Description, "Cost": Cost, "Quantity": Quantity})
                MoreItems = input("Add more items? (y/n): ").strip().lower()
                if MoreItems != "y":
                    break
            RecordExpense(DriverNumber, Items)

        elif Choice == "4":
            DriverNumber = int(input("Enter Driver Number: "))
            StartDate = input("Enter Rental Start Date (YYYY-MM-DD): ")
            CarNumber = int(input("Enter Car Number (1-4): "))
            Duration = int(input("Enter Rental Duration (in days): "))
            IsWeekly = input("Is this a weekly rental? (y/n): ").strip().lower() == "y"
            RecordRental(DriverNumber, StartDate, CarNumber, Duration, IsWeekly)

        elif Choice == "5":
            DriverNumber = int(input("Enter Driver Number: "))
            Amount = float(input("Enter Payment Amount: "))
            Reason = input("Enter Payment Reason: ")
            PaymentMethod = input("Enter Payment Method (Cash/Debit/Visa): ")
            RecordPayment(DriverNumber, Amount, Reason, PaymentMethod)

        elif Choice == "6":
            GenerateCorporateSummary()

        elif Choice == "7":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def driverFinancialListing():
    # Description: Driver Financial report for HAB Taxi Services.
    # Author: Cody Collins
    # Date(s): Aug 2 2024 - Aug 6 2024
    
    
    # Define required libraries.
    import datetime
    import FormatValues as FV
    import sys
    import time

    
    # Define program constants.


    # Define program functions.

    def ProgressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
        # Generate and display a progress bar with % complete at the end.

        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
        sys.stdout.flush()   
        
    # Main report processing starts here.
    while True:
        while True:
            StartDate = input("Enter the start date of the report (YYYY-MM-DD): ")
            if StartDate == "":
                print()
                print("ERROR - Start date cannot be blank.")
                print()
            else:
                StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d").date()
                break
        while True:
            EndDate = input("Enter the end date of the report (YYYY-MM-DD): ")
            if EndDate == "":
                print()
                print("ERROR - End date cannot be blank.")
                print()
            else:
                EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d").date()
                break


        RepPeriod = EndDate - StartDate
        RepPeriodStr = f"{RepPeriod.days} days"

        # Generate a progress bar to indicate report loading.
        print()
        TotalIterations = 30 
        Message = "Loading Report ..."

        for i in range(TotalIterations + 1):
            time.sleep(0.1)  
            ProgressBar(i, TotalIterations, prefix=Message, suffix='Complete', length=50)
        print()
        
        # Generate report headings.
        print()
        print(f"                             HAB Taxi Services")
        print(f"                          Driver Financial Report")
        print(f"Start Date: {StartDate}                              End Date: {EndDate}")
        print(f"Period: {RepPeriodStr}")
        print(f"========================================================================")
        print(f"Driver       Payment     Payment       Payment       Payment       Bal")
        print(f"  ID           ID         Date         Amount        Method        Due")
        print(f"========================================================================")


        
        # Initialize counters and accumulators.
        PayAcc = 0
        TransCtr = 0

        # Open the data file.
        f = open('driver_pay_info.dat', 'r')

        
        # Process each line (record) in the file in a loop.
        while True:
            for DriverRecords in f:
                
                # Read the record.  Grab values from the list.
                DriverLst = DriverRecords.split(",")

                PayID = DriverLst[0].strip()
                DriverNum = DriverLst[1].strip()
                PayDateStr = DriverLst[2].strip()
                PayDate = datetime.datetime.strptime(PayDateStr, "%Y-%m-%d").date()
                PayAmt = float(DriverLst[3].strip())
                PayReason = DriverLst[4].strip()
                PayMethod = DriverLst[5].strip()
                BalDue = float(DriverLst[6].strip())

                
                # Check if the PayDate is within the specified range.
                if StartDate <= PayDate <= EndDate:
                    # Display the detail line.
                    print(f" {DriverNum:<4s}         {PayID:<3s}      {PayDate}      {FV.FDollar2(PayAmt):<9s}     {PayMethod:<6s}    {FV.FDollar2(BalDue):>9s}")
                
                    # Update counters and accumulators.
                    PayAcc += PayAmt
                    TransCtr += 1

                else:
                    print(f"  No records found for this date range. Please check the date entered.")
                    
                    continue
        
            

            # break the loop once all records have been processed.
            break

            
        # Close the file.
        f.close()
        
        # Print summary data - counters and accumulators.
        print(f"========================================================================")
        print(f"Total Payments:     {FV.FDollar2(PayAcc)}")
        print(f"Total Transactions: {TransCtr}")
        print()
        print(f"End of Report")
        print()

        # Prompt user if they would like to enter another report.
        while True:
            ContinueChoice = input("Do you want generate another report? (Y/N): ")
            if ContinueChoice.upper() == "Y":
                break
            elif ContinueChoice.upper() == "N":
                print()
                print("Thank you for using this program!")
                print()
                time.sleep(1)
                menu()
            else:
                print("Invalid choice. Please enter Y or N.")


def driver():
    import datetime
    import time

    currDate = datetime.datetime.now()
    currDate = currDate.strftime("%d-%m-%Y")

    def employee_begin():
        print("Welcome to HAB taxi services")
        time.sleep(1.5)
        print("Please wait as company services system is loading")
        time.sleep(1.5)
        print(".")
        time.sleep(1.5)
        print("..")
        time.sleep(1.5)
        print("...")
        time.sleep(1)
        print("System's Ready!")
        time.sleep(1)

    def employee_generate():
        time.sleep(1.5)
        print("Please wait we are gathering your information")
        time.sleep(1.5)
        print(".")
        time.sleep(1.5)
        print("..")
        time.sleep(1.5)
        print("...")
        time.sleep(1)
        print("Here is your driver's information")
        time.sleep(1)



    def enter_new_employee():
        f = open('defaults.dat', 'r')
        NEXT_TRANS_NUM = int(f.readline())
        NEXT_DRIVER_NUM = int(f.readline())
        MONTHLY_STAND_FEE = float(f.readline())
        DAILY_RENTAL_FEE = float(f.readline())
        WEEKLY_RENTAL_FEE = float(f.readline())
        HST_RATE = float(f.readline())
        f.close()

        employee_begin()

        while True:
            while True:
                driver_name = input("Please enter driver's name: ").title()
                if driver_name == "":
                    print("Data entry error - Cannot be left blank, input valid driver's name.")
                elif driver_name.isalpha() == False:
                    print("Data entry error - Driver's name must be letter, Please try again")
                else:
                    break
            while True:
                driver_address = input("Please enter driver's address: ").title()
                if driver_address == "":
                    print("Data entry error - Cannot be left blank, input valid driver's address.")
                else:
                    break
            while True:
                driver_phone_num = input("Please enter driver's phone number: ")
                if driver_phone_num == "":
                    print("Data entry error - Cannot be left blank, input valid driver's phone number.")
                elif driver_phone_num.isalpha() == True:
                    print("Data entry error - Driver's phone number must be number, Please try again")
                else:
                    break
            while True:
                driver_license_num = input("Please enter driver's license number: ")
                if driver_license_num == "":
                    print("Data entry error - Cannot be left blank, input valid driver's license number.")
                elif driver_license_num.isalpha() == True:
                    print("Data entry error - Driver's license number must be number, Please try again")
                else:
                    break
            while True:
                driver_license_expiry_date = input("Please enter driver's licnese expiry date (DD-MM-YYYY): ")
                if driver_license_expiry_date == "":
                    print("Data entry error - Cannot be left blank, input valid driver's licnese expiry date.")
                elif driver_license_expiry_date.isalpha() == True:
                    print("Data entry error - Driver's license expiry date must be number, Please try again")
                elif len(driver_license_expiry_date) != 10:
                    print("Data entry error - Date too long or too short, input valid driver's license expiry date.")
                elif driver_license_expiry_date[2] != "-" or driver_license_expiry_date[5] != "-":
                    print("Data entry error - Must be a slash separating numbers, input valid driver's license expiry date.")
                elif not driver_license_expiry_date[:2].isdigit():
                    print("Data entry error - Date must contain only numbers, input valid driver's license expiry date.")
                elif not driver_license_expiry_date[3:4].isdigit():
                    print("Data entry error - Date must contain only numbers, input valid driver's license expiry date.")
                elif not driver_license_expiry_date[-4:].isdigit():
                    print("Data entry error - Date must contain only numbers, input valid driver's license expiry date.")
                else:
                    break
            while True:
                driver_insurance_company = input("Please enter driver's insurance company: ").title()
                if driver_insurance_company == "":
                    print("Data entry error - Cannot be left blank, input valid driver's insurance company.")
                elif driver_insurance_company.isalpha() == False:
                    print("Data entry error - Driver's insurance company must be letter, Please try again")
                else:
                    break
            while True:
                driver_insurance_policy_num = input("Please enter driver's insurance policy number: ")
                if driver_insurance_policy_num == "":
                    print("Data entry error - Cannot be left blank, input valid driver's insurance policy number.")
                elif driver_phone_num.isalpha() == True:
                    print("Data entry error - Driver's insurance policy number must be number, Please try again")
                else:
                    break
            while True:
                driver_owns_car = input("Please enter if driver own a car (Y/N): ").upper()
                if driver_owns_car == "Y" or driver_owns_car == "N":
                    break
                else:
                    print("Data entry error - Please select Y for yes, or N for no")

            employee_generate()

            print()
            print()
            print(" "* 15 + "HAB Taxi Services Driver's information" + " "* 16)
            print(" "* 14 + "*" * 39 + " "* 14)
            print()
            print(f"Transaction number: {NEXT_TRANS_NUM}")
            print(f"Driver number: {NEXT_DRIVER_NUM}")
            print()
            print(" "* 14 + "*" * 39 + " "* 14)
            print()
            print(f"Driver's name: {driver_name}")
            print(f"Driver's address: {driver_address}")
            print(f"Driver's phone number: {driver_phone_num}")
            print()
            print(" "* 14 + "*" * 39 + " "* 14)
            print()
            print(f"Driver's license number: {driver_license_num}")
            print(f"Driver's license expiry date: {driver_license_expiry_date}")
            print(f"Driver's insurance company: {driver_insurance_company}")
            print(f"Driber's insurance policy number: {driver_insurance_policy_num}")
            if driver_owns_car == "Y":
                print(f"Driver owns his/her car")
            else:
                print(f"Driver does not own his/her car")
            print()

            f = open('driver_info.dat', 'a')
            f.write("{}, ".format(NEXT_TRANS_NUM))
            f.write("{}, ".format(NEXT_DRIVER_NUM))
            f.write("{}, ".format(driver_name))
            f.write("{}, ".format(driver_address))
            f.write("{}, ".format(driver_phone_num))
            f.write("{}, ".format(driver_license_num))
            f.write("{}, ".format(driver_license_expiry_date))
            f.write("{}, ".format(driver_insurance_company))
            f.write("{}, ".format(driver_insurance_policy_num))
            f.write("{}, ".format(driver_owns_car))
            f.close()

            NEXT_DRIVER_NUM += 1
            NEXT_TRANS_NUM += 1
            f = open('defaults.dat', 'w')
            f.write("{}\n ".format(NEXT_TRANS_NUM))
            f.write("{}\n ".format(NEXT_DRIVER_NUM))
            f.write("{}\n ".format(MONTHLY_STAND_FEE))
            f.write("{}\n ".format(DAILY_RENTAL_FEE))
            f.write("{}\n ".format(WEEKLY_RENTAL_FEE))
            f.write("{}\n ".format(HST_RATE))
            f.close()

            #return enter_new_employee()

            cont = input("Do you want to process another Driver? (Y/N): ").upper()
            if cont == "Y":
                print("Starting new application...")
                time.sleep(2)
                continue
            else:
                menu()
    enter_new_employee()



menu()