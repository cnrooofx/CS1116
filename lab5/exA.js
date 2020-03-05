let canvas;
let context;
let width;
let height;

let threshold = 50;
let points = [];

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width;
    height = canvas.height;
    window.setInterval(draw, 33);
}

function draw() {
    let q = {
        x : getRandomNumber(0, 500),
        y : getRandomNumber(0, 500)
    }
    for (let p of points) {
      let distance = Math.sqrt((((q.x - p.x) ** 2) + ((q.y - p.y) ** 2)))
        if (distance < threshold) {
            context.beginPath();
            context.lineWidth = (1 / distance);
            context.moveTo(q.x, q.y);
            context.lineTo(p.x, p.y);
            context.stroke();
        }
    }
    points.push(q);
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
