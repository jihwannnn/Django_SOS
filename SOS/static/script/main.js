document.addEventListener('DOMContentLoaded', function() {
    var quizModal = document.getElementById("quizModal");
    var studyModal = document.getElementById("studyModal");
    var retestModal = document.getElementById("retestModal");
    var questionBtn = document.getElementById("questionBtn");
    var studyBtn = document.getElementById("studyBtn");  
    var retestBtn = document.getElementById("retestBtn");  
    var mistake_logBtn = document.getElementById("mistake_logBtn"); 
    var closeButtons = document.getElementsByClassName("close-button");
    var quizChapter8Btn = document.getElementById("quizChapter8Btn");
    var quizChapter9Btn = document.getElementById("quizChapter9Btn");
    var quizChapter10Btn = document.getElementById("quizChapter10Btn");
    var studyChapter8Btn = document.getElementById("studyChapter8Btn");
    var studyChapter9Btn = document.getElementById("studyChapter9Btn");
    var studyChapter10Btn = document.getElementById("studyChapter10Btn");
    var retestChapter8Btn = document.getElementById("retestChapter8Btn");  
    var retestChapter9Btn = document.getElementById("retestChapter9Btn");  
    var retestChapter10Btn = document.getElementById("retestChapter10Btn");  

    // If click on question, study, retest button, modal pop out
    questionBtn.onclick = function() {
        quizModal.style.display = "flex";
    }
    studyBtn.onclick = function() {
        studyModal.style.display = "flex";
    }
    retestBtn.onclick = function() {
        retestModal.style.display = "flex";
    }

    // If click on modal's close button(X), modal is closed
    Array.from(closeButtons).forEach(function(button) {
        button.onclick = function() {
            quizModal.style.display = "none";
            studyModal.style.display = "none";
            retestModal.style.display = "none";
        }
    });

    //If click outside of modal, modal closed
    window.onclick = function(event) {
        if (event.target == quizModal) {
            quizModal.style.display = "none";
        }
        if (event.target == studyModal) {
            studyModal.style.display = "none";
        }
        if (event.target == retestModal) {  
            retestModal.style.display = "none";
        }
        if (event.target == retestModal) {
            retestModal.style.display = "none";
        }
    }

    // If click on Chpater buttons, move to questions, study and retest
    quizChapter8Btn.onclick = function() {
        window.location.href = "/question/quiz/8/";
    }
    quizChapter9Btn.onclick = function() {
        window.location.href = "/question/quiz/9/";
    }
    quizChapter10Btn.onclick = function() {
        window.location.href = "/question/quiz/10/";
    }
    studyChapter8Btn.onclick = function() {
        window.location.href = "/question/study/8/";
    }
    studyChapter9Btn.onclick = function() {
        window.location.href = "/question/study/9/";
    }
    studyChapter10Btn.onclick = function() {
        window.location.href = "/question/study/10/";
    }
    retestChapter8Btn.onclick = function() {
        window.location.href = "/question/retest/8/";
    }
    retestChapter9Btn.onclick = function() {
        window.location.href = "/question/retest/9/";
    }
    retestChapter10Btn.onclick = function() {
        window.location.href = "/question/retest/10/";
    }

    //If click on mistakelog, move to mistake_log page
    mistake_logBtn.onclick = function(){
        window.location.href = "/question/mistake_log";
    }

    // make image move corresponding to mouse movement
    var container = document.querySelector('.image-container');
    var overlay = document.querySelector('.overlay');
    container.addEventListener('mousemove', function(e) {
        var x = e.offsetX;
        var y = e.offsetY;
        var rotateY = -1 / 5 * x + 20;
        var rotateX = 4 / 30 * y - 20;
        overlay.style.backgroundPosition = `${x / 5 + y / 5}%`;
        overlay.style.filter = `opacity(${x / 200}) brightness(1.2)`;
        container.style.transform = `perspective(350px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    container.addEventListener('mouseout', function() {
        overlay.style.filter = 'opacity(0)';
        container.style.transform = 'perspective(350px) rotateY(0deg) rotateX(0deg)';
    });

    //If click on logout, make user log out
    logoutBtn.addEventListener('click', function() {
        fetch('/question/logout/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => {
            if (response.ok) {
                window.location.href = '/question/';
            } else {
                console.error('Logout failed');
            }
        })
        .catch(error => {
            console.error('Error during logout:', error);
        });
    });
});
