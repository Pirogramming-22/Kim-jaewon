let attempts = 9;
let randomNumbers = [];

function initializeGame() {

    attempts = 9;
    document.getElementById("attempts").innerText = attempts;

    randomNumbers = generateRandomNumbers();

    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
    document.getElementById("attempts").innerHTML = `${attempts}`;
    document.getElementById("game-result-img").src = "";

    document.querySelector(".submit-button").removeAttribute("disabled");
}

function generateRandomNumbers() {
    const numbers = [];
    while (numbers.length < 3) {
        const  randInt = Math.floor(Math.random() * 10);
        if (numbers.includes(randInt)){
            continue;
        }
        numbers.push(randInt);
    }
    return numbers;
}

function check_numbers() {
    const input1 = document.getElementById("number1").value;
    const input2 = document.getElementById("number2").value;
    const input3 = document.getElementById("number3").value;

    if (input1 === "" || input2 === "" || input3 === "") {
        document.getElementById("number1").value = "";
        document.getElementById("number2").value = "";
        document.getElementById("number3").value = "";
        return;
    }
    const inputArray = [parseInt(input1), parseInt(input2), parseInt(input3)];
    
    //시도 횟수 감소
    decreaseAttempts();
    
    //결과 계산
    const result = calculateResult(inputArray);


    //결과 디스플레이 표시
    const resultContainer = document.getElementById("results");
    const resultElement = document.createElement("div");

    resultElement.innerHTML = inputArray.join(" ") + 
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + 
    ":" + 
    "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" +
    result.html;
    resultContainer.appendChild(resultElement);


    if (result.plain === "3 S 0 B") {
        document.getElementById("game-result-img").src = "success.png";
        document.querySelector(".submit-button").disabled = true;
    } else if (attempts === 0) {
        document.getElementById("game-result-img").src = "fail.png";
        document.querySelector(".submit-button").disabled = true;
    }

    document.getElementById("number1").value = "";
    document.getElementById("number2").value = "";
    document.getElementById("number3").value = "";
}

function decreaseAttempts(){
    attempts--;
    const attemptsElement = document.getElementById("attempts");
    attemptsElement.innerHTML = `${attempts}`;
}


function calculateResult(inputArray) {
    let strikes = 0;
    let balls = 0;

    for(let i =0; i< inputArray.length; i++) {
        if (inputArray[i] === randomNumbers[i]) {
            strikes++;
        } else if (randomNumbers.includes(inputArray[i])) {
            balls++;
        }
    }

    const plainResult = `${strikes} S ${balls} B`;

    if (strikes === 0 && balls === 0) {
        return {
            html: `<span class="out">O</span>`,
            plain: "O",
        };
    }
    
    return {
        html: `${strikes} <span class="strike">S</span> ${balls} <span class="out">B</span>`,
        plain: plainResult,
    };
}

window.onload = initializeGame;