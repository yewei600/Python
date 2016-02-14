def fixedPaymentBisection (balance, annualInterestRate):	
	monthlyInterestRate = annualInterestRate/12.0
	#fixedMonthlyPayment = 29150
	originalBalance = balance
	paidOff = False
        upper = (balance*(1+monthlyInterestRate)**12)/12.0 
        lower = balance/12
        

	while lower<=upper and not paidOff:
	        midpoint = (upper+lower)//2
		for i in range (0,12):
			monthlyUnpaidBalance = balance - midpoint
			RemainingBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
			balance = RemainingBalance
			#print "current balance: %d" % balance
		
		if balance ==0:
			paidOff = True
                        print "blance is %d" % balance
		else:
		    if 0 < balance:
		        upper = midpoint-1
		        balance = originalBalance
		    else:
		        lower = midpoint+1

			
	print midpoint

