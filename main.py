from flask import Flask, request, make_response, jsonify
import requests
app = Flask(__name__)

apikey = "YOUR_API_KEY"

def findSubCount(username):
    youtubeapiurl = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+username+"&fields=items/statistics/subscriberCount&key="+apikey
    response = requests.get(youtubeapiurl)
    subs = response.json()['items'][0]['statistics']['subscriberCount']
    return subs

@app.route('/', methods=['POST', 'GET'])
def index():
    input = request.get_json()
    psubs = int(findSubCount("pewdiepie"))
    tsubs = int(findSubCount("tseries"))
    diff = psubs-tsubs
    diffnews = ""
    if(diff<0):
        diffnews = "Pewds is behind T-Series by "+"{:,} subs.".format(diff)
    else:
        diffnews = "Pewds is ahead of T-Series by "+"{:,} subs.".format(diff)
    pewnews = "Hey fellow 9 year old. Pewdiepie has "+"{:,}".format(psubs) +" subscribers right now. "+diffnews+" Brofist."
    output = {'fulfillmentText': pewnews}

    return  make_response(jsonify(output))

if __name__ == '__main__':
    app.run(debug=True)
