console.log("Hello");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;

slider.oninput = function () {
    output.innerHTML = this.value;
}

function copy() {
    let textarea = document.getElementById("textareacopy");
    textarea.select();
    document.execCommand("copy");
}

function clearsummary() {
    let textarea = document.getElementById("textareacopy");
    textarea.innerHTML = "";
}