let canvas;
let context;
let width;
let main;
let size;
let interval_id;

let level;
let grid;
let grid_size;
let counter;

let player = {
    x : 13,
    y : 13,
    health : 100,
    move_up : false,
    move_down :  false,
    move_left : false,
    move_right : false,
    sprite : 0,
}
let monster = {
    x : 2,
    y : 2,
    damage : 25,
    move_up : false,
    move_down :  false,
    move_left : false,
    move_right : false,
}

let sprites;

let levels = [[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 6, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
  [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],

 [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]]

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    main = document.querySelector('main');
    width = 0.9 * Math.min(main.clientWidth, main.clientHeight);
    canvas.height = canvas.width = width;
    sprites = new Image();
    sprites.src = 'media/sprites.png'
    grid_size = 27;
    size = width / grid_size;
    newGrid();
    level = 0;

    player.x = 13;
    player.y = 13;
    player.health = 100;
    player.sprite = 0;
    monster.x = 2;
    monster.y = 2;
    monster.damage = 25;
    monster.move_speed = 5;

    player.move_up = false;
    player.move_down = false;
    player.move_left = false;
    player.move_right = false;
    monster.move_up = false;
    monster.move_down = true;
    monster.move_left = false;
    monster.move_right = false;

    change_level(level);
    interval_id = window.setInterval(draw, 100);
    window.addEventListener('keydown', activate, false);
    window.addEventListener('keyup', deactivate, false);
}

function draw() {
    context.clearRect(0, 0, width, width);
    build();
    move(player);
    move(monster);
    // if (collision()) {
    //     stop();
    // }
    // checkApple();
    // if (move_up || move_down || move_left || move_right) {
    //     body.push([snake.x, snake.y]);
    //     grid[snake.y][snake.x] = 1;
    // }
    // if (body.length > length) {
    //     let tail = body.shift();
    //     grid[tail[1]][tail[0]] = 0;
    // }
    // drawSnake();
}

function build() {
    for (let i = 0; i < grid_size; i += 1) {
        for (let j = 0; j < grid_size; j += 1) {
            let value = grid[j][i];
            if (value === 5) {
                context.drawImage(sprites, player.sprite, 48, 16, 16, size*i, size*j, size, size)
            } else if (value === 4) {
                context.drawImage(sprites, 0, 64, 16, 16, size*i, size*j, size, size)
            } else if (value === 6) {
                context.drawImage(sprites, 0, 16, 16, 16, size*i, size*j, size, size)
            } else if (value === 1) {
                context.drawImage(sprites, 0, 0, 16, 16, size*i, size*j, size, size)
            } else if (value === 0) {
                context.drawImage(sprites, 16, 0, 16, 16, size*i, size*j, size, size)
            }
        }
    }
}
function move(character) {
    if (character.move_up) {
        if (grid[character.y-1][character.x] !== 1) {
            grid[character.y][character.x] = 0;
            character.y -= 1;
        } else if (character === monster) {
            character.move_up = false;
            character.move_down = true;
        }
    } else if (character.move_down) {
        if (grid[character.y+1][character.x] !== 1) {
            grid[character.y][character.x] = 0;
            character.y += 1;
        } else if (character === monster) {
            character.move_down = false;
            character.move_up = true;
        }
    } else if (character.move_left) {
        if (grid[character.y][character.x-1] !== 1) {
            grid[character.y][character.x] = 0;
            character.x -= 1;
        } else if (character === monster) {
            character.move_left = false;
            character.move_right = true;
        }
    } else if (character.move_right) {
        if (grid[character.y][character.x+1] !== 1) {
            grid[character.y][character.x] = 0;
            character.x += 1;
        } else if (character === monster) {
            character.move_right = false;
            character.move_left = true;
        }
    }
    if (character === player) {
        grid[character.y][character.x] = 5
    } else if (character === monster) {
        grid[character.y][character.x] = 4
    }
}
function damage() {
    for (let x = player.x; x < player.x+3; x += 1) {
        for (let y = player.y; x < player.y+3; y += 1) {
            if (grid[y][x] === 4) {
                if (player.health-monster.damage < 0) {
                    stop()
                } else {
                    player.health -= monster.damage;
                }
            }
        }
    }
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
function change_level(num) {
    for (let i = 0; i < 27; i += 1) {
        for (let j = 0; j < 27; j += 1) {
            grid[i][+j] = levels[num][i][j]
        }
    }
    player.x = 13;
    player.y = 13;
    grid[player.y][player.x] = 5;
    grid[monster.y][monster.x] = 4;
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
        player.move_left = true;
        player.sprite = 0;
    } else if (KeyCode === 38) {
        player.move_up = true;
    } else if (KeyCode === 39) {
        player.move_right = true;
        player.sprite = 16;
    } else if (KeyCode === 40) {
        player.move_down = true;
    }
}
function deactivate(event) {
    let KeyCode = event.keyCode;
    if (KeyCode === 37) {
        player.move_left = false;
    } else if (KeyCode === 38) {
        player.move_up = false;
    } else if (KeyCode === 39) {
        player.move_right = false;
    } else if (KeyCode === 40) {
        player.move_down = false;
    }
}
function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
