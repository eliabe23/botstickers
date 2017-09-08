import telepot

telegram = telepot.Bot("262863240:AAHreV8hDp_EYAbbmGpcrPCP8_2VJ6HPJtc")

twobrokegirls = ('2bg', '2 broke girls')
narcos = ('narcos')
shameless = ('shameless', 'shameless us')
sons = ('sons', 'soa', 'sons of anarchy', 'sonsofanarchy')

def recebendoMsg(msg):
    frase = msg['text']
    frase = frase.lower()
    tipoMsg, tipoChat, chatID = telepot.glance(msg)

    if '/play ' in frase:
        nomedaserie = frase[6:]
        if nomedaserie in sons:
            resp = 'playsonsofanarchy'
        elif nomedaserie in shameless:
            resp = 'CAADAgADxAUAAvoLtgiCOopVZ7H8dwI'
        elif nomedaserie in narcos:
            resp = 'CAADAQADRQoAAuZdXQGWXScs1RuLMAI'
        elif nomedaserie in twobrokegirls:
            resp = 'CAADAQADOgsAAuZdXQGb1rpQJ2A4YwI'
        else:
            resp = 'não entendi'
        telegram.sendSticker(chatID,resp)
      
telegram.message_loop(recebendoMsg)

while True:
    pass

