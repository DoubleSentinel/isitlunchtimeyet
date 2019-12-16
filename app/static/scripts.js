
const updateTime = async () => {
    const response = await fetch("/api/"+verb);
    const json = await response.json();

    if(json.status != 'ok') {
        document.getElementById('main').innerHMTML = 'Maybe. :(';
    } else {
        document.getElementById('main').innerHTML = json.time;
        document.getElementById('second').innerHTML = json.flavorMessage;
    }
}

window.onload = async () => {
    updateTime();
    setInterval(updateTime, 5000);
}

