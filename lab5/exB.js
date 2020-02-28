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
            // xChange : getRandomNumber(-10, 10),
            // yChange : getRandomNumber(-10, 10)
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
        // for (let ball2 of balls) {
        //     if (collides(ball, ball2)) {
        //         ball.xChange = (ball.xChange * -1);
        //         ball.yChange = ((ball.yChange + gravity) * -1);
        //         ball2.xChange = (ball2.xChange * -1);
        //         ball2.yChange = ((ball2.yChange + gravity) * -1);
        //     } else {
                ball.x = ball.x + ball.xChange;
                ball.y = ball.y + ball.yChange;
                ball.yChange = ball.yChange + gravity;
            // }
        // }
        // if (ball.x <= (2 * ball.radius)) {
        //     ball.xChange = width;
        // } else if (ball.y <= (2 * ball.radius)) {
        //     ball.y = width;
        // }
    }
}

function collides(ball, ball2) {
    let ball_next_x
    let ball_next_y
    let ball2_next_x
    let ball2_next_y
    let distance = Math.sqrt(((((ball.x + ball.xChange) - (ball2.x + ball2.xChange)) ** 2) + (((ball.y + ball.yChange) - (ball2.y + ball2.yChange)) ** 2)));
    if (distance < (ball.r + ball2.r)) {
        return true;
        // ball.xChange = (ball.xChange * -1);
        // ball.yChange = ((ball.yChange + gravity) * -1);
        // ball2.xChange = (ball2.xChange * -1);
        // ball2.yChange = ((ball2.yChange + gravity) * -1);
    }
}
 function edges(ball) {
    // Top
    if (((ball.y + ball.yChange) - radius) < 0) {
        ball.xChange = (ball.xChange * -1);
        ball.yChange = (ball.yChange * -1);
    // Bottom
    } else if (((ball.y + ball.yChange) + radius) > height) {
        // ball.xChange = (ball.xChange * -1);
        ball.yChange = (ball.yChange * -1);
        return true;
    // Right
    } else if (((ball.x + ball.xChange) + radius) > width) {
        ball.xChange = (ball.xChange * -1);
        ball.yChange = (ball.yChange * -1);
        return true;
    // Left
    } else if (((ball.x + ball.xChange) - radius) < 0) {
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
