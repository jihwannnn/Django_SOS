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

    // URL 파라미터에서 챕터 정보 가져오기
    const urlSegments = window.location.pathname.split('/');
    const chapter = urlSegments[urlSegments.length - 2];
    
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

    var totalQuestions = parseInt("{{ total_questions }}");
    var currentQuestionIndex = parseInt("{{ current_index }}");
    var total_1 = totalQuestions-1;

    var answers = JSON.parse(localStorage.getItem('quizAnswers')) || new Array(totalQuestions).fill(null);
    

    // 이전, 다음 버튼 클릭 이벤트 설정
    document.getElementById('prev').addEventListener('click', goToPreviousQuestion);
    document.getElementById('next').addEventListener('click', goToNextQuestion);

    // submit 버튼 클릭 이벤트 설정
    var forms = document.querySelectorAll('.answer-form');
    var resultModal = document.getElementById("resultModal");
    var closeModalBtn = document.getElementById("closeModalBtn");
    var resultMessage = document.getElementById("resultMessage");
    var correctImg = resultModal.getAttribute('data-correct-img');
    var wrongImg = resultModal.getAttribute('data-wrong-img');

    forms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // 폼 제출 기본 동작을 막음

            var answer = form.querySelector('#answer').value;
            answers[currentQuestionIndex] = answer;
            localStorage.setItem('quizAnswers', JSON.stringify(answers));
            console.log('Saved Answer:', answer); // 디버깅용 로그
            console.log('All Answers:', answers); // 디버깅용 로그

            var messages = ['You are correct!', 'You are wrong!'];
            var randomMessage = messages[Math.floor(Math.random() * messages.length)];
            resultMessage.textContent = randomMessage;

            console.log('Random Message:', randomMessage); // 디버깅용 로그
            console.log('Setting color for resultMessage'); // 디버깅용 로그

            // 메시지에 따라 글자 색상 및 이미지 변경
            if (randomMessage === 'You are correct!') {
                resultMessage.classList.add('correct');
                resultMessage.classList.remove('wrong');
                resultImage.src = correctImg;
            } else {
                resultMessage.classList.add('wrong');
                resultMessage.classList.remove('correct');
                resultImage.src = wrongImg;
            }

            resultModal.style.display = 'flex';
            document.body.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
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
    
    document.getElementById('tsubmitBtn').addEventListener('click', function() {
        fetch('/submit-answers/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}' // Django CSRF 토큰
            },
            body: JSON.stringify({
                chapter: chapter,
                answers: answers
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Submission Response:', data); // 디버깅용 로그
            if (data.success) {
                alert('Your answers have been submitted successfully!');
                // 제출 후 로컬 저장소 초기화
                localStorage.removeItem('quizAnswers');
                window.location.href = '/some-other-page/'; // 제출 후 이동할 페이지 설정
            } else {
                alert('There was an error submitting your answers.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting your answers.');
        });
    });
});