const { time } = require('console');
const fs = require('fs')

jQuery.ajaxSettings.traditional = true;

function loadData() {

    var request = $.ajax({
        type: 'get',
        url: "http://127.0.0.1:5001" + '/data',
        //async: false,
        data: {
            Name: "SpotifyControl",
            Func: "getUpdatedData",
            ExpectReturn: true // maybe add like a thing to confirm that the request went through
        }
    }).done(function (data) {
        if (data != null) {
            loadSpotifyInfo(data)
            loadImage()
        }
        else {
            console.log("failed to get spotify data...trying again")

        }
    });


}


function loadImage() {
    var request = $.ajax({
        type: 'get',
        url: "http://127.0.0.1:5001" + '/data',
        //async: false,
        data: {
            Name: "SpotifyControl",
            Func: "getAlbumImage",
            ExpectReturn: true // maybe add like a thing to confirm that the request went through
        }
    }).done(function (data) {
        if (data != null) {
            console.log(data)
            base64_decode(data.imageString, __dirname + "\\images\\album.jpg")
        }
        else {
            console.log("failed to get album image")
            // clear buffer and retry
            clearBuffer()
        }
        skipDone = true
        if (inBetweenSkip > 0) {
            inBetweenSkip--;
            $('#skipSong').trigger('click'); // swag
        }
        prevDone = true
        if (inBetweenPrev > 0) {
            inBetweenPrev--;
            $('#prevSong').trigger('click'); // swag
        }
    });

}

function clearBuffer() {
    var request = $.ajax({
        type: 'get',
        url: "http://127.0.0.1:5001" + '/data',
        //async: false,
        data: {
            Name: "SerialHandler",
            Func: "clearBuffer",
            ExpectReturn: false // maybe add like a thing to confirm that the request went through
        }
    })
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
    ms += minSec.substring(index + 1) * 1000
    if (ms > 0) {
        return ms
    }
    return 0
}

function loadSpotifyInfo(data) {
    console.log(data)
    document.getElementById("title").innerHTML = data.item.name
    document.getElementById("artist").innerHTML = data.item.artists[0].name
    document.getElementById("spotimage").src = 'images/default.png' // placeholder album image, incase request is bunk
    document.getElementById("leftTime").innerHTML = msToMinSec(data.progress_ms - 780)
    document.getElementById("rightTime").innerHTML = msToMinSec(data.item.duration_ms)
    document.getElementById("seek").value = 100.0 * ((minSecToMS(document.getElementById("leftTime").innerHTML)) / (minSecToMS(document.getElementById("rightTime").innerHTML))) //yes
    document.getElementById("volume").value = data.volume
    changeVolumeImage()


    if (false == data.is_playing) {
        document.getElementById("pauseUnpause").src = "images/play.png"
        pauseButton = true
    }
    else {
        document.getElementById("pauseUnpause").src = "images/pause.png"
        pauseButton = false
        startTimer()
    }

}


function changeVolumeImage() {
    var vol = document.getElementById("volume").value
    console.log(vol)
    if (vol == 0) {
        $("#volumeImage path").attr("d", "M0 5v6h2.804L8 14V2L2.804 5H0zm7-1.268v8.536L3.072 10H1V6h2.072L7 3.732zm8.623 2.121l-.707-.707-2.147 2.147-2.146-2.147-.707.707L12.062 8l-2.146 2.146.707.707 2.146-2.147 2.147 2.147.707-.707L13.477 8l2.146-2.147z")
    } else if (vol < 33) {
        $("#volumeImage path").attr("d", "M10.04 5.984l.658-.77q.548.548.858 1.278.31.73.31 1.54 0 .54-.144 1.055-.143.516-.4.957-.259.44-.624.805l-.658-.77q.825-.865.825-2.047 0-1.183-.825-2.048zM0 11.032v-6h2.802l5.198-3v12l-5.198-3H0zm7 1.27v-8.54l-3.929 2.27H1v4h2.071L7 12.302z")
    } else if (vol < 67) {
        $("#volumeImage path").attr("d", "M0 11.032v-6h2.802l5.198-3v12l-5.198-3H0zm7 1.27v-8.54l-3.929 2.27H1v4h2.071L7 12.302zm4.464-2.314q.401-.925.401-1.956 0-1.032-.4-1.957-.402-.924-1.124-1.623L11 3.69q.873.834 1.369 1.957.496 1.123.496 2.385 0 1.262-.496 2.385-.496 1.123-1.369 1.956l-.659-.762q.722-.698 1.123-1.623z")
    } else {
        $("#volumeImage path").attr("d", "M12.945 1.379l-.652.763c1.577 1.462 2.57 3.544 2.57 5.858s-.994 4.396-2.57 5.858l.651.763a8.966 8.966 0 00.001-13.242zm-2.272 2.66l-.651.763a4.484 4.484 0 01-.001 6.397l.651.763c1.04-1 1.691-2.404 1.691-3.961s-.65-2.962-1.69-3.962zM0 5v6h2.804L8 14V2L2.804 5H0zm7-1.268v8.536L3.072 10H1V6h2.072L7 3.732z")
    }
}

var lastVolume = 50 // stores volume to return to on unmute
//onclick of the volume image toggles mute
// !!! this is kind of big and can be cut down using ternary statements but im too lazy to do it (tri?) !!!
$(function () {
    //binds mute volume button
    $('#volumeImage').on('click', function () {
        var vol = document.getElementById("volume").value
        if (vol == 0) {
            $.getJSON("http://127.0.0.1:5001" + '/data', {
                Name: "SpotifyControl",
                Func: "setVolume",
                Params: [lastVolume],
                ExpectReturn: false
            }, function (data) {
                changeVolumeImage()
            });
            document.getElementById("volume").value = lastVolume
        } else {
            lastVolume = vol
            document.getElementById("volume").value = 0
            $.getJSON("http://127.0.0.1:5001" + '/data', {
                Name: "SpotifyControl",
                Func: "setVolume",
                Params: [0],
                ExpectReturn: false
            }, function (data) {
                changeVolumeImage()
            });
        }
    });
});


var startedTimeUpdate = false

function startTimer() {
    if (startedTimeUpdate == false) {
        // this updates the seek every second
        window.setInterval(function () {
            if (pauseButton == false) {
                document.getElementById("leftTime").innerHTML = msToMinSec(minSecToMS(document.getElementById("leftTime").innerHTML) + 1000)
                document.getElementById("seek").value = 100.0 * ((minSecToMS(document.getElementById("leftTime").innerHTML)) / (minSecToMS(document.getElementById("rightTime").innerHTML)))
            }
            if (((minSecToMS(document.getElementById("leftTime").innerHTML)) >= ((minSecToMS(document.getElementById("rightTime").innerHTML))))) {
                document.getElementById("leftTime").innerHTML = "0:00"
                loadData()
            }
        }, 1000);
        startedTimeUpdate = true
    }
}

var skipDone = true // keeps track of if the skip request + update data is done
var inBetweenSkip = 0 // keeps track of the skips that are requested while the current skip is processing
$(function () {
    //binds skip song button
    $('#skipSong').on('click', function () {
        if (skipDone) {
            skipDone = false
            var request = $.ajax({
                type: 'get',
                url: "http://127.0.0.1:5001" + '/data',
                //async: false,
                data: {
                    Name: "SpotifyControl",
                    Func: "skipSong",
                    ExpectReturn: false // maybe add like a thing to confirm that the request went through
                }
            }).done(function () {
                loadData()
            });
        } else {
            inBetweenSkip++;
        }
    });
});

var prevDone = true // keeps track of if the skip request + update data is done
var inBetweenPrev = 0 // keeps track of the skips that are requested while the current skip is processing
$(function () {
    // binds previous song button
    $('#prevSong').on('click', function () {
        // if the song is greater than 3 seconds, restart song, else change sond
        // just like the pros
        if (minSecToMS(document.getElementById("leftTime").innerHTML) < 3000) {
            if (prevDone) {
                prevDone = false
                $.ajax({
                    type: 'get',
                    url: "http://127.0.0.1:5001" + '/data',
                    //async: false,
                    data: {
                        Name: "SpotifyControl",
                        Func: "previousSong",
                        ExpectReturn: false // maybe add like a thing to confirm that the request went through
                    }
                }).done(function () {
                    loadData()
                });
            } else {
                inBetweenPrev++;
            }
        } else {
            $.ajax({
                type: 'get',
                url: "http://127.0.0.1:5001" + '/data',
                //async: false,
                data: {
                    Name: "SpotifyControl",
                    Func: "seek",
                    Params: [0],
                    ExpectReturn: false // maybe add like a thing to confirm that the request went through
                }
            });
            document.getElementById("leftTime").innerHTML = "0:00";
        }
    })
});

var pauseButton = false;
//pause/unpause song
$(function () {
    $('#pauseUnpause').on("click", function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: (pauseButton ? "startPlayback" : "pausePlayback"),
            ExpectReturn: false
        }, function (data) {
            pauseButton = !pauseButton
            if (pauseButton) {
                $("#pauseUnpause svg path").attr("d", "M4.018 14L14.41 8 4.018 2z")
                startTimer()
            }
            else {
                $("#pauseUnpause svg path").attr("d", "M3 2h3v12H3zM10 2h3v12h-3z")
            }
        });
        return false;
    });
});

var shuffleBool = false;
//shuffle stuff
$(function () {
    $('#shuffleSong').on("click", function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "setShuffle",
            Params: [!shuffleBool],
            ExpectReturn: false
        }, function (data) {
            shuffleBool = !shuffleBool
            if (shuffleBool) {
                $("#shuffleSong svg path").attr("d", "M 4.5 6.8 l 0.7 -0.8 C 4.1 4.7 2.5 4 0.9 4 v 1 c 1.3 0 2.6 0.6 3.5 1.6 l 0.1 0.2 z m 7.5 4.7 c -1.2 0 -2.3 -0.5 -3.2 -1.3 l -0.6 0.8 c 1 1 2.4 1.5 3.8 1.5 V 14 l 3.5 -2 l -3.5 -2 v 1.5 z m 0 -6 V 7 l 3.5 -2 L 12 3 v 1.5 c -1.6 0 -3.2 0.7 -4.2 2 l -3.4 3.9 c -0.9 1 -2.2 1.6 -3.5 1.6 v 1 c 1.6 0 3.2 -0.7 4.2 -2 l 3.4 -3.9 c 0.9 -1 2.2 -1.6 3.5 -1.6 M 6 15 C 6 14.5 6.5 14 7 14 S 8 14.5 8 15 S 7.5 16 7 16 S 6 15.5 6 15 z")
            }
            else {
                $("#shuffleSong svg path").attr("d", "M4.5 6.8l.7-.8C4.1 4.7 2.5 4 .9 4v1c1.3 0 2.6.6 3.5 1.6l.1.2zm7.5 4.7c-1.2 0-2.3-.5-3.2-1.3l-.6.8c1 1 2.4 1.5 3.8 1.5V14l3.5-2-3.5-2v1.5zm0-6V7l3.5-2L12 3v1.5c-1.6 0-3.2.7-4.2 2l-3.4 3.9c-.9 1-2.2 1.6-3.5 1.6v1c1.6 0 3.2-.7 4.2-2l3.4-3.9c.9-1 2.2-1.6 3.5-1.6z")
            }
        });
        return false;
    });
});

var repeatStruct = ["off", "context", "track"];
var repeatTrinary = 1
//repeat stuff
$(function () {
    $('#repeatSong').on("click", function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "setRepeatStatus",
            Params: [repeatStruct[(repeatTrinary++) % 3]],
            ExpectReturn: false
        }, function (data) {
            if (repeatTrinary % 3 == 1) {
                $("#repeatSong svg path").attr("d", "M5.5 5H10v1.5l3.5-2-3.5-2V4H5.5C3 4 1 6 1 8.5c0 .6.1 1.2.4 1.8l.9-.5C2.1 9.4 2 9 2 8.5 2 6.6 3.6 5 5.5 5zm9.1 1.7l-.9.5c.2.4.3.8.3 1.3 0 1.9-1.6 3.5-3.5 3.5H6v-1.5l-3.5 2 3.5 2V13h4.5C13 13 15 11 15 8.5c0-.6-.1-1.2-.4-1.8z")
            }
            else if (repeatTrinary % 3 == 2) {
                $("#repeatSong svg path").attr("d", "M5.5 5H10v1.5l3.5-2-3.5-2V4H5.5C3 4 1 6 1 8.5c0 .6.1 1.2.4 1.8l.9-.5C2.1 9.4 2 9 2 8.5 2 6.6 3.6 5 5.5 5zm9.1 1.7l-.9.5c.2.4.3.8.3 1.3 0 1.9-1.6 3.5-3.5 3.5H6v-1.5l-3.5 2 3.5 2V13h4.5C13 13 15 11 15 8.5c0-.6-.1-1.2-.4-1.8 V 7 M 7 16 C 7 15.5 7.5 15 8 15 S 9 15.5 9 16 S 8.5 17 8 17 S 7 16.5 7 16 z")
            }
            else {
                $("#repeatSong svg path").attr("d", "M 5 5 v -0.5 V 4 c -2.2 0.3 -4 2.2 -4 4.5 c 0 0.6 0.1 1.2 0.4 1.8 l 0.9 -0.5 C 2.1 9.4 2 9 2 8.5 C 2 6.7 3.3 5.3 5 5 z M 10.5 12 H 6 v -1.5 l -3.5 2 l 3.5 2 V 13 h 4.5 c 1.9 0 3.5 -1.2 4.2 -2.8 c -0.5 0.3 -1 0.5 -1.5 0.6 c -0.7 0.7 -1.6 1.2 -2.7 1.2 z M 11.5 0 C 9 0 7 2 7 4.5 S 9 9 11.5 9 S 16 7 16 4.5 S 14 0 11.5 0 z m 0.9 7 h -1.3 V 3.6 H 10 v -1 h 0.1 c 0.2 0 0.3 0 0.4 -0.1 c 0.1 0 0.3 -0.1 0.4 -0.2 c 0.1 -0.1 0.2 -0.2 0.2 -0.3 c 0.1 -0.1 0.1 -0.2 0.1 -0.3 v -0.1 h 1.1 V 7 M 7 16 C 7 15.5 7.5 15 8 15 S 9 15.5 9 16 S 8.5 17 8 17 S 7 16.5 7 16 z")
            }
        });
        return false;
    });
});

$(function () {
    //binds seek slider
    function sendSeek() {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "seek",
            Params: [$("#seek").val() / 100.0],
            ExpectReturn: false
        }, function (data) {
        });
        document.getElementById("leftTime").innerHTML = msToMinSec(minSecToMS(document.getElementById("rightTime").innerHTML) * ($("#seek").val() / 100.0) - 1000)
    };

    $('#seek').on('mouseup', sendSeek);
    $('#seek').on('touchend', sendSeek);
});

$(function () {
    //binds volume slider
    function sendSeek() {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "setVolume",
            Params: [$("#volume").val()],
            ExpectReturn: false
        }, function (data) {
            changeVolumeImage()
        });
    };

    $('#volume').on('mouseup', sendSeek);
    $('#volume').on('touchend', sendSeek);
});

$(function () {
    $('#searchButton').on("click", function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "search",
            Params: [$("#search").val()],
            ExpectReturn: true
        }, function (data) {
            while (document.getElementById("searchResults").firstChild) {
                document.getElementById("searchResults").removeChild(document.getElementById("searchResults").firstChild);
            }
            data.tracks.items.forEach(searchResults)
        });
        return false;
    });
});

function searchResults(value, index) {

    var id = value.uri
    searchRes = ' \
        <div color=white id=searchResult' + index + ' title=' + id + '> \
            ' + value.name + ' ' + value.artists[0].name + '\
        </div>'
    $("#searchResults").append(searchRes)

    $("#searchResult" + index).on('click', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "SpotifyControl",
            Func: "playTrack",
            Params: [$("#searchResult" + index).attr('title')],
            ExpectReturn: true
        }, function (data) {
            loadData()
        });
        return false;
    });
}

// decode and store base64 strings to image, used for the album art
function base64_decode(base64Image, file) {
    base64Image = base64Image.substring(2, base64Image.length - 1)
    base64Image += "data:image/jpeg;base64,"
    fs.writeFile(file, Buffer.from(base64Image, 'base64'), function (err) {
        if (err) {
            console.log("image write error")
        }
        else {
            document.getElementById("spotimage").src = file + '?' + new Date().getTime(); // the le epic cache breaker
        }
    });
}