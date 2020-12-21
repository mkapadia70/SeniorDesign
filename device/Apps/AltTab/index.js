

function loadAppInfo() {
    // requests open window data from windows
    var request = $.ajax({
        type: 'get',
        url: "http://127.0.0.1:5001" + '/data',
        //async: false,
        data: {
            Name: "WindowsProgramControl",
            Func: "getOpenWindows",
            ExpectReturn: true // maybe add like a thing to confirm that the request went through
        }
    }).done(function (data) {
        // once it has the open window data, make html elements for each open window
        data.forEach(createOpenWindows);
    });
}

function createOpenWindows(value, index) {

    openWindow = '<div id=' + index + '> \
                    <img type="image" src="images/default.png" height=200 width=200>\
                    <p>' + value + '</p>\
                    </div>'

    $("#windowContainer").append(openWindow)

    if (index > 4) {
        breakFlex = '<div style="width: 100%"></div>'
        $("#windowContainer").append(breakFlex)
    }

    $("#" + index).on('click', function () {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
                Name: "WindowsProgramControl",
                Func: "switchFocus",
                Params: $("#" + index).children('p')[0].innerHTML, // why doesnt this work with arrays of params??
                ExpectReturn: false
        }, function (data) {
            
        });
        return false;
    });
}