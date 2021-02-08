
$(function () {
    $('#ExampleButton').on('click', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "ExampleApp",
            Func: "getExampleData",
            Params: [],
            ExpectReturn: true
        }, function (data) {
            console.log(data);
            document.getElementById("ExampleButton").innerHTML = data.text
        });
    });
});

$(function () {
    $('#TextButton').on('click', function () {
        var text = document.getElementById("textbox").value
        console.log(text)
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "ExampleApp",
            Func: "numberOfLetters",
            Params: text,
            ExpectReturn: true
        }, function (data) {
            console.log(data);
            document.getElementById("number").innerHTML = data.numberVal
        });
    });
});