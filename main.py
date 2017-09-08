import telepot

telegram = telepot.Bot("262863240:AAHreV8hDp_EYAbbmGpcrPCP8_2VJ6HPJtc")

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
seriecadastradas = ('nome da serie')

def recebendoMsg(msg):
    frase = msg['text']
    frase = frase.lower()
    tipoMsg, tipoChat, chatID = telepot.glance(msg)

    if '/play ' in frase:
        nomedaserie = frase[6:]
        if nomedaserie in sons:
            resp = 'playsonsofanarchy'
        elif nomedaserie in twobrokegirls:
            resp = 'CAADAQADOgsAAuZdXQGb1rpQJ2A4YwI'
        elif nomedaserie in threepercent:
            resp = 'CAADAQAD5AkAAuZdXQEay_ou6osaBgI'
        elif nomedaserie in twelvemonkeys:
            resp = 'CAADAQAD5gkAAuZdXQHo96ZiTxLXAwI'
        elif nomedaserie in trezerw:
            resp = 'CAADAQAD5wkAAuZdXQGdWO0ZNKK5BQI'
        elif nomedaserie in trintatrinta:
            resp = 'CAADAQAD5wsAAuZdXQHvXn_WRjY8BAI'
        elif nomedaserie in acasa:
            resp = 'CAADAQAD5gsAAuZdXQHeTJgcImHDRQI'
        elif nomedaserie in americancrime:
            resp = 'CAADAQAD6AkAAuZdXQFef4X---i8NQI'
        elif nomedaserie in americancrimestory:
            resp = 'CAADAQAD6QkAAuZdXQHYDfpMl7LuDwI'
        elif nomedaserie in americangods:
            resp = 'CAADAQADpAsAAuZdXQFl1_dekT6hDwI'
        elif nomedaserie in americanhorrorstory:
            resp = 'CAADAQAD6wkAAuZdXQG5uKKXh4PNRwI'
        elif nomedaserie in americanhousewife:
            resp = 'CAADAQAD-woAAuZdXQHTrmxmJtsFfwI'
        elif nomedaserie in angietribeca:
            resp = 'CAADAQAD_AoAAuZdXQE69ocdunlqgwI'
        elif nomedaserie in animalkingdom:
            resp = 'CAADAQAD7gkAAuZdXQHNK3eF3G0yPwI'
        elif nomedaserie in arrow:
            resp = 'CAADAQAD8woAAuZdXQGqz-Yu1V7oRAI'
        elif nomedaserie in desventuras:
            resp = 'CAADAQAD7wkAAuZdXQHqL3ZpNo8e_gI'
        elif nomedaserie in ashvsevildead:
            resp = 'CAADAQAD_QoAAuZdXQHcnL-7U1wVlgI'
        elif nomedaserie in atlanta:
            resp = 'CAADAQAD8QkAAuZdXQHBmobJsXVqewI'
        elif nomedaserie in atypical:
            resp = 'CAADAQADMgwAAuZdXQHDFSAuNhnsPAI'
        elif nomedaserie in babydaddy:
            resp = 'CAADAQADqQsAAuZdXQGZNVBOCjuFlgI'
        elif nomedaserie in ballers:
            resp = 'CAADAQAD8gkAAuZdXQG0h9dLoBdMpQI'
        elif nomedaserie in banshee:
            resp = 'CAADAQAD8wkAAuZdXQE6gJ5Yc020ygI'
        elif nomedaserie in baskets:
            resp = 'CAADAQAD9AkAAuZdXQGWouUD-hwqrwI'
        elif nomedaserie in bettercallsaul:
            resp = 'CAADAQAD9gkAAuZdXQELmKwfo1KZ3gI'
        elif nomedaserie in betterthings:
            resp = 'CAADAQAD9wkAAuZdXQGldCYKHx10KAI'
        elif nomedaserie in bbus:
            resp = 'CAADAQAD9gsAAuZdXQHd5hkDZDR6vAI'	
        elif nomedaserie in bll:
            resp = 'CAADAQAD-AkAAuZdXQHJSnhWxOd5LwI'	
        elif nomedaserie in biglove:
            resp = 'CAADAQAD-goAAuZdXQFP9iCMmk8SYgI'	
        elif nomedaserie in blackish:
            resp = 'CAADAQADOwsAAuZdXQGur6Qz2dU1EgI'	
        elif nomedaserie in blackmirror:
            resp = 'CAADAQAD-QoAAuZdXQEQeQQVDjrtNAI'	
        elif nomedaserie in blacksails:
            resp = 'CAADAQAD-gkAAuZdXQHMK2yuCn9icwI'	
        elif nomedaserie in blindspot:
            resp = 'CAADAQAD-wkAAuZdXQGZTbsik0eoWQI'	
        elif nomedaserie in bloodline:
            resp = 'CAADAQAD_AkAAuZdXQFg3JFcMpUTRAI'	
        elif nomedaserie in blooddrive:
            resp = 'CAADAQAD6AsAAuZdXQGX7hVvma5dXwI'	
        elif nomedaserie in broadcity:
            resp = 'CAADAQADPAsAAuZdXQGo8y_zojwOcAI'	
        elif nomedaserie in bninenine:
            resp = 'CAADAQAD_wkAAuZdXQFR3-68drdQdgI'	
        elif nomedaserie in bull:
            resp = 'CAADAQADqgsAAuZdXQGYM7ytYVi2XwI'	
        elif nomedaserie in casual:
            resp = 'CAADAQAECgAC5l1dAaoQGW8BHWsvAg'	
        elif nomedaserie in catastrophe:
            resp = 'CAADAQADqwsAAuZdXQFE4Xo61-FIpwI'	
        elif nomedaserie in chefstable:
            resp = 'CAADAQADAQoAAuZdXQE8fYtoqfjTggI'	
        elif nomedaserie in chewinggum:
            resp = 'CAADAQADFAwAAuZdXQG-Y8YZtftjxQI'	
        elif nomedaserie in chicagofire:
            resp = 'CAADAQADAgoAAuZdXQGuTCw32bLxRAI'	
        elif nomedaserie in seriecadastradas:
            resp = 'link do sticker'	
        elif nomedaserie in seriecadastradas:
            resp = 'link do sticker'	
        elif nomedaserie in narcos:
            resp = 'CAADAQADRQoAAuZdXQGWXScs1RuLMAI'
        else:
            resp = 'não entendi'
        telegram.sendSticker(chatID,resp)
      
telegram.message_loop(recebendoMsg)

while True:
    pass

