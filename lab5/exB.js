let canvas;
let context;
let width;
let height;

let balls = [];
let radius;
let e = 0.8; // Coefficient of restitution
let gravity = 0.2;
let time = 33;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width = (window.innerWidth - 30);
    height = canvas.height = (window.innerHeight - 30);
    radius = (width / 40);
    window.setInterval(draw, time);
}

function draw() {
    if (balls.length < 10) {
        let ball = {
            x : getRandomNumber(radius+15, (width-radius+15)),
            y : getRandomNumber(radius+15, (height-radius+15)),
            r : (radius + getRandomNumber(0, 15)),
            velocityX : getRandomNumber(-10, 10),
            velocityY : getRandomNumber(-5, 5),
            colour : 'rgb('+getRandomNumber(0, 255)+','+getRandomNumber(0, 255)+','+getRandomNumber(0, 255)+')',
            mass : 0,
            collided : false,
        }
        ball.mass = ball.r ** 2;
        if (velocityX === 0) {
            velocityX++
        }
        while (occupied(ball)) {
            ball.x = getRandomNumber(radius+15, (width-radius+15));
            ball.y = getRandomNumber(radius+15, (width-radius+15));
        }
        balls.push(ball);
    }
    context.clearRect(0, 0, width, height);
    for (let ball of balls) {
        ball.x += ball.velocityX;
        ball.y += ball.velocityY;
        ball.velocityY += gravity;
        drawBall(ball);
        for (let ball2 of balls) {
            if (near(ball, ball2)) {
                collides(ball, ball2);
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
    (ball.y < radii + ball2.y) &&
    ((! ball.collided) && (! ball2.collided))) {
        return true;
    } else {
        ball.collided = false;
    }
}

function collides(ball, ball2) {
    let ball_next_x = (ball.x + ball.velocityX);
    let ball_next_y = (ball.y + ball.velocityY);
    let ball2_next_x = (ball2.x + ball2.velocityX);
    let ball2_next_y = (ball2.y + ball2.velocityY);
    let distance = Math.sqrt((((ball_next_x - ball2_next_x) ** 2) + ((ball_next_y - ball2_next_y) ** 2)));
    if ((distance <= (ball.r + ball2.r)) &&
    ((ball2.velocityX !== 0) && (ball2.velocityY !== 0)))  {
        // let collisionX = ((ball.x * ball2.r) + (ball2.x * ball.r)) / (ball.r + ball2.r);
        // let collisionY = ((ball.y * ball2.r) + (ball2.y * ball.r)) / (ball.r + ball2.r);
        let newVelocityX = ((ball.velocityX * e) * (ball.mass - ball2.mass) +
          (2 * ball2.mass * ball2.velocityX)) / (ball.mass + ball2.mass);
        let newVelocityY = ((ball.velocityY * e) * (ball.mass - ball2.mass) +
          (2 * ball2.mass * ball2.velocityY)) / (ball.mass + ball2.mass);
        let newVelocityX2 = ((ball2.velocityX * e) * (ball2.mass - ball.mass) +
          (2 * ball.mass * ball.velocityX)) / (ball.mass + ball2.mass);
        let newVelocityY2 = ((ball2.velocityY * e) * (ball2.mass - ball.mass) +
          (2 * ball.mass * ball.velocityY)) / (ball.mass + ball2.mass);
        ball.velocityX = newVelocityX;
        ball.velocityY = newVelocityY;
        ball2.velocityX = newVelocityX2;
        ball2.velocityY = newVelocityY2;
        ball2.colour = ball.colour
        ball.collided = true;
        ball2.collided = true;
    }
}

function edges(ball) {
    // Top & Bottom
    if (((((ball.y) - ball.r) < 0) && ball.velocityY < 0) ||
    ((((ball.y) + ball.r) > height) && ball.velocityY > 0)) {
        ball.velocityY *= -1;
        changeColour(ball);
    // Right & Left
    } else if (((((ball.x) + ball.r) > width) && ball.velocityX > 0) ||
    ((((ball.x) - ball.r) < 0) && ball.velocityX < 0)) {
        ball.velocityX *= -1;
        changeColour(ball);
    }
}

function drawBall(ball) {
    context.strokeStyle = '#000';
    context.lineWidth = 0.5;
    context.beginPath();
    context.arc(ball.x, ball.y, ball.r, 0, (2 * Math.PI));
    context.fillStyle = ball.colour;
    context.fill();
    context.shadowBlur = 10;
    context.shadowColor = 'rgba(153,153,153, 0.8)';
    context.shadowOffsetX = 5;
    context.shadowOffsetY = 2;
}

function occupied(ball) {
    // Top Left x - r  y - r
    // Top Right x + r  y - r
    // Bottom Left x - r  y + r
    // Bottom Right x + r  y + r
    for (let otherball of balls) {
        let boxSize = (ball.r + otherball.r);
        if ((ball.x < otherball.x + boxSize) &&
        (ball.x > otherball.x - boxSize) &&
        (ball.y < otherball.y + boxSize) &&
        (ball.y > otherball.y - boxSize)) {
            // New ball x too close to another ball
            return true;
        }
    }
    return false;
}

function changeColour(ball) {
    ball.colour = 'rgb('+getRandomNumber(0, 255)+','+getRandomNumber(0, 255)+','+getRandomNumber(0, 255)+')';
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
