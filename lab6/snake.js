let canvas;
let context;
let width;
let height;
let intervalId;

let body = [];

let size;
let apple_radius;
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
    x : getRandomNumber(2, 22),
    y : getRandomNumber(2, 22),
    colour : 'red',
    value : 2,
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
    apple_radius = (size*0.45)
    intervalId = window.setInterval(main, 100);
    // window.setInterval(draw, 120)
    window.addEventListener('keydown', activate, false);
}

function main() {
    if (moveUp || moveDown || moveLeft || moveRight) {
        body.push([snake.y, snake.x]);
    }
    context.clearRect(0, 0, width, height);
    grid[apple.y][apple.x] = 2;
    if (body.length > length) {
        let tail = body.shift();
        grid[tail[0]][tail[1]] = 0;
    }
    if (grid[snake.y][snake.x] === 2) {
        length += apple.value;
        apple.x = getRandomNumber(0, grid.length-1);
        apple.y = getRandomNumber(0, grid.length-1);
        apple.value = 1;
    }
    grid[snake.y][snake.x] = 1;
    draw()
    if (collided) {
        stop()
        window.alert('You lose :(');
    }
    if (moveUp) {
        snake.y--;
    } else if (moveDown) {
        snake.y++;
    } else if (moveLeft) {
        snake.x--;
    } else if (moveRight) {
        snake.x++;
    }
    collision()
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

function draw() {
  // console.log('draw')
    let row_number = 0;
    for (let row of grid) {
        let cell_number = 0;
        for (let cell of row) {
            if (cell === 2) {
                context.fillStyle = apple.colour;
                // context.fillRect((cell_number*size), (row_number*size), size, size);
                context.beginPath();
                context.arc(((cell_number*size)+(size/2)), ((row_number*size)+(size/2)), apple_radius, 0, (2 * Math.PI));
                context.fill();
            } else if (cell === 1) {
                context.fillStyle = snake.colour;
                context.fillRect((cell_number*size+2), (row_number*size+2), size-2, size-2);
            }
            cell_number++;
        }
        row_number++
    }
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
