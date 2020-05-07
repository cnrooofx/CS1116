let bill;
let message;
let small_tip;
let large_tip;
let tip;
let form_element;

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    bill = document.querySelector('#bill');
    message = document.querySelector('#message');
    small_tip = document.querySelector('#small');
    large_tip = document.querySelector('#large');
    tip = document.querySelector('#tip');
    form_element = document.querySelector('form');
    form_element.addEventListener('submit', calculate, false);
}

function calculate(event) {
    let bill_amount = bill.value
    let error = check_for_pos_int(bill_amount);
    message.innerHTML = error;
    if (! error) {
        let bill_int = Number(bill_amount);
        let outcome;
        if (large_tip.checked) {
            outcome = (0.15 * bill_int);
        } else {
            outcome = (0.10 * bill_int);
        }
        tip.value = outcome;
    }
    event.preventDefault();
}

function check_for_pos_int(text) {
    let trimmed_text = text.trim();
    if (trimmed_text === "") {
        return "The bill must be a number greater than 0";
    }
    let number = Number(trimmed_text);
    if (String(number) !== trimmed_text) {
        return "The bill must be a number greater than 0";
    }
    if (number < 0) {
        return "The bill must be a number greater than 0";
    }
    return "";
}
