// sign up function
document.getElementById('signupForm').addEventListener('submit', function(event) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    const passwordConfirm = document.getElementById('password_confirm').value.trim();
    // checking id and password is filled
    if (!username || !password || !passwordConfirm) {
        event.preventDefault();
        alert('Please fill in all fields.');
        return;
    }
    // checking password is confirmed
    if (password !== passwordConfirm) {
        event.preventDefault();
        alert('Passwords do not match.');
    }
});
