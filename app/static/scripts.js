
const updateLunchtime = async () => {
    const response = await fetch("/api/lunch");
    const json = await response.json();

    if(json.status != 'ok') {
        document.getElementBy('main').innerHMTML = 'Maybe. :(';
    } else {
        document.getElementById('main').innerHTML = json.lunchtime.toUpperCase();
        document.getElementById('second').innerHTML = json.flavorMessage;
    }
}

window.onload = async () => {
    updateLunchtime();
    setInterval(updateLunchtime, 5000);
}

