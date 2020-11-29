function myOnload() {
    //requests program data from python which requests it from windows
    $.getJSON("http://127.0.0.1:5001" + '/data', {
        Name: "SpotifyControl",
        Func: "getCurrentData",
        Params: 0, // bs numbers
        ProcessId: -1, // bs numbers
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
    //binds skip song button
    $('#skipSong').on('click', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "skipSong",
            Params: 0,
            ProcessId: -1, //whatever
            ExpectReturn: true // maybe add like a thing to confirm that the request went through
        }, function (data) {
            loadSpotifyInfo(data)
        });
    });
});

$(function () {
    //binds skip song button
    $('#prevSong').on('click', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "prevSong",
            Params: 0,
            ProcessId: -1, //whatever
            ExpectReturn: true // maybe add like a thing to confirm that the request went through
        }, function (data) {
            loadSpotifyInfo(data)
        });
    });
});

var pressedApp = false;
//pause/unpause song
$(function () {
    $('#pauseUnpause').on("click", function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: (pressedApp ? "playSong" : "pauseSong"),
            Params: 0,
            ProcessId: -1, //whatever
            ExpectReturn: false
        }, function (data) {
            pressedApp = !pressedApp
            if (pressedApp) {
                document.getElementById("pauseUnpause").innerHTML = "Play"
            }
            else {
                document.getElementById("pauseUnpause").innerHTML = "Pause"
            }
        });
        return false;
    });
});
