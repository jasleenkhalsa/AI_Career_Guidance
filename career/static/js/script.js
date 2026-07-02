/* ==========================================
   AI Personalized Career Guidance System
   script.js
========================================== */

document.addEventListener("DOMContentLoaded", function () {

    console.log("Career Guidance System Loaded");

    // ============================
    // Password Match Validation
    // ============================

    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");
    const message = document.getElementById("message");

    if (password && confirmPassword && message) {

        confirmPassword.addEventListener("keyup", function () {

            if (password.value === confirmPassword.value) {

                message.innerHTML = "✔ Passwords Match";
                message.style.color = "green";

            } else {

                message.innerHTML = "✖ Passwords Do Not Match";
                message.style.color = "red";

            }

        });

    }

    // ============================
    // Phone Number Validation
    // ============================

    const phone = document.querySelector("input[name='phone']");

    if (phone) {

        phone.addEventListener("input", function () {

            this.value = this.value.replace(/\D/g, "");

            if (this.value.length > 10) {

                this.value = this.value.slice(0, 10);

            }

        });

    }

    // ============================
    // Email Validation
    // ============================

    const email = document.querySelector("input[type='email']");

    if (email) {

        email.addEventListener("blur", function () {

            let pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

            if (this.value !== "" && !this.value.match(pattern)) {

                alert("Please enter a valid email address.");

                this.focus();

            }

        });

    }

    // ============================
    // Questionnaire Validation
    // ============================

    const assessmentForm = document.querySelector("form");

    if (assessmentForm && window.location.pathname.includes("questionnaire")) {

        assessmentForm.addEventListener("submit", function (e) {

            let totalQuestions = 30;
            let answered = 0;

            for (let i = 1; i <= totalQuestions; i++) {

                if (document.querySelector(`input[name="q${i}"]:checked`)) {

                    answered++;

                }

            }

            if (answered < totalQuestions) {

                e.preventDefault();

                alert("Please answer all questions before submitting.");

            }

        });

    }

    // ============================
    // Loading Button Animation
    // ============================

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const btn = form.querySelector("button[type='submit']");

            if (btn) {

                btn.innerHTML = "Please Wait...";

                btn.disabled = true;

            }

        });

    });

    // ============================
    // Smooth Scroll
    // ============================

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            e.preventDefault();

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {

                target.scrollIntoView({

                    behavior: "smooth"

                });

            }

        });

    });

    // ============================
    // Card Hover Effect
    // ============================

    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {

        card.addEventListener("mouseenter", function () {

            this.style.transform = "scale(1.02)";

        });

        card.addEventListener("mouseleave", function () {

            this.style.transform = "scale(1)";

        });

    });

    // ============================
    // Fade In Animation
    // ============================

    const fadeElements = document.querySelectorAll(".card");

    fadeElements.forEach(function (element) {

        element.classList.add("fade-in");

    });

});