async function getTodayWord() {
    try {
        const response = await fetch('http://localhost:8000/current-word');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        };
        const data = await response.json();
        return data
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

async function validateWord(playerWord) {
    try {
        const response = await fetch(`http://localhost:8000/validate/${playerWord}`)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        };
        const data = await response.json()
        return data
    } catch (error) {
        console.error('Error fetching data:', error);
    }
    
}

async function checkWords(playerWord) {
    try {
        const response = await fetch(`http://localhost:8000/check-word/${playerWord}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        };
        const data = await response.json();
        return data
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

let letter_counter = 0
let tries = 1
let row = document.getElementById(`row${tries}`);
let divReceiveLetter = row.querySelectorAll('.square');
divReceiveLetter.forEach(div => {
    div.classList.add('active');
});

function isLetter(key) {
    return /^[a-zA-ZçÇ]$/.test(key)
};

function getUserWord (divs) {
    if (letter_counter === divs.length) {
        let word = ''
        divs.forEach(div => {
            word += div.textContent;
        })
        return word
    };
};

function addSquareClasses(result) {
    for (let i = 0; i < 5; i++) {
        if (result[i] == "2"){
            divReceiveLetter[i].classList.add("correct")
            divReceiveLetter[i].classList.remove('active')
        } else if (result[i] == "0"){
            divReceiveLetter[i].classList.add("wrong")
            divReceiveLetter[i].classList.remove('active')
        } else if (result[i] == "1"){
            divReceiveLetter[i].classList.add("almost")
            divReceiveLetter[i].classList.remove('active')
        }
    }
}

function usedLetter(userWord) {
    for (const char of userWord) {
        const divsWithLettersUsed = document.querySelector(`div[letter="${char}"]`)
        if (divsWithLettersUsed.classList.contains("used")) {
            
        } else {
            divsWithLettersUsed.classList.add("used")
        }
    }
}


// Adding letters in squares
document.querySelectorAll(".keyboard_button").forEach(div => {
    div.addEventListener("click", handleLetter);
})
function handleLetter(event) {
    const pressedKey = event.type === "click" ? event.target.getAttribute("letter") : event.key;

    if (letter_counter < divReceiveLetter.length && isLetter(pressedKey)) {
        const currentSquare = divReceiveLetter[letter_counter];
        currentSquare.textContent = pressedKey;
        currentSquare.classList.add('with_letter');
        letter_counter++;
    };
};

// Deleting letters from square
document.getElementById("backspace_button").addEventListener("click", handleBackspace);
function handleBackspace(event) {
    if (
        letter_counter > 0 &&
        (event.type === "click" || event.key === "Backspace")
    ) {
        letter_counter--;
        const currentSquare = divReceiveLetter[letter_counter];
        currentSquare.textContent = "";
        currentSquare.classList.remove('with_letter');
    };
};

document.getElementById("enter_button").addEventListener("click", handleEnter);
async function handleEnter(event) {
    if (
        letter_counter == divReceiveLetter.length &&
        (event.type === 'click' || event.key === "Enter")
    ) {
        let userWord = getUserWord(divReceiveLetter);
        const message = document.getElementById("message")

        const wordValidate = await validateWord(userWord)

        if (wordValidate.validate == false) {
            row = document.getElementById(`row${tries}`);
            row.classList.add('shake_it');
            setTimeout(() => {
                row.classList.remove('shake_it');
            }, 400);

            const messageInvalid = document.getElementById("message_invalid");
            messageInvalid.classList.add('slide_up');
            setTimeout(() => {
                messageInvalid.classList.remove('slide_up');
            }, 1200);
        } else {
            const wordCheck = await checkWords(userWord)
            const result = wordCheck.validation


            if (wordCheck.status == "incorrect" && tries < 6) {
                addSquareClasses(result)
                usedLetter(userWord)
                tries++
                row = document.getElementById(`row${tries}`);
                divReceiveLetter = row.querySelectorAll('.square');
                divReceiveLetter.forEach(div => {
                    div.classList.add('active')
                })
                letter_counter = 0
            }
    
            else if (wordCheck.status == "incorrect" && tries == 6) {
                addSquareClasses(result)
                usedLetter(userWord)
                tries++
                message.textContent = "Perdeu!!"
                message.classList.add('loose')
            }
    
            else if (wordCheck.status == "correct") {
                usedLetter(userWord)
                addSquareClasses(result)
                letter_counter = 100
                message.textContent = "Ganhou!!"
                message.classList.add('win')
                divReceiveLetter.forEach(div => {
                    div.classList.remove('active')
                })
            }
        }
    }
}


document.addEventListener('keydown', function(event) {
    if (isLetter(event.key) && letter_counter < divReceiveLetter.length) {
        handleLetter(event)
    }

    else if (event.key === "Backspace" && letter_counter > 0) {
        handleBackspace(event)
    }

    else if (event.key === "Enter" && letter_counter == divReceiveLetter.length) {
        handleEnter(event)
    }
})