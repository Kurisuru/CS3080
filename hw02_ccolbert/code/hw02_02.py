'''
PROGRAMMER:..Christopher Colbert
USERNAME:....ccolbert
PROGRAM:.....hw02_02.py

DESCRIPTION: Takes user input of loan amount, loan APR, and loan term length and calculates monthly payment,
final month payment, total amount paid, and cost of credit
'''

def mortgage_residual(loan_amount, loan_apr, loan_term, monthly_payment):
    #Convert APR to monthly interest and monthly payment amount
    monthly_interest_rate= (loan_apr/100)/12
    remaining_balance=loan_amount

    #for each month
    for month in range(1, loan_term*12 + 1):
        #subtracting interest from payment
        monthly_interest_amount= round(remaining_balance * monthly_interest_rate, 2)
        principal_payment = monthly_payment - monthly_interest_amount
        
        #take payment - interest out of balance
        remaining_balance -= principal_payment
    return remaining_balance
#end mortgage_residual function

def mortgage_payment(loan_amount, loan_apr, loan_term):
    monthly_interest_rate= (loan_apr/100)/12
    
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** (loan_term * 12)) / ((1 + monthly_interest_rate) ** (loan_term * 12) - 1)
    
    final_payment = monthly_payment + mortgage_residual(loan_amount, loan_apr, loan_term, monthly_payment)
    #* (1 + monthly_interest_rate) ** (loan_term * 12) - loan_amount
    
    return monthly_payment, final_payment
#end mortgage_payment function

#Main program
print("DATA ENTRY")
loan_amount = float(input("Enter loan amount ($): .. "))
loan_apr = float(input("Enter loan APR (%): ..... "))
loan_term = int(input("Enter loan term (yrs): .. "))

monthly_payment, final_payment = mortgage_payment(loan_amount, loan_apr, loan_term)
residual_balance = mortgage_residual(loan_amount, loan_apr, loan_term, monthly_payment)

#Print results
print("MORTGAGE TERMS")
print("Loan Amount: ......... $%10.2f" % loan_amount)
print("Loan Rate: ........... %11.3f%%" % loan_apr)
print("Loan Term: ........... %11d years" % loan_term)
print("Monthly Payment: ..... $%10.2f" % monthly_payment)
print("Final Amount: ........ $%10.2f" % (monthly_payment + residual_balance))
print("Total Payment: ....... $%10.2f" % (monthly_payment * loan_term * 12))
print("Cost of Credit: ...... $%10.2f" % (monthly_payment * loan_term * 12 - loan_amount + residual_balance))