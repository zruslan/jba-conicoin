# write your code here!
coins = int(input("Please, enter the number of conicoins you have: "))
rate = float(input("Please, enter the exchange rate: "))
dollars = int(coins * rate) if rate.is_integer() else round(coins * rate, 2)
print("The total amount of dollars: ", dollars)
