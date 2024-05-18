document.getElementById('signupForm').addEventListener('submit', function(event) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const passwordConfirm = document.getElementById('password_confirm').value.trim();

    if (!username || !password || !passwordConfirm) {
        event.preventDefault();
        alert('Please fill in all fields.');
        return;
    }

    if (password !== passwordConfirm) {
        event.preventDefault();
        alert('Passwords do not match.');
    }
});
