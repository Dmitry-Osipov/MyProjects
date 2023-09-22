let userName = askName();

function askName() {
    return prompt('Введите Ваше имя');
}

function sendOnEnter(event) {
    if (event.key === 'Enter') {
        send();
    }
}

function send() {
    let message = document.getElementById('message').value;

    if (message == '') {
        alert("Нужно ввести сообщение");
        return;
    }

    document.getElementById('result').innerText = `${userName}: ${message}`;
}

document.getElementById('message').addEventListener('keypress', sendOnEnter);