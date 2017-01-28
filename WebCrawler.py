# -*- coding: latin-1 -*-

import tweepy
import csv
import time

consumer_keys = "ibASLuTtzeozJYpIuG1eGldji"
consumer_secret = "69xvPCMwGHM8tt4j1LizgTxDDMXZ0dmTklRuMh8fF8uwUqY6Gg"
access_token = "823938970035908609-CZ00qIXvJUWspC39mNh3upSlDBCzExV"
access_token_secret = "nXO1u6bHoGt38Tp7n9Z0o1Vt2DEAqDovoqJuWwLdp9vaS"

auth = tweepy.OAuthHandler(consumer_keys, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

arq  = csv.writer(open("base_teste.csv", "w"))
arq2 = open("base_teste_json.json", "w") #trata como texto

row=[]

#coleta os dadose navega nessas informacoes com item()
statuses = tweepy.Cursor(api.search, q='#trump', since='2017-01-22', until='2017-01-23',lang='en').items()

while True:
    try:
        #le os tweets
        status = statuses.next()        
        #captura alguns parametros
        row=[str(status.user.screen_name), str(status.created_at), status.text.encode('utf-8'), status.geo]
        #escreve o CSV
##        print(row)
        arq.writerow(row)
        #escreve o JSON
        arq2.write(str(status))
        arq2.write("\n")
        
##        exit()
                
    except tweepy.TweepError: #erro do twitter, limite de dados
        print("wait 15 minutes...")
        time.sleep(60*15)
        continue
    
    except StopIteration: #acabaram os tweets
        print("Acabou")
        break
