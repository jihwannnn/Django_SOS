console.log('quizscript.js loaded'); // 파일이 로드되었는지 확인

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

    // 문제 내용 설정 (데이터베이스에서 가져오는 로직 추가)
    const quizContent = document.getElementById('quiz-content');
    quizContent.textContent = `Quiz content for Chapter ${chapter}`; // 예시 텍스트

    console.log('Quiz Content:', quizContent.textContent); // 디버깅용 로그

    // 이전, 다음 버튼 클릭 이벤트 설정
    document.getElementById('prev').addEventListener('click', function() {
        // 이전 문제로 이동하는 로직 추가
        alert('Previous Question');
    });

    document.getElementById('next').addEventListener('click', function() {
        // 다음 문제로 이동하는 로직 추가
        alert('Next Question');
    });

    // 추가된 부분: submit 버튼 클릭 이벤트 설정
    var submitBtn = document.getElementById('submitBtn');
    var solvedProblemsCount = 0;
    var solvedProblemsLimit = 2; // 문제를 다 푼 것으로 간주하는 제출 횟수
    var solvedModal = document.getElementById('solvedModal');
    var closeModalBtn = document.getElementById('closeModalBtn');
    var mainPageBtn = document.getElementById('mainPageBtn');
    var incorrectAnsBtn = document.getElementById('incorrectAnsBtn');

    submitBtn.addEventListener('click', function() {
        solvedProblemsCount++;
        if (solvedProblemsCount >= solvedProblemsLimit) {
            // 문제를 다 푼 것으로 간주하고 모달 창을 띄움
            solvedModal.style.display = 'flex';
            // 화면이 어두워지도록 배경 스타일 적용
            document.body.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        }
    });

    closeModalBtn.addEventListener('click', function() {
        solvedModal.style.display = 'none';
        document.body.style.backgroundColor = ''; // 배경색 초기화
    });

    // 모달 외부를 클릭하면 모달 창이 닫힘
    window.onclick = function(event) {
        if (event.target == solvedModal) {
            solvedModal.style.display = 'none';
            document.body.style.backgroundColor = ''; // 배경색 초기화
        }
    }

    // 모달 창의 버튼 클릭 이벤트 설정
    mainPageBtn.addEventListener('click', function() {
        window.location.href = "{% url 'question:main' %}";
    });

    incorrectAnsBtn.addEventListener('click', function() {
        window.location.href = "{% url 'question:incorrect_answers' %}";
    });
    
});