let feet;
let inches;
let metres;
let message1;
let message2;
let form_element;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    feet = document.getElementById('feet');
    inches = document.getElementById('inches');
    metres = document.getElementById('metres');
    message1 = document.getElementById('message1');
    message2 = document.getElementById('message2');
    form_element = document.querySelector('form');
    form_element.addEventListener('submit', convert, false);
}

function convert(event) {
    let feet_error = validate(feet, 0, 10);
    let inches_error = validate(inches, 0, 11);
    message1.innerHTML = feet_error;
    message2.innerHTML = inches_error;
    if (feet_error === '' && inches_error === '') {
        let feet_int = Number(feet.value);
        let inches_int = Number(inches.value);
        let metres_int = ((feet_int * 12) + inches_int) * 0.0254;
        metres.value = metres_int;
    }
    event.preventDefault();
}

function validate(element, min, max) {
    let value = element.value.trim();
    let error = '';
    if (value === '') {
        error = 'Required'
    } else {
        let number = ~~Number(value);
        if (String(number) !== value) {
            error = 'Must be a whole number';
        } else if (number < min) {
            error = 'Must be greater than ' + min;
        } else if (number > max) {
            error = 'Must be less than ' + max;
        }
    }
    return error
}
