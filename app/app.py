from flask import Flask, request, render_template, jsonify
from datetime import datetime, time
from requests import get as http_get
import pytz

app = Flask(__name__)

URL_FOR_API = 'http://ip-api.com/json/'

LUNCH_HOURS = {
    'start': time(hour=11, minute=30),
    'end': time(hour=13)
}


def get_client_ip_location(request):
    if app.debug:
        # client_ip = '144.2.103.184' # Neuchâtel
        client_ip = '72.229.28.185'  # New York
    else:
        client_ip = request.remote_addr
    response = http_get(URL_FOR_API + client_ip)
    return response.json()


def is_lunchtime(request):
    try:
        client_info = get_client_ip_location(request)
        client_timezone = client_info['timezone']
        client_time_now = datetime.now(pytz.timezone(client_timezone)).time()
        return LUNCH_HOURS['start'] <= client_time_now < LUNCH_HOURS['end']
    except KeyError:
        raise BaseException("Could not find timezone from IP", client_info['message'])


@app.route('/', methods=['GET'])
def web():
    return render_template('index.html')


@app.route('/api')
def api():
    return 'to implement'

@app.route('/api/lunch')
def api_lunch():
    try:
        return jsonify(
            status='ok',
            lunchtime='yes' if is_lunchtime(request) else 'no',
            flavorMessage='not implemented'
        )
    except BaseException as e:
        return jsonify(
            status='error',
            errorMessage=str(e),
        )
