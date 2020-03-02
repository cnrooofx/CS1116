let canvas;
let context;
let width;
let height;

let balls = [];
let radius = 30;
let gravity = 0.2;
let time = 33; // In Miliseconds

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    canvas.width = (window.innerWidth - 30);
    canvas.height = (window.innerHeight - 30);
    width = canvas.width;
    height = canvas.height;
    radius = (width / 50)
    window.setInterval(draw, time);
}

// Velocity = Displacement / Time
//          =

function draw() {
    if (balls.length < 10) {
        let ball = {
            x : getRandomNumber(radius, (width-radius)),
            y : getRandomNumber(radius, (height-radius)),
            r : (radius + getRandomNumber(0, 15)),
            xChange : getRandomNumber(-10, 10),
            yChange : getRandomNumber(-10, 10),
            mass : 0,
            velocity : 0
        }
        //      mass =        (4/3 pi r^3) volume            * density
        ball['mass'] = ((4/3) * Math.PI * ((ball.r / 100) ** 3) * 270);
        //      velocity = displacement / time  Pixels per milisecond?
        ball['velocity'] = ((Math.sqrt((ball.xChange ** 2) + (ball.yChange ** 2))) / (time));
        balls.push(ball);
    }
    context.clearRect(0, 0, width, height);
    for (let ball of balls) {
        ball.x += ball.xChange;
        ball.y += ball.yChange;
        ball.yChange += gravity;
        for (let ball2 of balls) {
            if (collides(ball, ball2)) {
                // let v_ball = (((ball.velocity * (ball.mass - ball2.mass)) + (2 * ball2.mass * ball2.velocity)) / (ball.mass + ball2.mass));
                // let v_ball2 = (((ball2.velocity * (ball2.mass - ball.mass)) + (2 * ball.mass * ball.velocity)) / (ball.mass + ball2.mass));
                // console.log(v_ball);
                // console.log(v_ball2);
                ball.xChange *= -1;
                ball.yChange = ((ball.yChange * -1) + gravity);
                ball2.xChange *= -1;
                ball2.yChange = ((ball2.yChange * -1) + gravity);
            }
        }
        // if (ball.x <= (2 * ball.radius)) {
        //     ball.xChange = width;
        // } else if (ball.y <= (2 * ball.radius)) {
        //     ball.y = width;
        // }
        edges(ball);
        drawBall(ball);
    }
}

function collides(ball, ball2) {
    let ball_next_x = (ball.x + ball.xChange);
    let ball_next_y = (ball.y + ball.yChange);
    let ball2_next_x = (ball2.x + ball2.xChange);
    let ball2_next_y = (ball2.y + ball2.yChange);
    let distance = Math.sqrt((((ball_next_x - ball2_next_x) ** 2) + ((ball_next_y - ball2_next_y) ** 2)));
    if ((distance < (ball.r + ball2.r)) &&
    ((ball2.xChange !== 0) && (ball2.yChange !== 0)))  {
        return true;
        // ball.xChange = (ball.xChange * -1);
        // ball.yChange = ((ball.yChange + gravity) * -1);
        // ball2.xChange = (ball2.xChange * -1);
        // ball2.yChange = ((ball2.yChange + gravity) * -1);
    }
}

function edges(ball) {
    // Top & Bottom
    if ((((ball.y) - ball.r) < 0) ||
    (((ball.y) + ball.r) > height)) {
        // ball.xChange = (ball.xChange * -1);
        ball.yChange = (ball.yChange * -1);
        if (((ball.y + ball.r + ball.yChange) > height) &&
        ((ball.yChange < -0.1) && (ball.xChange < -0.1))) {
            ball.yChange = 0;
            ball.xChange = 0;
        } else {
            ball.yChange += gravity;
        }
    // Right & Left
    } else if ((((ball.x) + ball.r) > width) ||
    (((ball.x) - ball.r) < 0)) {
        ball.xChange = (ball.xChange * -1);
        ball.yChange += gravity;
        ball.xChange += gravity;
        return true;
    }
}

function drawBall(ball) {
    context.beginPath();
    context.arc(ball.x, ball.y, ball.r, 0, (2 * Math.PI));
    context.fill();
    context.shadowBlur = 10;
    context.shadowColor = 'rgba(153,153,153, 0.8)';
    context.shadowOffsetX = 5;
    context.shadowOffsetY = 2;
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// V2 – V1 = -e (U 2– U1)

// M1 U1 + M2 U2 = M1 V1 + M 2V2
