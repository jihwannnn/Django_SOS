document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById("popupModal");
    var questionBtn = document.getElementById("questionBtn");
    var studyBtn = document.getElementById("studyBtn");
    var span = document.getElementsByClassName("close")[0];

    questionBtn.onclick = function() {
        modal.style.display = "flex";
    }

    studyBtn.onclick = function() {
        modal.style.display = "flex";
    }

    span.onclick = function() {
        modal.style.display = "none";
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
