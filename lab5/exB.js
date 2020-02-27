let canvas;
let context;
let width;
let height;

let balls = [];
let radius = 30;
let gravity = 0.9;

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
      ball.x = ball.x + ball.xChange;
      ball.y = ball.y + ball.yChange + gravity;
      // for (let ball2 of balls) {
      //
      // }
      // if (ball.x <= (2 * ball.radius)) {
      //     ball.xChange = width;
      // } else if (ball.y <= (2 * ball.radius)) {
      //     ball.y = width;
      // }
  }
}

// function collides(ball, ball2) {
//     let distance = Math.sqrt((((ball.x - ball2.x) ** 2) + ((ball.y - ball2.y) ** 2)));
//     if distance < (ball.r + ball2.r) {
//
//     }
// }

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
