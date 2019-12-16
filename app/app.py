from flask import Flask, request, render_template, jsonify, redirect, url_for
from datetime import datetime, time
from requests import get as http_get
import pytz

from verbs import VERBS

app = Flask(__name__)

URL_FOR_API = 'http://ip-api.com/json/'


class IpApiError(BaseException):
    pass


def get_client_ip_location(request):
    if app.debug:
        # client_ip = '144.2.103.184' # Neuchâtel
        client_ip = '72.229.28.185'  # New York
    else:
        client_ip = request.remote_addr
    response = http_get(URL_FOR_API + client_ip)
    return response.json()


def check_time_for_verb(verb, time):
    for time_frame in VERBS[verb]:
        frame_start = datetime.strptime(time_frame['start'], "%H:%M:%S")
        frame_end = datetime.strptime(time_frame['end'], "%H:%M:%S")

        if frame_start.time() <= time < frame_end.time():
            return time_frame['is_it_time'], time_frame['flavor']

    return "NO", "It's most definitely, probably not the time"


def is_requested_time(verb, hour, minute):
    return check_time_for_verb(verb, time(hour=hour, minute=minute))


def is_client_time(request, verb):
    try:
        client_info = get_client_ip_location(request)
        client_timezone = client_info['timezone']
        client_time_now = datetime.now(pytz.timezone(client_timezone)).time()
    except KeyError:
        raise IpApiError("Could not find timezone from IP", client_info['message'])

    return check_time_for_verb(verb, client_time_now)


@app.route('/', methods=['GET'])
def web():
    return redirect(url_for('is_it_time_to', verb=VERBS['lunch']))


@app.route('/api/<string:verb>/<int:hour>/<int:minute>')
def api_verb_request(verb, hour, minute):
    try:
        response, flavor = is_requested_time(verb, hour, minute)
        return jsonify(
            status='ok',
            time=response,
            flavorMessage=flavor,
        )
    except BaseException as e:
        return jsonify(
            status='error',
            errorMessage=str(e),
        )


@app.route('/api/<string:verb>')
def api_verb(verb):
    try:
        response, flavor = is_client_time(request, verb)
        return jsonify(
            status='ok',
            time=response,
            flavorMessage=flavor,
        )
    except BaseException as e:
        return jsonify(
            status='error',
            errorMessage=str(e),
        )


@app.route('/<string:verb>')
def is_it_time_to(verb):
    return render_template('index.html', verb=verb)
