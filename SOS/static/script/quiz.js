console.log('quizs.js loaded');

// functions for moving to previous and next question pages
function goToPreviousQuestion() {
    if (currentQuestionIndex > 0) {
        window.location.href = window.location.pathname + "?q=" + (currentQuestionIndex - 1);
    }
}
function goToNextQuestion() {
    if (currentQuestionIndex < totalQuestions - 1) {
        window.location.href = window.location.pathname + "?q=" + (currentQuestionIndex + 1);
    }
}

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOMContentLoaded event fired'); 

    //getting chapter from url parameter
    const chapter = document.querySelector('.container').getAttribute('data-chapter');
    
    console.log('Chapter:', chapter);

    // setting chapter title
    const chapterTitle = document.getElementById('chapter-title');
    chapterTitle.textContent = `Chapter ${chapter} Quiz`;

    console.log('Chapter Title Text:', chapterTitle.textContent); 

    // animation activation class
    setTimeout(() => {
        chapterTitle.classList.add('show');
        console.log('Animation Class Added'); 
    }, 100); // start animation after 100ms

    // variable for storing submitted answers
    var answers = JSON.parse(localStorage.getItem('quizAnswers')) || new Array(totalQuestions).fill("");

     // logic for make next button and prev button invisivle in specific case
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    if (currentQuestionIndex === 0) {
        prevButton.classList.add('invisible');
    } else {
        prevButton.classList.remove('invisible');
    }
    if (currentQuestionIndex === totalQuestions-1) {
        nextButton.classList.add('invisible');
    } else {
        nextButton.classList.remove('invisible');
    }

    // loading logic for moving to prev and next question pages on click
    document.getElementById('prev').addEventListener('click', goToPreviousQuestion);
    document.getElementById('next').addEventListener('click', goToNextQuestion);

    // getting element used for submit
    var forms = document.querySelectorAll('.answer-form');
    var resultModal = document.getElementById("resultModal");
    var closeModalBtn = document.getElementById("closeModalBtn");
    var resultMessage = document.getElementById("resultMessage");
    var resultImage = document.getElementById("resultImage"); 
    var correctImg = resultModal.getAttribute('data-correct-img');
    var wrongImg = resultModal.getAttribute('data-wrong-img');

    //form for submitting user's answer
    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // prevent general form's post function
            var answer = form.querySelector('#answer').value;
            answers[currentQuestionIndex] = answer;
            localStorage.setItem('quizAnswers', JSON.stringify(answers));
            console.log('Saved Answer:', answer); 
            console.log('All Answers:', answers); 

            // checking submiitted answer is correct
            if (correctAnswers == answer.toLowerCase()) {
                resultMessage.textContent = 'You are correct!';
                resultMessage.classList.add('correct');
                resultMessage.classList.remove('wrong');
                resultImage.src = correctImg;
            } else {
                resultMessage.textContent = 'You are wrong!';
                resultMessage.classList.add('wrong');
                resultMessage.classList.remove('correct');
                resultImage.src = wrongImg;
            }
            resultModal.style.display = 'flex';
            document.body.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        });
    });

    //handling for modal closing
    closeModalBtn.addEventListener('click', function() {
        resultModal.style.display = 'none';
        document.body.style.backgroundColor = ''; 
    });
    window.onclick = function(event) {
        if (event.target == resultModal) {
            resultModal.style.display = 'none';
            document.body.style.backgroundColor = ''; 
        }
    }

    //default setting totalModal for none
    document.getElementById('totalModal').style.display = 'none';
    // if tsubmit is clicked, open totalModal
    document.getElementById('tsubmitBtn').addEventListener('click', function() {
        document.getElementById('totalModal').style.display = 'flex'; 
    });

    //if click yes in totalModal, post result to server 
    document.getElementById('yesButton').addEventListener('click', function() {
        fetch(`/question/quiz/${chapter_num}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({
                answers: answers
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Submission Response:', data); 
            //if success post, move to result page
            if (data.success) {
                localStorage.removeItem('quizAnswers');
                window.location.href = '/question/result/';
            //if not, error alert
            } else {
                alert('There was an error submitting your answers: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting your answers.');
        });
    });

    //if click no in totalModal, close modal
    document.getElementById('noButton').addEventListener('click', function() {
        document.getElementById('totalModal').style.display = 'none';
    });
});
