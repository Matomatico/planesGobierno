#!/usr/bin/env python

import cgi,urllib
from google.appengine.api import xmpp
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from d.d import v
from d.l import l
from random import randint
import logging
import time

# response 
response = "Invalid tweet"

# Enums de ejemplo
regiones = { "070000" : "CUSCO", "140000" : "LIMA", "120000" : "LALIBERTAD" }
types = { "s" : "SOLUCION", "m" : "METAS" }
ops = { 
    "153" : "Ayllu",
    "601" : "Tawntinsuyo",
    "2644" : "AlianzaPopular",
    "602" : "PAPA",
    "1257" : "@APP_Peru",
    "2164" : "FIA",
    "1366" : "@KeikoFujimori",
    "2366" : "@KausachunCusco",
    "4" : "@AccionPopularPe",
    "2368" : "Pachakuteq",
    "5" : "SiempreUnidos",
    "1555" : "TyL",
    "445" : "APU",
	
	"1269" : "FuerzaRegional",
	"332" : "CDR",
	"2160" : "FrenteAmplio",
	"22" : "@Solidaridad_PSN",
	"1264" : "Humanista",
	"553" : "PatriaJoven",
	"46" : "@Peru_Posible",
	"181" : "ConfianzaPeru",
	"47" : "UPP",
	"2259" : "JusticiayCapacidad",
	
	"2191" : "DemocraciaDirecta",
	"32" : "@APRAonline",
	"21" : "RestauracionNacional",
	"1920" : "COEE",
	"55" : "PeruPatriaSegura",
	"2258" : "SeguridadyHonradez",
	"2628" : "NuevaLibertad",
	"15" : "@ppcdelperu"
}

def create_mention ( op ) :
    if ( op[:1] == '@' ) :
        return op
    else: return '#' + op

def create_tweet ( to_tweet ) :
    # extraer datos
    region = regiones[to_tweet['u']]
    type = types[to_tweet['t']]
    op = create_mention(ops[to_tweet['o']])
    content = str(unicode(to_tweet['c'], 'ISO-8859-1').encode("ISO-8859-1"))
    link = " http://bit.ly/" + l[to_tweet['u']][to_tweet['o']]
    # esqueleto de tweet
    my_tweet = "#ERM14 #" + region + " " + op + " #LoHara? " + type + " \""  
    # longitud inicial de contenido
    content_len = 140 - len(my_tweet) - len(link)
  
    # modificar la longitud si el contenido es más largo
    if content_len < len(content) :
        # caracteres que sobran. presumo que es por 'http://'
		content_len -= (4 + 1)
        content = to_tweet['c'][:content_len]	
        # si es muy largo agregar '...'
        my_tweet += content + "...\"" + link
    else :
        content_len -= 1
        content = to_tweet['c'][:content_len]
        my_tweet += content + "\"" + link  
    if content_len <= 0 :
        return
    response = str(my_tweet)        
    logging.info("Current tweet is %s", my_tweet )
    return response
  
def generate_tweet():
    n_elements = len(v)
    random_element = v[randint(0, n_elements)]
    return create_tweet(random_element)  

class BotPDG(webapp.RequestHandler):
    def get(self):
        import simplejson as json
        import tweepy
        CONSUMER_KEY ="CONSUMER_KEY"
        CONSUMER_SECRET = "CONSUMER_SECRET"
        ACCESS_KEY = "ACCESS_KEY"
        ACCESS_SECRET = "ACCESS_SECRET"
        auth = tweepy.OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
        auth.set_access_token( ACCESS_KEY, ACCESS_SECRET )
        bot = tweepy.API(auth)
        # create status
        status = generate_tweet()
        bot.update_status(status)
        self.response.out.write("Whoa! Done, finally!")
        

application = webapp.WSGIApplication([('/PATH/TO/BOT', BotPDG)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
