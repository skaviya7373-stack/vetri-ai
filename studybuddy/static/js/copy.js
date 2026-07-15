function copyContent() {
    const content = document.getElementById("ai-content");

    if (!content) {
        alert("No content found!");
        return;
    }

    navigator.clipboard.writeText(content.innerText)
        .then(() => {
            alert("✅ Content copied successfully!");
        })
        .catch((err) => {
            console.error(err);
            alert("❌ Failed to copy content.");
        });
}