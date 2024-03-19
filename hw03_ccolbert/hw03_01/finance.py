'''
PROGRAMMER: Christopher Colbert
USERNAME: ccolbert
PROGRAM: finance.py

DESCRIPTION: Mortgage Functions
'''

def mortgage_residual(amount, rate, term, payment):
    #Convert APR to monthly interest
    monthly_rate= (rate/100)/12
    
    remaining_balance=amount

    #for each month
    for month in range(0, term*12):
        #subtracting interest from payment
        amount= round(remaining_balance * monthly_rate, 2)
        principal_payment = payment - amount
        
        #take payment - interest out of balance
        remaining_balance -= principal_payment
        
    return remaining_balance
#end mortgage_residual function
    
def mortgage_payment(amount, rate, term):
    #Convert APR to monthly interest 
    monthly_rate= (rate/100)/12
    
    monthly_payment = round(amount * (monthly_rate * (1 + monthly_rate) ** (term * 12)) / ((1 + monthly_rate) ** (term * 12) - 1),2)
    
    final_payment = round(monthly_payment + mortgage_residual(amount, rate, term, monthly_payment),2)
    
    return monthly_payment, final_payment
#end mortgage_payment function


def mortgage_amortization(amount, rate, term, increment=1):
    monthly_rate = rate/100/12
    
    monthly_payment, final_payment = mortgage_payment(amount,rate,term)
    
    total_paid = 0
    total_interest = 0
    
    title = "MORTGAGE AMORTIZATION SCHEDULE\n"
    
    header = ("\n%8s%33s%33s" %("", r"/----------Payment------------\ ", r" /-----------Total-------------\ "))
    header += ("\n%6s%11s%11s%11s%11s%11s%11s%11s"
              %("month","payment","interest","principle","interest","principle","paid","balance"))
    table = ""
    remaining_balance = amount
    
    #for each month
    for month in range(0, term * 12 - 1):
        interest_payment = round(remaining_balance * monthly_rate,2)
        principal_payment = monthly_payment - interest_payment
        total_interest += interest_payment
        total_paid += monthly_payment
        remaining_balance -= principal_payment
        
        #add every increment month to table
        if (month + 1) % increment == 0:
            table += f"{month+1:6} {monthly_payment:10.2f} {interest_payment:10.2f} {principal_payment:10.2f} {total_interest:10.2f} {total_paid - total_interest:10.2f} {total_paid:10.2f} {remaining_balance:10.2f}\n"
        

    # Add final payment
    interest_payment = remaining_balance * monthly_rate
    principal_payment = final_payment - interest_payment
    total_interest += interest_payment
    total_paid += final_payment
    remaining_balance -= principal_payment
    
    table += f"{term * 12:6} {final_payment:10.2f} {interest_payment:10.2f} {principal_payment:10.2f} {total_interest:10.2f} {total_paid - total_interest:10.2f} {total_paid:10.2f} {remaining_balance:10.2f}\n"
    
    #format summary string
    summary = f"Loan amount: ......${amount}\n"
    summary += f"Loan rate: ........ {rate}% \n"
    summary += f"Loan term: ........ {term} years\n"
    summary += f"Monthly Payment: ..${monthly_payment:.2f}\n"
    summary += f"Final Payment: ....${final_payment:.2f}\n"
    summary += f"Total Paid: .......${total_paid:.2f}\n"
    summary += f"Cost of Credit: ...${total_interest:.2f}"
    
    return (title,summary,header,table)

def mortgage_report(amount, rate, years, increment = 1):
    
    report = ""
    for s in mortgage_amortization(amount, rate, years, increment):
        report += s
    return report
