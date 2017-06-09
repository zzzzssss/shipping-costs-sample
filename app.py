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

    cost = {'sell':100, 'buy':200}
    speech = "You succeed " + str(action_t) + str(number)+str(commodity[0])+"at"+str(price)+str(date_per[0]) +"contract"+"with db code"+str(cost[action_t])

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-testmistro-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
