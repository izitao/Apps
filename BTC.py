import requests
import time
import json

def main():

    def get_actual_rate(link):
        '''Gets actual rate info from API'''
        response = requests.get(link)
        print(response.status_code)
        acutal_rate = response.json()
        print(acutal_rate)
        for key,value in acutal_rate.items():
            print(key, value)

        actual_time = acutal_rate['time']['updated']
        actual_rate_eur = acutal_rate['bpi']['EUR']['rate_float']
        actual_rate_usd = acutal_rate['bpi']['USD']['rate_float']
        actual_rate_gbp = acutal_rate['bpi']['GBP']['rate_float']

        save_course(course_file, actual_time, actual_rate_eur)
        return {'actual_time': actual_time, 'actual_rate_EUR': actual_rate_eur}


    def save_course(course_file, actual_time, actual_rate_eur):
        '''Saves into course_file history of rates'''
        new_data = {"time": actual_time, "actual rate": actual_rate_eur}
        print(new_data)

        with open(course_file) as cf:
            data = json.load(cf)
            temp = data["data"]
            temp.append(new_data)

        with open(course_file, "w") as cf:
            json.dump(data, cf, indent=4)
            cf.close()

    def buy_btc(buy_file, amount_eur, actual_time, actual_rate):
        bitcoins_bought = float(amount_eur)/float(actual_rate)
        buy_log = {'time': actual_time,'euros inserted': amount_eur, 'amount_of_BTC_bought': bitcoins_bought, 'rate': actual_rate }

        with open(buy_file) as bf:
            data_buy = json.load(bf)
            temp_buy = data_buy["buy_history"]
            temp_buy.append(buy_log)

        with open(buy_file, "w") as bf:
            json.dump(data_buy, bf, indent=4)


    link ="https://api.coindesk.com/v1/bpi/currentprice.json?fbclid=IwAR3-1uFyFyyp4bHDQRBdTb4ekxpzWI3gYjjUKgqzZ_rCNSJnVuQASub8j-w"
    course_file = "course.json"
    buy_file = "buy_file.json"
    buy = False

    while True:
        time.sleep(1)
        act_rate = get_actual_rate(link)
        if buy == True:
            amount_eur = float(input('How many Euros you want to insert? '))
            buy_btc(buy_file, amount_eur, act_rate['actual_time'], act_rate['actual_rate_EUR'])
            amount = 0
            buy = False

if __name__ == "__main__":
    main()



