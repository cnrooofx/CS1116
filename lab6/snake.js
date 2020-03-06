let canvas;
let context;
let width;
let height;
let intervalId;

let body = [];

let size;
let length = 1;
let prev_x;
let prev_y;
let moveUp = false;
let moveDown = false;
let moveLeft = false;
let moveRight = false;

let snake = {
    x : getRandomNumber(2, 22),
    y : getRandomNumber(2, 22),
    colour : 'green'
}
let apple = {
    x : getRandomNumber(2, 22),
    y : getRandomNumber(2, 22),
    colour : 'red',
}

// let grid_size = 25;
// let grid = [ for (y of Array(grid_size)) [ for (x of Array(grid_size) 0 ]]
let grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]];

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width;
    height = canvas.height;
    size = (width / grid.length);
    // intervalId = window.setInterval(draw, 66);
    window.setInterval(draw, 120)
    window.addEventListener('keydown', activate, false);
}

function draw() {
    while (body.length < length) {
        console.log('hi')
        let piece = {
            x : 0,
            y : 0,
            age : 0,
        }
        body.push(piece)
    }
    context.clearRect(0, 0, width, height);
    grid[apple.y][apple.x] = 2;
    for (let piece of body) {
        if (piece.age > length) {
            grid[piece.y][piece.x] = 0;
        }
        piece.age++;

    }
    // grid[prev_y][prev_x] = 0;
    if (grid[snake.y][snake.x] === 2) {
        apple.x = getRandomNumber(2, 22);
        apple.y = getRandomNumber(2, 22);
        length++;
    }
    grid[snake.y][snake.x] = 1;
    let row_number = 0;
    for (let row of grid) {
        let cell_number = 0;
        for (let cell of row) {
            if (cell === 2) {
                context.fillStyle = apple.colour;
                context.fillRect((cell_number*size), (row_number*size), size, size);
            } else if (cell === 1) {
                context.fillStyle = snake.colour;
                context.fillRect((cell_number*size), (row_number*size), size, size);
            }
            cell_number++;
        }
        row_number++
    }
    prev_x = snake.x;
    prev_y = snake.y;
    if (moveUp) {
        --snake.y;
    } else if (moveDown) {
        ++snake.y;
    } else if (moveLeft) {
        --snake.x;
    } else if (moveRight) {
        ++snake.x;
    }
    edges()
    // if (grid[snake.y][snake.x] === 1) {
    //     stop()
    // }
    // length++;
}

function activate(event) {
    let KeyCode = event.keyCode;
    if (KeyCode === 37) {
        moveLeft = true;
        moveUp = false;
        moveDown = false;
        moveRight = false;
    } else if (KeyCode === 38) {
        moveUp = true;
        moveDown = false;
        moveLeft = false;
        moveRight = false;
    } else if (KeyCode === 39) {
        moveRight = true;
        moveUp = false;
        moveDown = false;
        moveLeft = false;
    } else if (KeyCode === 40) {
        moveDown = true;
        moveUp = false;
        moveLeft = false;
        moveRight = false;
    }
}

function edges() {
    if ((snake.x < 0) || (snake.x > grid.length) ||
    (snake.y < 0) || (snake.y > grid.length)) {
        window.alert('You lose :(')
        stop()
    }
}

function stop() {
    window.clearInterval(intervalId);
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
