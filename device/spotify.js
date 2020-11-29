function myOnload() {
    //requests program data from python which requests it from windows
    $.getJSON("http://127.0.0.1:5001" + '/data', {
        Name: "SpotifyControl",
        Func: "getCurrentData",
        Params: 1, // bs numbers
        ProcessId: 2, // bs numbers
        ExpectReturn: true
    }, function (data) {
        loadSpotifyInfo(data)
    });
}

function loadSpotifyInfo(data) {
    console.log(data)
    document.getElementById("dataspot").innerHTML = data.item.name
    document.getElementById("spotimage").src = data.item.album.images[0].url
}

$(function () {
    //binds the master volume slider
    $('#skipSong').bind('click', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "skipSong",
            Params: 1,
            ProcessId: 2, //whatever
            ExpectReturn: true // maybe add like a thing to confirm that the request went through
        }, function (data) {
            loadSpotifyInfo(data)
        });
        return false;
    });
});
