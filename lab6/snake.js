let canvas;
let context;
let width;
let height;
let intervalId;

let body = [];

let size;
let halfSize;
let snake_size;
let length = 1;
let collided = false;

let moveUp = false;
let moveDown = false;
let moveLeft = false;
let moveRight = false;

let snake = {
    x : getRandomNumber(2, 22),
    y : getRandomNumber(2, 22),
    colour : 'green',
}
let apple = {
    x : getRandomNumber(0, 24),
    y : getRandomNumber(0, 24),
    value : 5,
    life : 0,
}
let grid_size = 25;
let grid = []
for (let i = 0; i < grid_size; i += 1) {
    let new_line = [];
    for (let i = 0; i < grid_size; i += 1) {
        new_line.push(0);
    }
    grid.push(new_line);
}

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width;
    height = canvas.height;
    size = width / grid.length;
    halfSize = size / 2;
    snake_size = size * 0.75;
    grid[apple.y][apple.x] = 2;
    intervalId = window.setInterval(main, 100);
    window.addEventListener('keydown', activate, false);
}

function main() {
    if (collided) {
        stop();
        window.alert('You lose :(');
    }
    if (moveUp || moveDown || moveLeft || moveRight) {
        body.push([snake.y, snake.x]);
    }
    if (body.length > length) {
        let tail = body.shift();
        grid[tail[0]][tail[1]] = 0;
    }
    // draw()
    drawSnake();
    drawApple();
    grid[snake.y][snake.x] = 1;
    if (moveUp) {
        snake.y--;
    } else if (moveDown) {
        snake.y++;
    } else if (moveLeft) {
        snake.x--;
    } else if (moveRight) {
        snake.x++;
    }
    collision();
}

function activate(event) {
    let KeyCode = event.keyCode;
    if (KeyCode === 37 && !moveRight) {
        moveLeft = true;
        moveUp = false;
        moveDown = false;
        moveRight = false;
    } else if (KeyCode === 38 && !moveDown) {
        moveUp = true;
        moveDown = false;
        moveLeft = false;
        moveRight = false;
    } else if (KeyCode === 39 && ! moveLeft) {
        moveRight = true;
        moveUp = false;
        moveDown = false;
        moveLeft = false;
    } else if (KeyCode === 40 && !moveUp) {
        moveDown = true;
        moveUp = false;
        moveLeft = false;
        moveRight = false;
    }
}

function collision() {
    if ((snake.x < 0) || (snake.x > grid.length-1) ||
    (snake.y < 0) || (snake.y > grid.length-1)) {
        collided = true;
    } else if ((grid[snake.y][snake.x] === 1) &&
    (moveUp || moveDown || moveLeft || moveRight)) {
        collided = true;
    }
}

function stop() {
    window.clearInterval(intervalId);
}

// function draw() {
//     context.clearRect(0, 0, width, height);
//     let row_number = 0;
//     for (let row of grid) {
//         let cell_number = 0;
//         for (let cell of row) {
//             if (cell === 2) {
//                 context.fillStyle = apple.colour;
//                 context.beginPath();
//                 context.arc(((apple.x*size)+halfSize), ((apple.y*size)+halfSize), apple_radius, 0, (2 * Math.PI));
//                 context.fill();
//             } else if (cell === 1) {
//                 context.fillStyle = snake.colour;
//                 context.fillRect((cell_number*size+2), (row_number*size+2), size-2, size-2);
//             }
//             cell_number++;
//         }
//         row_number++
//     }
// }

function drawSnake() {
    context.clearRect(0, 0, width, height);
    context.fillStyle = snake.colour;
    context.beginPath();
    context.arc(((snake.x*size)+halfSize), ((snake.y*size)+halfSize), snake_size*0.5, 0, (2 * Math.PI));
    context.fill();
    if (length > 1) {
        context.beginPath();
        context.strokeStyle = snake.colour;
        context.lineJoin = 'round';
        context.lineWidth = snake_size;
        context.moveTo((snake.x*size)+halfSize, (snake.y*size)+halfSize);
        for (let i = body.length-2; i >= 0; i--) {
            let segment = body[i]
            context.lineTo((segment[1]*size)+halfSize, (segment[0]*size)+halfSize);
        }
        context.stroke();
        context.beginPath();
        context.arc(((body[0][1]*size)+halfSize), ((body[0][0]*size)+halfSize), snake_size*0.5, 0, (2 * Math.PI));
        context.fill();
    }
}

function drawApple() {
    if ((grid[snake.y][snake.x] === 2) || (apple.life === 1))  {
        grid[apple.y][apple.x] = 0;
        grid[snake.y][snake.x] = 1;
        context.fillStyle = snake.colour;
        context.beginPath();
        context.arc(((snake.x*size)+halfSize), ((snake.y*size)+halfSize), (size * 0.7), 0, (2 * Math.PI));
        context.fill();
        length += apple.value;
        apple.x = getRandomNumber(0, grid.length-1);
        apple.y = getRandomNumber(0, grid.length-1);
        // while (grid[apple.y][apple.x] !== 1) {
        //     apple.x = getRandomNumber(0, grid.length-1);
        //     apple.y = getRandomNumber(0, grid.length-1);
        // }
        apple.value = getRandomNumber(2, 4);
        apple.value = getRandomNumber(1, 4);
        if (apple.value > 3) {
            apple.life = getRandomNumber(15, 30);
            apple.value = 5;
        } else {
            apple.life = 0;
        }
        grid[apple.y][apple.x] = 2;
    }
    if (apple.value > 3) {
        apple.life--;
        context.fillStyle = 'pink';
    } else {
        context.fillStyle = 'red';
    }
    context.beginPath();
    context.arc(((apple.x*size)+halfSize), ((apple.y*size)+halfSize), size*0.4, 0, (2 * Math.PI));
    context.fill();
}

// function updateScore() {}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
