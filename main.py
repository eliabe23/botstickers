import requests  
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_sticker(self, chat_id, text):
        params = {'chat_id': chat_id, 'sticker': text}
        method = 'sendSticker'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = 'nada'

        return last_update


greet_bot = BotHandler("262863240:AAHreV8hDp_EYAbbmGpcrPCP8_2VJ6HPJtc")  

twobrokegirls = ('2bg', '2 broke girls')
threepercent = ('3%', '3 por cento')
twelvemonkeys = ('12M', '12 monkeys', '12monkeys')
trezerw = ('13 reasons why', '13rw', 'os 13 porques')
trintatrinta = ('30 for 30', '30f30', '30for30')
acasa = ('a casa', 'casa')
americancrime = ('american crime', 'ac')
americancrimestory = ('american crime story', 'acs', 'crime story')
americangods = ('american gods', 'ag')
americanhorrorstory = ('american horror story', 'ahs')
americanhousewife = ('american housewife', 'ah')
angietribeca = ('angie', 'angie tribeca', 'tribeca', 'at')
animalkingdom = ('animal kingdom', 'ak')
arrow = ('arrow', 'naba')
desventuras = ('desventuras em serie', 'des', 'A Series of Unfortunate Events')
ashvsevildead = ('ash vs evil dead', 'aved')
atlanta = ('atlanta')
atypical = ('atypical')
babydaddy = ('baby daddy', 'bd')
ballers = ('ballers')
banshee = ('banshee')
baskets = ('baskets')
bettercallsaul = ('better call saul', 'bcs')
betterthings = ('better things')
bbus = ('big brother us', 'bbus', 'big brother')
bll = ('bll', 'big little lies')
biglove = ('big love', 'bl')
blackish = ('blackish', 'black-ish')
blackmirror = ('bm', 'black mirror')
blacksails = ('bs', 'black sails')
blindspot = ('blindspot')
bloodline = ('bloodline')
blooddrive = ('blooddrive', 'bd')
broadcity = ('bc', 'broad city')
bninenine = ('b99', 'brooklyn nine nine')
bull = ('bull')
casual = ('casual')
catastrophe = ('catastrophe')
chefstable = ('chefs table', 'ct')
chewinggum = ('chewing gum', 'cg')
chicagofire = ('chicago fire', 'cf', 'cfire')
narcos = ('narcos')
shameless = ('shameless', 'shameless us')
sons = ('sons', 'soa', 'sons of anarchy', 'sonsofanarchy')

def main():  
    new_offset = None

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        if last_update == 'nada':
            print = 'travado'
        else:
            
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']
            
            if '/play ' in last_chat_text:
                nomedaserie = last_chat_text.lower()[6:]
                if nomedaserie in sons:
                    greet_bot.send_sticker(last_chat_id, 'playsonsofanarchy')
                elif nomedaserie in twobrokegirls:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADOgsAAuZdXQGb1rpQJ2A4YwI')
                elif nomedaserie in threepercent:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD5AkAAuZdXQEay_ou6osaBgI')
                elif nomedaserie in twelvemonkeys:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD5gkAAuZdXQHo96ZiTxLXAwI')
                elif nomedaserie in trezerw:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD5wkAAuZdXQGdWO0ZNKK5BQI')
                elif nomedaserie in trintatrinta:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD5wsAAuZdXQHvXn_WRjY8BAI')
                elif nomedaserie in acasa:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD5gsAAuZdXQHeTJgcImHDRQI')
                elif nomedaserie in americancrime:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD6AkAAuZdXQFef4X---i8NQI')
                elif nomedaserie in americancrimestory:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD6QkAAuZdXQHYDfpMl7LuDwI')
                elif nomedaserie in americangods:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADpAsAAuZdXQFl1_dekT6hDwI')
                elif nomedaserie in americanhorrorstory:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD6wkAAuZdXQG5uKKXh4PNRwI')
                elif nomedaserie in americanhousewife:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD-woAAuZdXQHTrmxmJtsFfwI')
                elif nomedaserie in angietribeca:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD_AoAAuZdXQE69ocdunlqgwI')
                elif nomedaserie in animalkingdom:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD7gkAAuZdXQHNK3eF3G0yPwI')
                elif nomedaserie in arrow:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD8woAAuZdXQGqz-Yu1V7oRAI')
                elif nomedaserie in desventuras:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD7wkAAuZdXQHqL3ZpNo8e_gI')
                elif nomedaserie in ashvsevildead:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD_QoAAuZdXQHcnL-7U1wVlgI')
                elif nomedaserie in atlanta:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD8QkAAuZdXQHBmobJsXVqewI')
                elif nomedaserie in atypical:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADMgwAAuZdXQHDFSAuNhnsPAI')
                elif nomedaserie in babydaddy:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADqQsAAuZdXQGZNVBOCjuFlgI')
                elif nomedaserie in ballers:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD8gkAAuZdXQG0h9dLoBdMpQI')
                elif nomedaserie in banshee:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD8wkAAuZdXQE6gJ5Yc020ygI')
                elif nomedaserie in baskets:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD9AkAAuZdXQGWouUD-hwqrwI')
                elif nomedaserie in bettercallsaul:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD9gkAAuZdXQELmKwfo1KZ3gI')
                elif nomedaserie in betterthings:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD9wkAAuZdXQGldCYKHx10KAI')
                elif nomedaserie in bbus:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD9gsAAuZdXQHd5hkDZDR6vAI')	
                elif nomedaserie in bll:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD-AkAAuZdXQHJSnhWxOd5LwI')	
                elif nomedaserie in biglove:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD-goAAuZdXQFP9iCMmk8SYgI')	
                elif nomedaserie in blackish:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADOwsAAuZdXQGur6Qz2dU1EgI')	
                elif nomedaserie in blackmirror:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD-QoAAuZdXQEQeQQVDjrtNAI')	
                elif nomedaserie in blacksails:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD-gkAAuZdXQHMK2yuCn9icwI')	
                elif nomedaserie in blindspot:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD-wkAAuZdXQGZTbsik0eoWQI')	
                elif nomedaserie in bloodline:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD_AkAAuZdXQFg3JFcMpUTRAI')	
                elif nomedaserie in blooddrive:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD6AsAAuZdXQGX7hVvma5dXwI')	
                elif nomedaserie in broadcity:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADPAsAAuZdXQGo8y_zojwOcAI')	
                elif nomedaserie in bninenine:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAD_wkAAuZdXQFR3-68drdQdgI')	
                elif nomedaserie in bull:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADqgsAAuZdXQGYM7ytYVi2XwI')	
                elif nomedaserie in casual:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQAECgAC5l1dAaoQGW8BHWsvAg')	
                elif nomedaserie in catastrophe:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADqwsAAuZdXQFE4Xo61-FIpwI')	
                elif nomedaserie in chefstable:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADAQoAAuZdXQE8fYtoqfjTggI')	
                elif nomedaserie in chewinggum:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADFAwAAuZdXQG-Y8YZtftjxQI')	
                elif nomedaserie in chicagofire:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADAgoAAuZdXQGuTCw32bLxRAI')	
                elif nomedaserie in narcos:
                    greet_bot.send_sticker(last_chat_id, 'CAADAQADRQoAAuZdXQGWXScs1RuLMAI')
                else:
                    greet_bot.send_message(last_chat_id, 'nao entendi')
        

        new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
