jQuery.ajaxSettings.traditional = true;

//this will hold all of our dynamic jquery stuff for the windows volume mixer
//master volume
$(function () {
    //binds the master volume slider
    $('#masterVolume').on('input', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "WindowsVolumeMixerControl",
            Func: "setMasterVolume",
            Params: [$("#masterVolume").val() / 100.0],
            ExpectReturn: false
        }, function (data) {
        });
        return false;
    });
});

function myOnload() {
    //requests program data from python which requests it from windows
    $.getJSON("http://127.0.0.1:5001" + '/data', {
        Name: "WindowsVolumeMixerControl",
        Func: "getAllSoundDeviceData",
        ExpectReturn: true
    }, function (data) {
        data.forEach(changeSliderData);
    });
}

function changeSliderData(value, index) {
    //This function add the relative sliders for the data to the html
    //also binds the sliders to send back updates on volume to windows       
    sliderHTML = ' \
        <div class="col-sm-3"> \
            <input type="range" min="0" max="100" value="' + (value.currentVolume * 100) + '" class="slider" id="' + index + '"> \
            <h3 class="text-center">' + value.name + '</h3> \
            <input type="checkbox" id="muteUnmuteApp' + index + '" style="display: none;"> \
            <label for="muteUnmuteApp' + index + '" class="unmute"> \
                <img src="images/mute.png" title="Mute icon" id="mute' + index + '" style="width: 20%; height: 20%; display: none;"> \
            </label> \
            <label for="muteUnmuteApp' + index + '" class="mute"> \
                <img src="images/speaker.png" title="Speaker icon" id="speaker' + index + '" style="width: 20%; height: 20%; display: initial;"> \
            </label> \
        </div>'

    $("#sliderContainer").append(sliderHTML)

    $("#" + index).on('input', function () {
        //console.log("Button: " + index + ", Volume: " + $("#" + index).val() + ", PID:" + value.pid)
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "WindowsVolumeMixerControl",
            Func: "setApplicationVolume",
            Params: [$("#" + index).val() / 100.0, value.pid],
        }, function (data) {
        });
        return false;
    });

    // mute/unmute individual app
    $("#muteUnmuteApp" + index).on("change", function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "WindowsVolumeMixerControl",
            Func: ($("#muteUnmuteApp" + index).is(':checked') ? "muteApplicationVolume" : "unmuteApplicationVolume"),
            Params: [value.pid],
            ExpectReturn: false
        }, function (data) {
            if ($("#muteUnmuteApp" + index).is(':checked')) {
                $("#mute" + index).css("display", "initial");
                $("#speaker" + index).css("display", "none");
            }
            else {
                $("#mute" + index).css("display", "none");
                $("#speaker" + index).css("display", "initial");
            }
        });
        return false;
    });
}

var pressedApp = false;
// mute/unmute master
$(function () {
    $('#muteUnmuteApp').on("change", function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            Name: "WindowsVolumeMixerControl",
            Func: (pressedApp ? "unmuteMasterVolume" : "muteMasterVolume"),
        }, function (data) {
            pressedApp = !pressedApp
        });
        return false;
    });
});