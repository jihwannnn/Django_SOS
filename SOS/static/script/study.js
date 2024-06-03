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
    //getting chapter from url parameter
    const chapter = document.querySelector('.container').getAttribute('data-chapter');

    // setting chapter title
    const chapterTitle = document.getElementById('chapter-title');
    chapterTitle.textContent = `Chapter ${chapter} Study`;

    // animation activation class
    setTimeout(() => {
        chapterTitle.classList.add('show');
    }, 100); // start animation after 100ms

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
});