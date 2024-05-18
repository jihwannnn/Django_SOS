document.addEventListener('DOMContentLoaded', function() {
    var quizModal = document.getElementById("quizModal");
    var studyModal = document.getElementById("studyModal");
    var questionBtn = document.getElementById("questionBtn");
    var studyBtn = document.getElementById("studyBtn");
    var closeButtons = document.getElementsByClassName("close-button");

    // "Quiz" 버튼을 클릭하면 퀴즈 모달 창이 열립니다.
    questionBtn.onclick = function() {
        quizModal.style.display = "flex";
    }

    // "Study" 버튼을 클릭하면 학습 모달 창이 열립니다.
    studyBtn.onclick = function() {
        studyModal.style.display = "flex";
    }

    // 모달 창의 닫기 버튼(X)을 클릭하면 모달 창이 닫힙니다.
    Array.from(closeButtons).forEach(function(button) {
        button.onclick = function() {
            quizModal.style.display = "none";
            studyModal.style.display = "none";
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
});