# Simple Weather Service API gateway using APIXU

# Step
- Create dialog using BJtech platform
- Add call api component
- Fill in URL of simple weather service api
- Run this program

# JSON Request 
- BJtech platform will send this JSON to your api gateway
- For example your chatbot send Latitude and Longitude to get weather of specific location:

  {'type': '?', 'replyToken': '?', 'msisdn': '?', 'data': {'lat': '101.1', 'long': '96.1'}}

# JSON Response

- Your api gateway must be response with following JSON:
  
  1. Response BUTTON: 
     {'replyToken': '', msisdn: '', 'outputtype': 'button', 'data': {X}} <br/>
     X: {'title': '', 'desc': '', 'url': '', 'keywords': [{'type': 'URI', 'label': '', 'data': ''}, .. ]}

  2. Response TEXT: 
     {'replyToken': '', msisdn: '', 'outputtype': 'text', 'data': {X}} <br/>
     X: {'text1': '?', 'text2': '?', 'text3': '?'}

  4. Response IMAGE: {'replyToken': '', msisdn: '', 'outputtype': 'image', 'data': {X}} <br/>
     X: {'url': ''}

  5. Response CAROUSEL: {'replyToken': '', msisdn: '', 'outputtype': 'carousel', 'data': {X}} <br/>
     X: {[ {'title': '', 'desc': '', 'url': '', 'buttons': [{'type': 'URI', 'label': '', 'data': ''}]}, {'title': '', 'desc': '', 'url': '', 'buttons': [{'type': 'URI', 'label': '', 'data': ''}]}, ..  ]}

  6. Response ERROR: {'outputtype': 'error', 'data': 'Lokasi kamu gak bisa aku cek kak, coba lokasi yg lain ya'}

- You must send back replyToken and msisdn value generated by bot platform, otherwise call api will be rejected