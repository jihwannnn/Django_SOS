document.addEventListener('DOMContentLoaded', function() {
    var currentQuestionIndex = 0;
    var questions = [
        // 여기에 각 챕터의 이미지 URL 목록을 추가하세요.
        //{% for question in questions %}
            //"{{ question.image.url }}",
        //{% endfor %}
    ];

    var questionImage = document.querySelector('.question-image');
    var prevBtn = document.getElementById('prevBtn');
    var nextBtn = document.getElementById('nextBtn');

    function updateQuestionImage() {
        questionImage.src = questions[currentQuestionIndex];
    }

    prevBtn.addEventListener('click', function() {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            updateQuestionImage();
        }
    });

    nextBtn.addEventListener('click', function() {
        if (currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            updateQuestionImage();
        }
    });

    // 초기 이미지 설정
    if (questions.length > 0) {
        updateQuestionImage();
    }
});
