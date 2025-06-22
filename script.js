let display = document.getElementById('display');

function press(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

function calculate() {
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression: display.value })
    })
    .then(response => response.json())
    .then(data => {
        display.value = data.result;
    })
    .catch(() => {
        display.value = 'Error';
    });
}
