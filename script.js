let timer;
let seconds = 0;

function startTimer() {
    if (!timer) {
        timer = setInterval(() => {
            seconds++;
            document.getElementById("timer").innerText = new Date(seconds * 1000).toISOString().substr(11, 8);
        }, 1000);
    }
}

function stopTimer() {
    clearInterval(timer);
    timer = null;
}

function resetTimer() {
    stopTimer();
    seconds = 0;
    document.getElementById("timer").innerText = "00:00:00";
}
