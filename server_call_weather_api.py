from config import *
from flask import Flask, render_template, request, redirect

import errno
import os
import sys
import requests
import json

app = Flask(__name__)

@app.route('/checkHello', methods=['GET'])
def checkHello():
    return "Welcome to weather service API"


@app.route('/checkWeather', methods=['POST'])
def checkWeather():
    #INPUT: {'type': '', 'replyToken': '', 'msisdn': '', 'data': {'lat': '101.1', 'long': '96.1'}}

    #OUTPUT BUTTON: {'replyToken': '', msisdn: '', 'outputtype': 'button', 'data': {X}}
    #X: {'title': '', 'desc': '', 'url': '', 'keywords': [{'type': 'URI', 'label': '', 'data': ''}, .. ]}

    #OUTPUT TEXT: {'replyToken': '', msisdn: '', 'outputtype': 'text', 'data': {X}}
    #X: {'text1': '', 'text2': '', 'text3': ''}
    
    #OUTPUT IMAGE: {'replyToken': '', msisdn: '', 'outputtype': 'image', 'data': {X}}
    #X: {'url': ''}
    
    #OUTPUT CAROUSEL: {'replyToken': '', msisdn: '', 'outputtype': 'carousel', 'data': {X}}
    #X: {[ {'title': '', 'desc': '', 'url': '', 'buttons': [{'type': 'URI', 'label': '', 'data': ''}]}, {'title': '', 'desc': '', 'url': '', 'buttons': [{'type': 'URI', 'label': '', 'data': ''}]}, ..  ]}

    #OUTPUT ERROR: {'outputtype': 'error', 'data': 'Lokasi kamu gak bisa aku cek kak, coba lokasi yg lain ya'}
    
    body = request.get_data(as_text=True)
    print "1----->", body

    JSONData = json.loads(body)
    outputtype = JSONData['type']
    replyToken = JSONData['replyToken']
    msisdn = JSONData['msisdn']
    data = JSONData['data']
    for key in data:
        print key, data[key]
        
    payload = (('key', 'ce2c7a07312a4fd6ae945314171411'), ('q', data['lat'] + ',' + data['long']))
    resp = requests.get("https://api.apixu.com/v1/current.json", params=payload)    
    print "2----->", resp.text
    JSONResult = json.loads(resp.text)

    finalPayload = {}
    finalPayload['replyToken'] = replyToken
    finalPayload['msisdn'] = msisdn
                                        
    
    if 'error' in resp.text:
        print "error call api"
        finalPayload['data'] = 'Lokasi kamu gak bisa aku cek kak, coba lokasi yg lain ya'
        finalPayload['outputtype'] = 'error'
    
    else:
        print JSONResult['location']['name'], JSONResult['location']['region'], JSONResult['current']['temp_c'], JSONResult['current']['condition']['text']

        s = {}
        s['title'] = 'Cuaca hari ini di ' + JSONResult['location']['name'] + ' ' + JSONResult['location']['region']
        s['desc'] = 'Hari ini cuaca ' + JSONResult['current']['condition']['text'] + ' dengan suhu rata2 ' + str(JSONResult['current']['temp_c']) + ' C'
        s['url'] = 'https://bloximages.newyork1.vip.townnews.com/northwestgeorgianews.com/content/tncms/assets/v3/editorial/f/5e/f5e0b1b2-e405-11e3-a8fb-001a4bcf6878/5667424c7359a.image.jpg'
        keywords = []
        button = {}
        button['data'] = 'http://www.bmkg.go.id/cuaca/prakiraan-cuaca-indonesia.bmkg?Prov=07&NamaProv=DKI%20Jakarta'
        button['type'] = 'URI'
        button['label'] = 'Visit BMGK'
        keywords.append(button)
        s['keywords'] = keywords
    
        payload = s
        finalPayload['data'] = payload
        finalPayload['outputtype'] = 'button'
        
    print "3---->", finalPayload    
    return json.dumps(finalPayload)


if __name__==  "__main__":
    print "Call Api Gateway is runnng"
    app.run('0.0.0.0', debug=False)
