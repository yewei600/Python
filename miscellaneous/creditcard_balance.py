def creditcard_balance (balance,annualInterestRate,monthlyPaymentRate):
#balance:  the outstanding balance on the credit card
#annualInterestRate:  annual interest rate as a decimal
#monthlyPaymentRate:  minimum monthly payment rate as a decimal
    totalPaid = 0
    for i in range(0,12):
        minMonthPayment = monthlyPaymentRate * balance
        remainingBalance = balance - minMonthPayment
        monthlyUnpaidBalance = balance - minMonthPayment
        remainingBalance = monthlyUnpaidBalance + (annualInterestRate/12.0)*monthlyUnpaidBalance       
        print "Month: %d" %(i+1)
        print "Minimum monthly payment: %.2f" % minMonthPayment
        print "Remaining balance: %.2f" % remainingBalance
        balance = remainingBalance
        totalPaid +=minMonthPayment
    
    print "Total paid: %.2f" % totalPaid
    print "Remaining balance: %.2f" % balance
        
        

        
    