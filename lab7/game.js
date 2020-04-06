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


document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    main = document.querySelector('main');
    console.log(main);
    console.log(main.clientHeight);
    width = Math.min(main.clientWidth, main.clientHeight);
    canvas.height = canvas.width = width;
    size = width / grid_size;
    newGrid();
    move_up = false;
    move_down = false;
    move_left = false;
    move_right = false;
    interval_id = window.setInterval(draw, 100);
    window.addEventListener('keydown', activate, false);
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

function newGrid() {
    grid = []
    for (let i = 0; i < grid_size; i += 1) {
        let new_line = [];
        for (let i = 0; i < grid_size; i += 1) {
            new_line.push(0);
        }
        grid.push(new_line);
    }
}
function activate(event) {
    let KeyCode = event.keyCode;
    if (KeyCode === 37 && !move_right) {
        move_left = true;
        move_up = false;
        move_down = false;
        move_right = false;
    } else if (KeyCode === 38 && !move_down) {
        move_up = true;
        move_down = false;
        move_left = false;
        move_right = false;
    } else if (KeyCode === 39 && !move_left) {
        move_right = true;
        move_up = false;
        move_down = false;
        move_left = false;
    } else if (KeyCode === 40 && !move_up) {
        move_down = true;
        move_up = false;
        move_left = false;
        move_right = false;
    }
}
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
