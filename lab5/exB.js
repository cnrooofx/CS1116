let canvas;
let context;
let width;
let height;

let balls = [];
let radius;
let e = 0.8; // Coefficient of restitution
let gravity = 0.2;
let time = 33;
let threshold;
let gradient;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width = (window.innerWidth - 30);
    height = canvas.height = (window.innerHeight - 30);
    radius = (width / 40);
    threshold = (radius * 2)
    window.setInterval(draw, time);
}

function draw() {
    if (balls.length < 10) {
        let ball = {
            x : getRandomNumber(radius+15, (width-radius+15)),
            y : getRandomNumber(radius+15, (height-radius+15)),
            r : (radius + getRandomNumber(0, 15)),
            velocityX : getRandomNumber(-5, 5),
            velocityY : getRandomNumber(-5, 5),
            colour : 'rgb('+getRandomNumber(0, 255)+','+getRandomNumber(0, 255)+','+getRandomNumber(0, 255)+')',
            mass : 0,
            collided : false,
        }
        ball.mass = ball.r ** 2;
        if (ball.velocityX === 0) {
            ball.velocityX++;
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
        edges(ball);
        for (let ball2 of balls) {
            if (near(ball, ball2)) {
                console.log('collided')
                collides(ball, ball2);
            }
            let distance = Math.sqrt((((ball.x - ball2.x) ** 2) + ((ball.y - ball2.y) ** 2)));
            if (distance < threshold) {
                context.beginPath();
                context.lineWidth = (1 / distance);
                context.moveTo(ball.x, ball.y);
                context.lineTo(ball2.x, ball2.y);
                context.stroke();
            }
        }
    }
}

function near(ball, ball2) {
    if ((ball.x - ball.r < ball2.x + ball2.r) &&
    (ball.x + ball.r > ball2.x - ball2.r) &&
    (ball.y - ball.r < ball2.y + ball2.r) &&
    (ball.y + ball.r > ball2.y - ball2.r) &&
    (! ball.collided) && (! ball2.collided)) {
        console.log('true');
        return true;
    } else {
        ball.collided = false;
        ball2.collided = false;
        console.log('false');
        return false;
    }
}

function collides(ball, ball2) {
    let distance = Math.sqrt((((ball.x - ball2.x) ** 2) + ((ball.y - ball2.y) ** 2)));
    if (distance <= (ball.r + ball2.r))  {
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
        ball.colour = ball2.colour
        ball.collided = true;
        ball2.collided = true;
        console.log(ball.collided)
        console.log(ball2.collided)
    }
}

function edges(ball) {
    // Top & Bottom
    if ((ball.y - ball.r <= 0 && ball.velocityY < 0) ||
    (ball.y + ball.r >= height && ball.velocityY > 0)) {
        ball.velocityY *= -1;
        changeColour(ball);
    // Right & Left
  } else if (((ball.x + ball.r >= width) && ball.velocityX > 0) ||
    ((ball.x - ball.r <= 0) && ball.velocityX < 0)) {
        ball.velocityX *= -1;
        changeColour(ball);
    }
}

function drawBall(ball) {
    context.strokeStyle = '#000';
    context.lineWidth = 0.5;
    context.beginPath();
    context.arc(ball.x, ball.y, ball.r, 0, (2 * Math.PI));
    gradient = context.createRadialGradient((ball.x - 0.5 * ball.r), (ball.y - 0.5 * ball.r), (ball.r / 2), ball.x, ball.y, ball.r);
    gradient.addColorStop(1, ball.colour);
    gradient.addColorStop(0.8, '#019F62');
    gradient.addColorStop(0, 'rgba(1, 159, 98, 0)');
    context.fillStyle = gradient;
    context.fill();
    context.shadowBlur = 10;
    context.shadowColor = 'rgba(153,153,153, 0.8)';
    context.shadowOffsetX = 5;
    context.shadowOffsetY = 2;
}

function occupied(ball) {
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
