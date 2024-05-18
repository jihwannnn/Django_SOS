console.log('quizscript.js loaded'); // 파일이 로드되었는지 확인

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOMContentLoaded event fired'); // 디버깅용 로그

    // URL 파라미터에서 챕터 정보 가져오기
    const urlParams = new URLSearchParams(window.location.search);
    const chapter = urlParams.get('chapter_num') || '8'; // 기본값: 8

    console.log('Chapter:', chapter); // 디버깅용 로그

    // 챕터 타이틀 설정
    const chapterTitle = document.getElementById('chapter-title');
    chapterTitle.textContent = `Chapter ${chapter}`;

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
});