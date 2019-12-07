from flask import Flask, request, render_template
from datetime import datetime, time
import urllib, json, pytz

app = Flask(__name__)

URL_FOR_API = 'http://ip-api.com/json/'

LUNCH_HOURS = { 'start': time(hour=11, minute=30),
                'end': time(hour=13)}

def get_client_ip_location(request):
    if app.debug:
        # client_ip = '144.2.103.184' # Neuchâtel
        client_ip =  '72.229.28.185' # New York
    else:
        client_ip = request.remote_addr
    req = urllib.request.Request(URL_FOR_API + client_ip)
    return json.loads(urllib.request.urlopen(req).read())

@app.route('/', methods=['GET'])
def web():
    client_timezone = get_client_ip_location(request)['timezone']
    client_time_now = datetime.now(pytz.timezone(client_timezone)).time()
    its_lunchtime = LUNCH_HOURS['start'] <= client_time_now < LUNCH_HOURS['end']
    return render_template('template.html',
                            its_lunchtime=its_lunchtime)

@app.route('/api')
def api():
    return
