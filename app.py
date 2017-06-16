#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "test_mistro":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    action_t = parameters.get("action")
    commodity=parameters.get("commodity")
    number=parameters.get("number")
    price=parameters.get("price")
    date_per=parameters.get("date-period")
    
    commodity_url={'Wheat': 'https://server.askmistro.com/picture?file=5GXV5VBCL1HVINDYMLTQJCXY1TJUH8Y8.jpg&name=Token',
                    'Gold':'https://server.askmistro.com/picture?file=E3YK1WJGGBEP2U8UPLGMGJDXTQEV7IYB.jpg&name=Token', 
                    'WTI':'https://server.askmistro.com/picture?file=VG6S9YG7QUP6I8YH48P0L3CE3V4XGOX6.jpg&name=Token',
                    'Sugar':'https://server.askmistro.com/picture?file=7PG8I73GQ677736LKX9T945GELG55KE0.jpg&name=Token',
                    'Soybeans':'https://server.askmistro.com/picture?file=QXVBNVJOWCDHOH5IVIDMLGRNQ06SGMGA.jpg&name=Token',
                    'Coffee':'https://server.askmistro.com/picture?file=EV9GCSBX0QOLJ146GOJZ7AEPFO63YYKR.jpg&name=Token',
                    'Corn':'https://server.askmistro.com/picture?file=O3RECAHF8COYP5WQ8E54MH32FRFQZQA8.jpg&name=Token',
                    'Cocoa':'https://server.askmistro.com/picture?file=ECETA1JI1303VD3LABM53CR8DWEXCC85.jpg&name=Token',
                    'Brent':'https://server.askmistro.com/picture?file=VG6S9YG7QUP6I8YH48P0L3CE3V4XGOX6.jpg&name=Token',
                    'Nature gas':'https://server.askmistro.com/picture?file=B7VG8YVS5VEMK4BYVIOIRF7THRTGPFV4.jpg&name=Token',
                    'Copper':'https://server.askmistro.com/picture?file=T6BRK5SY9XGYI6P2F53999MYCX9AWIF4.jpg&name=Token',
                    'Lead': 'https://server.askmistro.com/picture?file=LG7GOI35WV6FAF8M8TVVHTBKCESMDE6Q.jpg&name=Token',
                    'Zinc':'https://server.askmistro.com/picture?file=78U8ECHWG4UIRLC38PMJTPNLH5Y1AN3K.jpg&name=Token',
                    'Silver':'https://server.askmistro.com/picture?file=3HA86TAIDG1I4UQLIGXD7BWPDBQG99CQ.jpg&name=Token' 
                    }

    commodity_list=""
    price_list=""
    number_list=""
    date_per_list=""

    for i in xrange(len(commodity)):
        commodity_list+=str(commodity[i])+" "
    for i in xrange(len(price)):
        price_list+="$"+str(price[i])+" "
    for i in xrange(len(number)):
        number_list+=str(number[i])+" "
    for i in xrange(len(date_per)):
        date_per_list+=str(date_per[i])+" "
    
    speech = "Are you sure you want to " + str(action_t)+" "+number_list+commodity_list+"at"+price_list+"for "+date_per_list +"contract."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        "data": commodity_url[commodity[0]],
        #"data": {},
        # "contextOut": [],
        "source": "apiai-testmistro"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')

