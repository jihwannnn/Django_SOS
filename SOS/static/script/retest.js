console.log('quizscript.js loaded'); // 파일이 로드되었는지 확인

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
    console.log('DOMContentLoaded event fired'); // 디버깅용 로그

    const quizContainer = document.querySelector('.container');
    const chapter = quizContainer.dataset.chapter;
    
    console.log('Chapter:', chapter); // 디버깅용 로그

    // 챕터 타이틀 설정
    const chapterTitle = document.getElementById('chapter-title');
    chapterTitle.textContent = `Chapter ${chapter} Quiz`;

    console.log('Chapter Title Text:', chapterTitle.textContent); // 디버깅용 로그

    // 애니메이션 활성화 클래스 추가
    setTimeout(() => {
        chapterTitle.classList.add('show');
        console.log('Animation Class Added'); // 디버깅용 로그
    }, 100); // 페이지 로드 후 100ms 대기 후 애니메이션 시작

    // 이전, 다음 버튼 클릭 이벤트 설정
    document.getElementById('prev').addEventListener('click', goToPreviousQuestion);
    document.getElementById('next').addEventListener('click', goToNextQuestion);

    // submit 버튼 클릭 이벤트 설정
    var form = document.getElementById('quizForm');
    var resultModal = document.getElementById("resultModal");
    var closeModalBtn = document.getElementById("closeModalBtn");
    var resultMessage = document.getElementById("resultMessage");
    var resultImage = document.getElementById("resultImage");
    var correctImg = resultModal.getAttribute('data-correct-img');
    var wrongImg = resultModal.getAttribute('data-wrong-img');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // 폼 제출 기본 동작을 막음
        var formData = new FormData(form);

        fetch(window.location.href, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            var result = data.result;
            if (result === 'correct') {
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
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    closeModalBtn.addEventListener('click', function() {
        resultModal.style.display = 'none';
        document.body.style.backgroundColor = ''; // 배경색 초기화
    });

    // 모달 외부를 클릭하면 모달 창이 닫힘
    window.onclick = function(event) {
        if (event.target == resultModal) {
            resultModal.style.display = 'none';
            document.body.style.backgroundColor = ''; // 배경색 초기화
        }
    }
});