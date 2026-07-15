document.addEventListener("DOMContentLoaded", function () {
    console.log("Vetri AI Loaded Successfully");
});

function copyContent() {
    // Copy content
}

function downloadPDF() {
    window.location.href = "/download-pdf/";
}

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function () {
            const btn = form.querySelector("button");
            if (btn) {
                btn.innerHTML = "⏳ Generating...";
                btn.disabled = true;
            }
        });
    }
});