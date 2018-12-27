def compoundCalculator(initial, return_percent):
  print(return_percent)
  
  balance = initial
  trading_days = 0

  while balance < 135000000000 * 2:
    print('Day ' + str(trading_days) + ' Balance: ' + str(balance))
    balance = balance + (balance * return_percent)
    trading_days += 1

print(compoundCalculator(400, (442.13 - 400) / 400))