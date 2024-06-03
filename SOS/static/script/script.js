// login function
document.getElementById('loginForm').addEventListener('submit', function(event) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    // checking id and password is filled
    if (!username || !password) {
        event.preventDefault();
        alert('Please fill in both fields.');
    }
});
