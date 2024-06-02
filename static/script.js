var WebSocketString = "";

if (window.location.hostname == "127.0.0.1") {
  WebSocketString = "ws://localhost:8000/ws";
} else {
  WebSocketString = "wss://${window.location.hostname}$/ws";
}

var ws = new WebSocket(WebSocketString);
var sendButton = document.getElementById("sendButton");
var userInput = document.getElementById("userInput");
var chatHistory = document.getElementById("chatHistory");

ws.onmessage = function(event) {
  var message = event.data;
  var messageDiv = document.createElement("div");
  messageDiv.textContent = "- " + message;
  chatHistory.appendChild(messageDiv);
};

sendButton.onclick = function() {
  var message = userInput.value;
  ws.send(message);
  userInput.value = "";
};