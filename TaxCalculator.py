# Tax calculator - Asks user to enter the cost and either a country or state tax. It then returns the tax plus the total

cost = float(raw_input("What is the cost?> "))
tax_rate = float(raw_input("What is the tax rate? Please enter in decimal form.> "))
tax = cost*tax_rate
print "tax = " + str(tax)
print "Total cost = " + str(tax+cost)