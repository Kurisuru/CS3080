'''
PROGRAMMER:..Christopher Colbert
USERNAME:....ccolbert
PROGRAM:.....hw01_01.py

DESCRIPTION: Simulate a loan given the amount, APR, term length, and minimum
payment. Outputs the final payment amount, and the residual balance.
'''
#recieve user input
print("DATA ENTRY")
loan_amount = float(input("Enter loan amount ($): "))
loan_apr = float(input("Enter loan APR (%): "))
loan_term = int(input("Enter loan term (yrs): "))
loan_monthly_payment = float(input("Enter monthly payment ($): "))

#Convert APR to monthly interest and monthly payment amount
monthly_interest_rate= (loan_apr/100)/12
remaining_balance=loan_amount

#for each month
for month in range(1, loan_term*12 + 1):
    #subtracting interest from payment
    monthly_interest_amount= round(remaining_balance * monthly_interest_rate, 2)
    principal_payment = loan_monthly_payment - monthly_interest_amount
    
    #take payment - interest out of balance
    remaining_balance -= principal_payment

#Print results
print("ANALYSIS RESULTS")
print("Loan Rate: ........... %11.3f%%" % loan_apr)
print("Loan Term: ........... %11d years" % loan_term)
print("Loan Amount: ......... $%10.2f" % loan_amount)
print("Monthly Payment: ..... $%10.2f" % loan_monthly_payment)
print("Residual Balance: .... $%10.2f" % remaining_balance)
print("Final Amount: ........ $%10.2f" % (loan_monthly_payment + remaining_balance))
