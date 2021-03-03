import requests


class MyConverter:
    def __init__(self):
        self.request_cache = dict()
        self.rates_cache = dict()

    def cache_init(self, base_cur):
        self.request_cache = requests.get("http://www.floatrates.com/daily/" + base_cur + ".json").json()
        self.rates_cache["USD"] = self.request_cache.get("usd", {"rate": 1})["rate"]
        self.rates_cache["EUR"] = self.request_cache.get("eur", {"rate": 1})["rate"]

    def get_rate(self, cur_code):
        print("Checking the cache...")
        if rate := self.rates_cache.get(cur_code):
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            rate = self.request_cache.get(cur_code.lower(), {"rate": 0})["rate"]
            self.rates_cache.update({cur_code: rate})
        return rate

    def run(self):
        self.cache_init(input())
        while cur_code := input().upper():
            amount = float(input())
            cur_rate = self.get_rate(cur_code)
            print(f"You received {round(amount * cur_rate, 2)} {cur_code}.")


if __name__ == "__main__":
    conv = MyConverter()
    conv.run()
