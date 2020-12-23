

$(function () {
    $("#notepad").on("click", function () {
        var request = $.ajax({
            type: 'get',
            url: "http://127.0.0.1:5001" + '/data',
            //async: false,
            data: {
                Name: "WindowsProgramControl",
                Func: "startNotepad",
                ExpectReturn: false // maybe add like a thing to confirm that the request went through
            }
        });
    })
});