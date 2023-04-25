// Team Euliss Spikes :: Jeff Chen, Aahan Mehta
//SoftDev pd8
//K31 -- canvas based JS animation
//2023-04-25

var c = document.getElementById("playground");

var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "black";

var requestID;

var clear = (e) => {
    ctx.clearRect(0, 0, 500, 500);
};

var radius = 0;
var growing = true;

var drawDot = () => {
    clear();
    
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, Math.PI*2, true);
    ctx.fill();
    ctx.closePath();
    
    if (growing && radius > 250) {
        growing = false;
    } else if (growing ==false && radius < 1) {
        growing = true;
    }

    if (growing) {
        radius++; 
    } else {
        radius--;
    }

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}

var stopIt = () => {
    window.cancelAnimationFrame(requestID)
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);