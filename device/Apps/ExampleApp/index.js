function getPythonData() {
    // requests open window data from windows
    var request = $.ajax({
        type: 'get',
        url: "http://127.0.0.1:5001" + '/data',
        //async: false,
        data: {
            Name: "ExampleApp",
            Func: "getExampleData",
            ExpectReturn: true // maybe add like a thing to confirm that the request went through
        }
    }).done(function (data) {
        // once it has the open window data, make html elements for each open window
        console.log(data);
        document.getElementById("ExampleButton").innerHTML = data.text
    });
}