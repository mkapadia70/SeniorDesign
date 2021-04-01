
function loadAppInfo() {
    // requests open window data from windows
    var request = $.ajax({
        type: 'get',
        url: "http://127.0.0.1:5001" + '/data',
        //async: false,
        data: {
            Name: "LaunchApplication",
            Func: "getAllApplications",
            // this fetches an array of applications
            // where each app is a dictionary containing
            // app name, app .exe, and app icon
            ExpectReturn: true
        }
    }).done(function (data) {
        // once it has the open window data, make html elements for each icon
        data.forEach(displayApp);
    });
}

function displayApp(value, index) {

}