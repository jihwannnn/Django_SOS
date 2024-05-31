document.addEventListener('DOMContentLoaded', function() {
    var quizModal = document.getElementById("quizModal");
    var studyModal = document.getElementById("studyModal");
    var retestModal = document.getElementById("retestModal");
    var questionBtn = document.getElementById("questionBtn");
    var studyBtn = document.getElementById("studyBtn");  
    var retestBtn = document.getElementById("retestBtn");  // 추가
    var mistake_logBtn = document.getElementById("mistake_logBtn"); //by G
    var closeButtons = document.getElementsByClassName("close-button");
    var quizChapter8Btn = document.getElementById("quizChapter8Btn");
    var quizChapter9Btn = document.getElementById("quizChapter9Btn");
    var quizChapter10Btn = document.getElementById("quizChapter10Btn");
    var studyChapter8Btn = document.getElementById("studyChapter8Btn");
    var studyChapter9Btn = document.getElementById("studyChapter9Btn");
    var studyChapter10Btn = document.getElementById("studyChapter10Btn");
    var retestChapter8Btn = document.getElementById("retestChapter8Btn");  // 추가
    var retestChapter9Btn = document.getElementById("retestChapter9Btn");  // 추가
    var retestChapter10Btn = document.getElementById("retestChapter10Btn");  // 추가

    // "Quiz" 버튼을 클릭하면 퀴즈 모달 창이 열립니다.
    questionBtn.onclick = function() {
        quizModal.style.display = "flex";
    }

    // "Study" 버튼을 클릭하면 학습 모달 창이 열립니다.
    studyBtn.onclick = function() {
        studyModal.style.display = "flex";
    }

    // "Retest" 버튼을 클릭하면 재시험 모달 창이 열립니다.
    retestBtn.onclick = function() {
        retestModal.style.display = "flex";
    }

    // 모달 창의 닫기 버튼(X)을 클릭하면 모달 창이 닫힙니다.
    Array.from(closeButtons).forEach(function(button) {
        button.onclick = function() {
            quizModal.style.display = "none";
            studyModal.style.display = "none";
            retestModal.style.display = "none";
        }
    });

    // 모달 외부를 클릭하면 모달 창이 닫힙니다.
    window.onclick = function(event) {
        if (event.target == quizModal) {
            quizModal.style.display = "none";
        }
        if (event.target == studyModal) {
            studyModal.style.display = "none";
        }
        if (event.target == retestModal) {  // 수정
            retestModal.style.display = "none";
        }
        if (event.target == retestModal) {
            retestModal.style.display = "none";
        }
    }

    // Chapter 버튼 클릭 시 퀴즈 페이지로 이동
    quizChapter8Btn.onclick = function() {
        window.location.href = "/question/quiz/8/";
    }

    quizChapter9Btn.onclick = function() {
        window.location.href = "/question/quiz/9/";
    }

    quizChapter10Btn.onclick = function() {
        window.location.href = "/question/quiz/10/";
    }

    // Study 버튼 클릭 시 학습 페이지로 이동
    studyChapter8Btn.onclick = function() {
        window.location.href = "/question/study/8/";
    }

    studyChapter9Btn.onclick = function() {
        window.location.href = "/question/study/9/";
    }

    studyChapter10Btn.onclick = function() {
        window.location.href = "/question/study/10/";
    }

    // Mistake log 버튼 클릭시 해당 페이지로 이동 by G
    mistake_logBtn.onclick = function(){
        window.location.href = "/question/mistake_log";
    }

    // retest 버튼 클릭 시 재시험 페이지로 이동
    retestChapter8Btn.onclick = function() {
        window.location.href = "/question/retest/8/";
    }

    retestChapter9Btn.onclick = function() {
        window.location.href = "/question/retest/9/";
    }

    retestChapter10Btn.onclick = function() {
        window.location.href = "/question/retest/10/";
    }

    // 이미지 컨테이너 마우스 움직임에 따른 효과
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
