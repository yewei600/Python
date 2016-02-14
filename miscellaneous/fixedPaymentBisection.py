def fixedPayment (balance, annualInterestRate):	
	monthlyInterestRate = annualInterestRate/12.0
	fixedMonthlyPayment = 99634.0
	originalBalance = balance
	paidOff = False

	while not paidOff:
		for i in range (0,12):
			monthlyUnpaidBalance = balance - fixedMonthlyPayment
			RemainingBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
			balance = RemainingBalance
			#print "current balance: %d" % balance
		
		if balance <=0:
			paidOff = True
                        print "balance is %d" % balance
		else:
			fixedMonthlyPayment+=10
			balance = originalBalance
			#print "RESET balance: %d" % balance

	print fixedMonthlyPayment

