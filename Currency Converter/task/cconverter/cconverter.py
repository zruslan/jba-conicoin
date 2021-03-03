# write your code here!
import requests
import json

cur_rates = {"RUB": 2.98,
             "ARS": 0.82,
             "HNL": 0.17,
             "AUD": 1.9622,
             "MAD": 0.208}


URL = "http://www.floatrates.com/daily/"

cur_code = input()

r = requests.get(URL + cur_code + ".json")
resp = json.loads(r.text)
print(resp["usd"])
print(resp["eur"])


# coins = float(input())
# if coins.is_integer():
#     coins = int(coins)

# print(*[f"I will get {round(coins * rate, 2)} {cur} from the sale of {coins} conicoins." for cur, rate in
#        cur_rates.items()], sep="\n")

# coins = int(input("Please, enter the number of conicoins you have: "))
# rate = float(input("Please, enter the exchange rate: "))
# dollars = int(coins * rate) if rate.is_integer() else round(coins * rate, 2)
# print("The total amount of dollars: ", dollars)
