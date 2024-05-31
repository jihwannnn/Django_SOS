console.log('study.js loaded'); // 파일이 로드되었는지 확인

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
    const chapter = document.querySelector('.container').getAttribute('data-chapter');
    
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

    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');

    // 첫 번째 문제일 때 이전 버튼 숨기기, 첫 번째가 아닐 때 다시 보이게 설정
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

    document.getElementById('prev').addEventListener('click', goToPreviousQuestion);
    document.getElementById('next').addEventListener('click', goToNextQuestion);

});