const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");

signupBtn.onclick = () => {
    loginForm.style.marginLeft = "-50%";
    loginText.style.marginLeft = "-50%";
};

loginBtn.onclick = () => {
    loginForm.style.marginLeft = "0%";
    loginText.style.marginLeft = "0%";
};

signupLink.onclick = () => {
    signupBtn.click();
    return false;
};

const loginFormEl = document.getElementById("loginForm");
loginFormEl.addEventListener("submit", function (event) {
    event.preventDefault();

    const email = document.getElementById("loginEmail").value;
    const password = document.getElementById("loginPassword").value;

    const storedUser = JSON.parse(localStorage.getItem(email));

    if (storedUser && storedUser.password === password) {
        alert("Login successful!");
        window.location.href = "user-dashboard.html"; 
    } else {
        alert("Invalid credentials. Please try again.");
    }
});


const signupFormEl = document.getElementById("signupForm");
signupFormEl.addEventListener("submit", function (event) {
    event.preventDefault();

    const email = document.getElementById("signupEmail").value;
    const password = document.getElementById("signupPassword").value;

    if (localStorage.getItem(email)) {
        alert("User already exists. Please log in.");
        return;
    }

    const newUser = { email, password };
    localStorage.setItem(email, JSON.stringify(newUser));

    alert("You've registered successfully!");

    loginBtn.click();
});
