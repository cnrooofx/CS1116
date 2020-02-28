let canvas;
let context;
let width;
let height;

let balls = [];
let radius = 30;
let gravity = 0.1;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width;
    height = canvas.height;
    window.setInterval(draw, 33);
}

function draw() {
    if (balls.length < 10) {
        let ball = {
            x : getRandomNumber(radius, (width-radius)),
            y : getRandomNumber(radius, (height-radius)),
            r : (radius + getRandomNumber(-10, 10)),
            xChange : getRandomNumber(-10, 10),
            yChange : getRandomNumber(-10, 10)
        };
        balls.push(ball);
    }
    context.clearRect(0, 0, width, height);
    for (let ball of balls) {
        context.beginPath();
        context.arc(ball.x, ball.y, ball.r, 0, (2 * Math.PI))
        context.fill()
        // if (edges(ball)) {
        // }
        edges(ball)
        ball.x = ball.x + ball.xChange;
        ball.y = ball.y + ball.yChange;
        ball.yChange = ball.yChange + gravity;
        for (let ball2 of balls) {
            collides(ball, ball2);
        }
        // if (ball.x <= (2 * ball.radius)) {
        //     ball.xChange = width;
        // } else if (ball.y <= (2 * ball.radius)) {
        //     ball.y = width;
        // }
    }
}

function collides(ball, ball2) {
    let distance = Math.sqrt((((ball.x - ball2.x) ** 2) + ((ball.y - ball2.y) ** 2)));
    if (distance < (ball.r + ball2.r)) {
        ball.xChange = (ball.xChange * -1);
        ball.yChange = ((ball.yChange + gravity) * -1);
        ball2.xChange = (ball2.xChange * -1);
        ball2.yChange = ((ball2.yChange + gravity) * -1);
    }
}
 function edges(ball) {
    if (((ball.y + ball.yChange) - radius) < 0) {
        ball.xChange = (ball.xChange * -1);
        ball.yChange = (ball.yChange * -1);
    } else if (((ball.y + ball.yChange) + radius) > height) {
        // ball.xChange = (ball.xChange * -1);
        ball.yChange = (ball.yChange * -1);
        return true;
    } else if ((((ball.x + ball.xChange) + radius) > width) ||
        ((ball.x + ball.xChange) - radius) < 0) {
        ball.xChange = (ball.xChange * -1);
        ball.yChange = (ball.yChange * -1);
        return true;
    }
 }

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// V2 – V1 = -e (U 2– U1)

// M1 U1 + M2 U2 = M1 V1 + M 2V2
