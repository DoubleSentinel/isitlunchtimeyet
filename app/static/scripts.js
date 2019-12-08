
const updateLunchtime = async () => {
    const response = await fetch("/api/lunch");
    const json = await response.json();

    if(json.status != 'ok') {
        document.getElementBy('main').innerHMTML = 'Maybe. :(';
    } else {
        document.getElementById('main').innerHTML = json.lunchtime.toUpperCase();
    }
}

window.onload = async () => {
    updateLunchtime();
    setInterval(updateLunchtime, 5000);
}

