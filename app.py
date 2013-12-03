from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route('/rns/<int:rns_id>/<int:max_ann>', methods = ['GET'])
def get_rns(rns_id, max_ann):
    r = requests.get('http://www.londonstockexchange.com/exchange/area-news/news/afx/xmlrequest.html?announcementId=%d&maxAnn=%d' % (rns_id, max_ann))
    return r.text

if __name__ == '__main__':
    app.run(debug = True)