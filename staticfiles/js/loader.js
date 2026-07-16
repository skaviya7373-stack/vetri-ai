document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            const btn = form.querySelector("button");

            btn.innerHTML = "⏳ Generating...";

            btn.disabled = true;

        });

    }

});