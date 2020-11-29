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

function msToMinSec(millis) {
    var minutes = Math.floor(millis / 60000);
    var seconds = ((millis % 60000) / 1000).toFixed(0);
    if (minutes < 0 || seconds < 0) {
        return "0:00"
    }
    return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
}

function minSecToMS(minSec) {
    var index = minSec.indexOf(":")
    var ms = minSec.substring(0, index) * 60000
    ms += minSec.substring(index+1) * 1000
    if (ms > 0) {
        return ms
    }
    return 0
}

var startedTimeUpdate = false

function loadSpotifyInfo(data) {
    
    document.getElementById("title").innerHTML = data.item.name
    document.getElementById("artist").innerHTML = data.item.artists[0].name
    document.getElementById("spotimage").src = data.item.album.images[0].url
    document.getElementById("seek").value = 100.0 * ((data.progress_ms) / (data.item.duration_ms))
    document.getElementById("leftTime").innerHTML = msToMinSec(data.progress_ms-780)
    document.getElementById("rightTime").innerHTML = msToMinSec(data.item.duration_ms)

    if ("false" == data.is_playing) {
        document.getElementById("pauseUnpause").src = "images/play.png"
        pressedApp = true
    }
    else {
        document.getElementById("pauseUnpause").src = "images/pause.png"
        pressedApp = false
    }

    if (startedTimeUpdate == false) {
        // this updates the seek every second
        window.setInterval(function(){
            if(pressedApp == false) {
                document.getElementById("leftTime").innerHTML = msToMinSec(minSecToMS(document.getElementById("leftTime").innerHTML) + 1000)
            }
        }, 1000);
        startedTimeUpdate = true
    }

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
                document.getElementById("pauseUnpause").src = "images/play.png"
            }
            else {
                document.getElementById("pauseUnpause").src = "images/pause.png"
            }
        });
        return false;
    });
});

$(function () {
    //binds the master volume slider
    function sendSeek() {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "seek",
            Params: $("#seek").val() / 100.0,
            ProcessId: -1, //whatever
            ExpectReturn: false
        }, function (data) {
        });
        document.getElementById("leftTime").innerHTML = msToMinSec(minSecToMS(document.getElementById("rightTime").innerHTML) * ($("#seek").val() / 100.0) -1000)
    };

    $('#seek').on('mouseup', sendSeek);
    $('#seek').on('touchend', sendSeek);
});
