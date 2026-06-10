function sendMessage(){

let msg =
document.getElementById(
"message"
).value;

let div =
document.getElementById(
"chat"
);

div.innerHTML +=
"<p>"+msg+"</p>";

}