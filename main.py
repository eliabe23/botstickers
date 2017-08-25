import telepot

telegram = telepot.Bot("262863240:AAHreV8hDp_EYAbbmGpcrPCP8_2VJ6HPJtc")

sons = ('play sons', 'play soa', 'play sons of anarchy', 'play sonsofanarchy')
shameless = ('play shameless', 'play shameless us')
def recebendoMsg(msg):
    frase = msg['text']
    frase = frase.lower()
    tipoMsg, tipoChat, chatID = telepot.glance(msg)

    if frase in sons:
        resp = 'CAADAQAD3goAAuZdXQE8WyJzDTSomAI'
    if frase in shameless:
        resp = 'CAADAQADZgoAAuZdXQG-CK4aW3AfOQI'
    
    telegram.sendSticker(chatID,resp)

telegram.message_loop(recebendoMsg)

while True:
    pass

