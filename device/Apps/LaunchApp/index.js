jQuery.ajaxSettings.traditional = true;

function loadAppInfo() {
    $.getJSON("http://127.0.0.1:5001" + '/data', {
        Name: "LaunchApplication",
        Func: "getAllApplications",
        // this fetches an array of applications
        // where each app is a dictionary containing
        // app name, app .exe, and app icon
        ExpectReturn: true
    }, function (data) {
        // once it has the applications data, make html elements for each icon
        // console.log(__dirname);
        data = JSON.parse(data);
        data.forEach(displayApps);
    });
}

function displayApps(value, index) {
    if (value.icon_path) {
        console.log(value.icon_path)
        var path = value.icon_path
        displayApp = '<div id="' + index + '" class="col-1 my-2"> \
                        <img type="image" src='+ String(path) +' height=50 width=50> \
                        </div>'

        $("#appContainer").append(displayApp)
    }
}