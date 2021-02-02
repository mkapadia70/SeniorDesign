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
        document.getElementById("volumeImage").src = "images/volume0.PNG"
    } else if (vol < 33) {
        document.getElementById("volumeImage").src = "images/volume1.PNG"
    } else if (vol < 67) {
        document.getElementById("volumeImage").src = "images/volume2.PNG"
    } else {
        document.getElementById("volumeImage").src = "images/volume3.PNG"
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
                document.getElementById("pauseUnpause").src = "images/play.png"
                startTimer()
            }
            else {
                document.getElementById("pauseUnpause").src = "images/pause.png"
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
                document.getElementById("shuffleSong").src = "images/shuffleOn.png"
            }
            else {
                document.getElementById("shuffleSong").src = "images/shuffleOff.png"
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
                document.getElementById("repeatSong").src = "images/repeatOff.png"
            }
            else if (repeatTrinary % 3 == 2) {
                document.getElementById("repeatSong").src = "images/repeatContext.png"
            }
            else {
                document.getElementById("repeatSong").src = "images/repeatTrack.png"
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