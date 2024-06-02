var ws = new WebSocket("ws://localhost:8080/ws");
var sendButton = document.getElementById("sendButton");
var userInput = document.getElementById("userInput");
var chatHistory = document.getElementById("chatHistory");
var lastUserMessageDiv = null;
var isNewUserInput = true;

ws.onmessage = function(event) {
  var message = event.data.trim();

  if (lastUserMessageDiv && !isNewUserInput) {
    var shouldAddSpace = true;
    var noPrependSpaceChars = [",", ".", "!", "?", ";", ":", "'"];

    if (noPrependSpaceChars.includes(message.charAt(0))) {
      shouldAddSpace = false;
    }

    lastUserMessageDiv.textContent += (shouldAddSpace ? " " : "") + message;
  } else {
    var messageDiv = document.createElement("div");
    messageDiv.className = "chat-message ai-response";
    messageDiv.textContent = message;
    chatHistory.appendChild(messageDiv);
    lastUserMessageDiv = messageDiv;
    isNewUserInput = false;
  }
};

sendButton.onclick = function() {
  var message = userInput.value.trim();
  if (message) {
    var userInputDiv = document.createElement("div");
    userInputDiv.className = "chat-message user-input";
    userInputDiv.textContent = message;
    chatHistory.appendChild(userInputDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight;
    ws.send(message);
    userInput.value = "";
    isNewUserInput = true;
    lastUserMessageDiv = null;
  }
};