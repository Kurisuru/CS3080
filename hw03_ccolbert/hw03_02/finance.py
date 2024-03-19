'''
PROGRAMMER: Christopher Colbert
USERNAME: ccolbert
PROGRAM: finance.py

DESCRIPTION: Mortgage Functions with accelerated payoff option.
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


def mortgage_amortization(amount, rate, term, fixed = 0, variable = 0, increment = 1):
    term_months = term*12
    monthly_rate = rate/100/12
    
    monthly_payment, final_payment = mortgage_payment(amount,rate,term)
    
    #initialize totals
    total_paid = 0
    total_interest = 0
    final_month = 0
    
    title = "MORTGAGE AMORTIZATION SCHEDULE\n"
    
    header = ("\n%8s%33s%33s" %("", r"/----------Payment------------\ ", r" /-----------Total-------------\ "))
    header += ("\n%6s%11s%11s%11s%11s%11s%11s%11s"
              %("month","payment","interest","principle","interest","principle","paid","balance"))
    table = ""
    remaining_balance = amount
        
    #for each month calculate total paid, total interest, 
    for month in range(term_months):
        interest_payment = round(remaining_balance * monthly_rate,2)
        principal_payment = monthly_payment - interest_payment
        
        principal_payment += variable / 100 * principal_payment
        
        principal_payment += fixed / 100 * monthly_payment
        
        #check if principal exceeds remaining balance
        if remaining_balance > principal_payment:
            total_interest += interest_payment
            total_paid += monthly_payment + (fixed / 100 * monthly_payment) + (variable / 100 * (monthly_payment - interest_payment))
            remaining_balance -= principal_payment
            
            #add every incremented month to table
            if (month + 1) % increment == 0:
                table += f"{month+1:6} {monthly_payment:10.2f} {interest_payment:10.2f} {principal_payment:10.2f} {total_interest:10.2f} {total_paid - total_interest:10.2f} {total_paid:10.2f} {remaining_balance:10.2f}\n"
        #if principal is greater than remaining, save last month, final payment,
        else:
            if final_month == 0:
                final_month = month + 1

                # Add final payment for normal payoff option
                interest_payment = remaining_balance * monthly_rate 
                final_payment = remaining_balance
                principal_payment = final_payment - interest_payment
                total_interest += interest_payment
                total_paid += final_payment
                remaining_balance -= final_payment
    if final_month == 0:
        table += f"{term*12:6} {final_payment:10.2f} {interest_payment:10.2f} {principal_payment:10.2f} {total_interest:10.2f} {total_paid - total_interest:10.2f} {total_paid:10.2f} {remaining_balance:10.2f}\n"
    else:
        table += f"{final_month:6} {final_payment:10.2f} {interest_payment:10.2f} {principal_payment:10.2f} {total_interest:10.2f} {total_paid - total_interest:10.2f} {total_paid:10.2f} {remaining_balance:10.2f}\n"
    
    #format summary string
    summary = f"Loan amount: ..........${amount}\n"
    summary += f"Loan rate: ............ {rate}% \n"
    summary += f"Loan term: ............ {term} years\n"
    summary += f"Monthly Payment: ......${monthly_payment:.2f}\n"
    summary += f"Final Payment: ........${final_payment:.2f}\n"
    summary += f"Total Paid: ...........${total_paid:.2f}\n"
    summary += f"Cost of Credit: .......${total_interest:.2f}"
    
    #if accelerated, show time and money saved from original
    if fixed > 0 or variable >0:
        #get original total and interest total
        original_total = 0
        original_interest = 0
        remaining_balance = amount
        
        for month in range(0, term * 12 - 1):
            interest_payment = round(remaining_balance * monthly_rate,2)
            principal_payment = monthly_payment - interest_payment
            original_interest += interest_payment
            original_total += monthly_payment
            remaining_balance -= principal_payment
            
        interest_payment = remaining_balance * monthly_rate
        principal_payment = final_payment - interest_payment
        original_interest += interest_payment
        original_total += final_payment
        remaining_balance -= principal_payment
        
        
        accelerated_years = int(term - final_month / 12)
        accelerated_months = term * 12 - final_month - accelerated_years * 12
        summary += f"\nAccelerated Payoff:"
        summary += f"\nTime Saved: ........... {accelerated_years} years {accelerated_months} months"
        summary += f"\nAmount Saved: .........${original_total - total_paid}"
        summary += f"\nInterest Saved: .......${original_interest - total_interest}"
        summary += f"\nTotal Saved:...........${original_total + original_interest - total_interest - total_paid}"
    
    return (title,summary,header,table)

def mortgage_report(amount, rate, years, increment = 1, fixed = 0, variable = 0):
    report = ""
    for s in mortgage_amortization(amount, rate, years, increment, fixed, variable):
        report += s
    return report
