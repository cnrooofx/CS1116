let canvas;
let context;
let width;
let height;

let balls = [];
let radius = 30;
let gravity = 0.2;
let time = 20;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width = (window.innerWidth - 30);
    height = canvas.height = (window.innerHeight - 30);
    radius = (width / 50)
    window.setInterval(draw, time);
}

// Velocity = Displacement / Time
//          =

function draw() {
    if (balls.length < 10) {
        let ball = {
            x : getRandomNumber(radius+15, (width-radius+15)),
            y : getRandomNumber(radius+15, (height-radius+15)),
            r : (radius + getRandomNumber(0, 15)),
            xChange : getRandomNumber(-10, 10),
            yChange : getRandomNumber(-10, 10),
            colour : 'rgb('+getRandomNumber(0, 255)+','+getRandomNumber(0, 255)+','+getRandomNumber(0, 255)+')',
            mass : 0,
            // velocity : 0
        }
        ball.mass = (Math.PI * (ball.r ** 2));
        //      velocity = displacement / time  Pixels per milisecond?
        // ball.velocity = ((Math.sqrt((ball.xChange ** 2) + (ball.yChange ** 2))) / (time));
        balls.push(ball);
    }
    context.clearRect(0, 0, width, height);
    for (let ball of balls) {
        ball.x += ball.xChange;
        ball.y += ball.yChange;
        ball.yChange += gravity;
        drawBall(ball);
        for (let ball2 of balls) {
            if (near(ball, ball2)) {
                collides(ball, ball2)
                // let v_ball = (((ball.velocity * (ball.mass - ball2.mass)) + (2 * ball2.mass * ball2.velocity)) / (ball.mass + ball2.mass));
                // let v_ball2 = (((ball2.velocity * (ball2.mass - ball.mass)) + (2 * ball.mass * ball.velocity)) / (ball.mass + ball2.mass));
                // console.log(v_ball);
                // console.log(v_ball2);
            }
        }
        edges(ball);
    }
}

function near(ball, ball2) {
    let radii = ball.r + ball2.r
    if ((ball.x + radii > ball2.x) &&
    (ball.x < radii + ball2.x) &&
    (ball.y + radii > ball2.y) &&
    (ball.y < radii + ball2.y)) {
        return true;
    }
}

function collides(ball, ball2) {
    let ball_next_x = (ball.x + ball.xChange);
    let ball_next_y = (ball.y + ball.yChange);
    let ball2_next_x = (ball2.x + ball2.xChange);
    let ball2_next_y = (ball2.y + ball2.yChange);
    let distance = Math.sqrt((((ball_next_x - ball2_next_x) ** 2) + ((ball_next_y - ball2_next_y) ** 2)));
    if ((distance <= (ball.r + ball2.r)) &&
    ((ball2.xChange !== 0) && (ball2.yChange !== 0)))  {
        ball.xChange *= -1;
        ball.yChange = ((ball.yChange * -1) + gravity);
        ball2.xChange *= -1;
        ball2.yChange = ((ball2.yChange * -1) + gravity);
    }
}

function edges(ball) {
    // Top & Bottom
    if (((((ball.y) - ball.r) < 0) && ball.yChange < 0) ||
    ((((ball.y) + ball.r) > height) && ball.yChange > 0)) {
        ball.yChange *= -1;
        ball.yChange += gravity;
    // Right & Left
  } else if (((((ball.x) + ball.r) > width) && ball.xChange > 0) ||
    ((((ball.x) - ball.r) < 0) && ball.xChange < 0)) {
        ball.xChange = (ball.xChange * -1);
        ball.yChange += gravity;
        ball.xChange += gravity;
        return true;
    }
}

function drawBall(ball) {
    context.fillStyle = ball.colour;
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
