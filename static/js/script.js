/**
 * RENTCAST AI - GLOBAL JAVASCRIPT
 * Handles Theme Toggle, UI Animations, Dashboard Updates,
 * Loading States, and Navigation Behavior
 */

document.addEventListener("DOMContentLoaded", function () {

    const htmlElement = document.documentElement;
    const themeToggle = document.getElementById("themeToggle");
    const form = document.getElementById("predictionForm");
    const loading = document.getElementById("loading");


/* ==================================================
   1. DARK MODE TOGGLE WITH LOCAL STORAGE
================================================== */

if (themeToggle) {

    const themeIcon = themeToggle.querySelector("i");

    const savedTheme = localStorage.getItem("theme") || "light";

    htmlElement.setAttribute("data-theme", savedTheme);

    updateToggleIcon(savedTheme);

    themeToggle.addEventListener("click", function () {

        const currentTheme = htmlElement.getAttribute("data-theme");

        const newTheme = currentTheme === "light" ? "dark" : "light";

        htmlElement.setAttribute("data-theme", newTheme);

        localStorage.setItem("theme", newTheme);

        updateToggleIcon(newTheme);

    });


    function updateToggleIcon(theme) {

        if (!themeIcon) return;

        if (theme === "dark") {
            themeIcon.classList.remove("fa-moon");
            themeIcon.classList.add("fa-sun");
        } else {
            themeIcon.classList.remove("fa-sun");
            themeIcon.classList.add("fa-moon");
        }

    }

}



/* ==================================================
   2. FORM SUBMISSION LOADING STATE
================================================== */

if (form) {

    form.addEventListener("submit", function () {

        if (loading) {
            loading.style.display = "block";
        }

        const btn = form.querySelector(".predict-btn");

        if (btn) {
            btn.disabled = true;
            btn.style.opacity = "0.7";
        }

    });

}



/* ==================================================
   3. SIDEBAR ACTIVE LINK DETECTION
================================================== */

const navLinks = document.querySelectorAll(".sidebar a");

navLinks.forEach(link => {

    const linkPath = link.getAttribute("href");

    if (linkPath === window.location.pathname) {

        link.classList.add("active");

    } else {

        link.classList.remove("active");

    }

});



/* ==================================================
   4. DASHBOARD AUTO REFRESH
================================================== */

if (window.location.pathname === "/dashboard") {

    setTimeout(function () {

        location.reload();

    }, 30000); // refresh every 30 seconds

}



/* ==================================================
   5. KPI CARD COUNTER ANIMATION
================================================== */

const counters = document.querySelectorAll(".kpi-counter");

counters.forEach(counter => {

    const target = parseFloat(counter.innerText.replace(/[^0-9.]/g, ""));

    if (!target) return;

    let current = 0;

    const increment = target / 60;

    function animateCounter() {

        current += increment;

        if (current >= target) {
            current = target;
        }

        counter.innerText = Math.floor(current);

        if (current < target) {
            requestAnimationFrame(animateCounter);
        }

    }

    animateCounter();

});



/* ==================================================
   6. RESULT PAGE PRICE COUNTER
================================================== */

const priceCounter = document.getElementById("priceCounter");

if (priceCounter && window.predictedPrice) {

    let count = 0;

    const target = window.predictedPrice;

    const increment = target / 60;

    function animatePrice() {

        count += increment;

        if (count >= target) {
            count = target;
        }

        priceCounter.innerText = "$" + Math.floor(count);

        if (count < target) {
            requestAnimationFrame(animatePrice);
        }

    }

    animatePrice();

}



/* ==================================================
   7. GLOBAL CHART RESIZE FIX
================================================== */

window.addEventListener("resize", function () {

    if (window.Chart && Chart.instances) {

        Object.values(Chart.instances).forEach(chart => {
            chart.resize();
        });

    }

});



/* ==================================================
   8. BUTTON RIPPLE EFFECT (UI POLISH)
================================================== */

document.querySelectorAll(".predict-btn").forEach(button => {

    button.addEventListener("click", function (e) {

        const ripple = document.createElement("span");

        ripple.classList.add("ripple");

        this.appendChild(ripple);

        const rect = this.getBoundingClientRect();

        ripple.style.left = (e.clientX - rect.left) + "px";
        ripple.style.top = (e.clientY - rect.top) + "px";

        setTimeout(() => {
            ripple.remove();
        }, 600);

    });

});



/* ==================================================
   9. SMOOTH SCROLLING FOR DASHBOARD
================================================== */

document.querySelectorAll("a[href^='#']").forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {

            e.preventDefault();

            target.scrollIntoView({
                behavior: "smooth"
            });

        }

    });

});

});