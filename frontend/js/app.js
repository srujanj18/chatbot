async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const response = await fetch("http://localhost:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput })
    });
    const data = await response.json();
    const messageBox = document.getElementById("messages");
    messageBox.innerHTML += `<div>User: ${userInput}</div><div>Bot: ${data.answer}</div>`;
    document.getElementById("user-input").value = "";
}
