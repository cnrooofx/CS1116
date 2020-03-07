let canvas;
let context;
let width;
let height;
let interval_id;

let body;
let grid_size = 25;
let grid;
let size;
let half_size;
let snake_size;
let length;
let collided;
let move_up;
let move_down;
let move_left;
let move_right;

let snake = {
    x : 0,
    y : 0,
    colour : 'green',
}
let apple = {
    x : 0,
    y : 0,
    value : 5,
    life : 0,
}

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width;
    height = canvas.height;
    size = width / grid_size;
    half_size = size / 2;
    snake_size = size * 0.75;
    newGrid();
    snake.x = getRandomNumber(2, 22);
    snake.y = getRandomNumber(2, 22);
    snake.colour = 'green';
    apple.x = getRandomNumber(3, 21);
    apple.y = getRandomNumber(3, 21);
    apple.value = 5;
    apple.life = 0;
    body = [];
    length = 1;
    move_up = false;
    move_down = false;
    move_left = false;
    move_right = false;
    grid[apple.y][apple.x] = 2;
    interval_id = window.setInterval(draw, 100);
    window.addEventListener('keydown', activate, false);
}

function draw() {
    context.clearRect(0, 0, width, height);
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
        body.push([snake.y, snake.x]);
        grid[snake.y][snake.x] = 1;
    }
    if (body.length > length) {
        let tail = body.shift();
        grid[tail[0]][tail[1]] = 0;
    }
    drawSnake();
    // test()
}
function collision() {
    if ((snake.x < 0) || (snake.x > grid_size-1) ||
    (snake.y < 0) || (snake.y > grid_size-1)) {
        return true;
    } else if ((grid[snake.y][snake.x] === 1) &&
    (move_up || move_down || move_left || move_right)) {
        return true;
    }
    return false;
}
function stop() {
    // grid[snake.y][snake.x] = 1;
    drawSnake();
    window.alert('You lose :(');
    clearInterval(interval_id);
    init()
}
function drawSnake() {
    context.fillStyle = snake.colour;
    context.beginPath();
    context.arc(((snake.x*size)+half_size), ((snake.y*size)+half_size), snake_size*0.5, 0, (2 * Math.PI));
    context.fill();
    if (length > 1) {
        context.beginPath();
        context.strokeStyle = snake.colour;
        context.lineJoin = 'round';
        context.lineWidth = snake_size;
        context.moveTo((snake.x*size)+half_size, (snake.y*size)+half_size);
        for (let i = body.length-2; i >= 0; i--) {
            let segment = body[i]
            context.lineTo((segment[1]*size)+half_size, (segment[0]*size)+half_size);
        }
        context.stroke();
        context.beginPath();
        context.arc(((body[0][1]*size)+half_size), ((body[0][0]*size)+half_size), snake_size*0.5, 0, (2 * Math.PI));
        context.fill();
    }
}
function checkApple() {
    if (apple.life === 1) {
        newApple()
    } else if (grid[snake.y][snake.x] === 2) {
        context.fillStyle = snake.colour;
        context.beginPath();
        context.arc(((snake.x*size)+half_size), ((snake.y*size)+half_size), size*0.7, 0, (2 * Math.PI));
        context.fill();
        length += apple.value;
        // updateScore();
        newApple();
    }
    if (apple.value > 3) {
        apple.life--;
        if (apple.life < 10 && apple.life > 0) {
            context.fillStyle = 'rgba(255, 0, 255, 0.25)';
        } else {
            context.fillStyle = 'rgb(255, 0, 255)';
        }
    } else {
        context.fillStyle = 'red';
    }
    context.beginPath();
    context.arc(((apple.x*size)+half_size), ((apple.y*size)+half_size), size*0.4, 0, (2 * Math.PI));
    context.fill();
}
function newApple() {
    grid[apple.y][apple.x] = 0;
    apple.x = getRandomNumber(0, grid_size-1);
    apple.y = getRandomNumber(0, grid_size-1);
    while (grid[apple.y][apple.x] === 1) {
        apple.x = getRandomNumber(0, grid_size-1);
        apple.y = getRandomNumber(0, grid_size-1);
    }
    apple.value = getRandomNumber(1, 4);
    if (apple.value > 3) {
        apple.life = getRandomNumber(15, 30);
        apple.value = 5;
    } else {
        apple.life = 0;
    }
    grid[apple.y][apple.x] = 2;
}
function updateScore() {

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

// function test() {
//     // context.clearRect(0, 0, width, height);
//     let row_number = 0;
//     for (let row of grid) {
//         let cell_number = 0;
//         for (let cell of row) {
//             if (cell === 2) {
//                 context.fillStyle = 'rgba(255, 0, 0, 0.2)';
//                 context.fillRect((cell_number*size+2), (row_number*size+2), size-2, size-2);
//                 // context.beginPath();
//                 // context.arc(((apple.x*size)+half_size), ((apple.y*size)+half_size), size*0.4, 0, (2 * Math.PI));
//                 // context.fill();
//             } else if (cell === 1) {
//                 context.fillStyle = 'rgba(0, 255, 0, 0.2)';
//                 context.fillRect((cell_number*size+2), (row_number*size+2), size-2, size-2);
//             } else {
//                 context.fillStyle = 'rgba(0, 0, 255, 0.2)';
//                 context.fillRect((cell_number*size+2), (row_number*size+2), size-2, size-2);
//             }
//             cell_number++;
//         }
//         row_number++
//     }
// }
