let feet_input;
let feet_span;
let inches_input;
let inches_span;
let metres_box;
let form_element;
let feet_msg;
let inches_msg;
let feet_int;
let inches_int;
let metres_int;

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    feet_input = document.getElementById('feet');
    feet_span = document.getElementById('message1');
    inches_input = document.getElementById('inches');
    inches_span = document.getElementById('message2');
    metres_box = document.getElementById('metres');
    form_element = document.querySelector('form');
    form_element.addEventListener('submit', convert_to_metres, false);
    feet_input.addEventListener('change', validate_input, false);
    inches_input.addEventListener('change', validate_input, false);
}

function validate_input(event) {
    feet_msg = check_for_int(feet_input.value, 0, 8);
    inches_msg = check_for_int(inches_input.value, 0, 11);
    feet_span.innerHTML = feet_msg;
    inches_span.innerHTML = inches_msg;
}

function convert_to_metres(event) {
    feet_msg = check_for_int(feet_input.value, 0, 8);
    inches_msg = check_for_int(inches_input.value, 0, 11);
    feet_span.innerHTML = feet_msg;
    inches_span.innerHTML = inches_msg;
    if (! feet_msg && ! inches_msg) {
        feet_int = Number(feet_input.value);
        inches_int = Number(inches_input.value);
        metres_int = ((feet_int * 12) + inches_int) * 0.0254;
        metres_box.value = metres_int;
    }
    event.preventDefault();
}

function check_for_int(text, minimum, maximum) {
    let trimmed_text = text.trim();
    if (trimmed_text === "") {
        return "Required";
    }
    let number = ~~Number(trimmed_text);
    if (String(number) !== trimmed_text) {
        return "Must be a whole number";
    }
    if (number < minimum) {
        return "Must be no less than " + minimum;
    }
    if (number > maximum) {
        return "Must be no greater than " + maximum;
    }
    return '';
}
