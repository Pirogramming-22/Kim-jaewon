let timerInterval;
let milliseconds = 0;

const timerNumber = document.getElementById("timer");
const startBtn = document.getElementById("start-btn");
const stopBtn = document.getElementById("stop-btn");
const resetBtn = document.getElementById("reset-btn");
const recordList = document.getElementById("record-list");
const selectAllCheckbox = document.getElementById("select-all");
const deleteBtn = document.getElementById("delete-btn");


function formatTime(ms) {
    const seconds = Math.floor(ms / 100); 
    const milliseconds = ms % 100; 
    return `${String(seconds).padStart(2, "0")}:${String(milliseconds).padStart(2, "0")}`;
}

function startTimer() {
    timerInterval = setInterval(() => {
        milliseconds++;
        timerNumber.textContent = formatTime(milliseconds);
    }, 10); 
}

function addRecord(time) {
    const li = document.createElement("li");
    li.innerHTML =`
    <input type="checkbox" class="record-checkbox">
    <span>${time}</span>
    `;
    recordList.appendChild(li);
}

function stopTimer() {
    clearInterval(timerInterval);
    addRecord(formatTime(milliseconds));
}

function resetTimer() {
    clearInterval(timerInterval);
    milliseconds = 0;
    timerNumber.textContent = "00:00";
}



function deleteSelectedRecords() {
    const checkboxes = document.querySelectorAll(".record-checkbox:checked");
    checkboxes.forEach((checkbox) => {
    checkbox.parentElement.remove();
    });
}

function SelectAll() {
    const allCheckboxes = document.querySelectorAll(".record-checkbox");
    allCheckboxes.forEach((checkbox) => {
    checkbox.checked = selectAllCheckbox.checked;
    });
}

startBtn.addEventListener("click", startTimer);
stopBtn.addEventListener("click", stopTimer);
resetBtn.addEventListener("click", resetTimer);
deleteBtn.addEventListener("click", deleteSelectedRecords);
selectAllCheckbox.addEventListener("change", SelectAll);
