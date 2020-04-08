let canvas;
let context;
let width;
let main;
let size;
let interval_id;

let move_up;
let move_down;
let move_left;
let move_right;
let big_grid;
let big_size;
let grid;
let grid_size;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    main = document.querySelector('main');
    width = Math.min(main.clientWidth, main.clientHeight);
    canvas.height = canvas.width = width;
    big_size = 9;
    grid_size = 27;
    size = width / grid_size;
    newGrid(big_grid, big_size);
    newGrid(grid, grid_size);
    move_up = false;
    move_down = false;
    move_left = false;
    move_right = false;
    interval_id = window.setInterval(draw, 100);
    window.addEventListener('keydown', activate, false);
    window.addEventListener('keyup', deactivate, false);
}

function draw() {
    context.clearRect(0, 0, width, width);
    if (move_up) {
        snake.y -= 1;
    } else if (move_down) {
        snake.y += 1;
    } else if (move_left) {
        snake.x -= 1;
    } else if (move_right) {
        snake.x += 1;
    }
    if (collision()) {
        stop();
    }
    checkApple();
    if (move_up || move_down || move_left || move_right) {
        body.push([snake.x, snake.y]);
        grid[snake.y][snake.x] = 1;
    }
    if (body.length > length) {
        let tail = body.shift();
        grid[tail[1]][tail[0]] = 0;
    }
    drawSnake();
}

function build() {
    for (let i = 0; i < size_grid; i += 1) {
        for (let i = 0; i < size_grid; i += 1) {
            new_line.push(0);
        }
        name_grid.push(new_line);
    }
}
function newGrid(name_grid, size_grid) {
    name_grid = []
    for (let i = 0; i < size_grid; i += 1) {
        let new_line = [];
        for (let i = 0; i < size_grid; i += 1) {
            new_line.push(0);
        }
        name_grid.push(new_line);
    }
}
function stop() {
    window.alert('Game Over :(');
    clearInterval(interval_id);
    window.removeEventListener('keydown', activate);
    window.removeEventListener('keyup', deactivate);
    init();
}
function activate(event) {
    let KeyCode = event.keyCode;
    if (KeyCode === 37) {
        move_left = true;
    } else if (KeyCode === 38) {
        move_up = true;
    } else if (KeyCode === 39) {
        move_right = true;
    } else if (KeyCode === 40) {
        move_down = true;
    }
}
function deactivate(event) {
    let KeyCode = event.keyCode;
    if (KeyCode === 37) {
        move_left = false;
    } else if (KeyCode === 38) {
        move_up = false;
    } else if (KeyCode === 39) {
        move_right = false;
    } else if (KeyCode === 40) {
        move_down = false;
    }
}
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
