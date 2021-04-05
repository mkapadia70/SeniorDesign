jQuery.ajaxSettings.traditional = true;

function loadAppInfo() {
    $.getJSON("http://127.0.0.1:5001" + '/data', {
        Name: "LaunchApplication",
        Func: "getAllApplicationsEmulation",
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
        if ( !value.name.includes("Uninstall") && !value.name.includes("uninstall") &&
        !value.name.includes("Remove") && !value.name.includes("remove") &&
        !value.name.includes("x86") && !value.name.includes("preferences") &&
        !value.name.includes("skinned") ){
            var path = value.icon_path
            var name = value.name
            displayApp = '<div id="' + index + '" class="col-3 my-2" style="display: flex; justify-content: space-between;"> \
                            <img type="image" src='+ String(path) +' height=50 width=50> \
                            <p> '+ String(name) +'<\p> \
                            </div>'

            $("#appContainer").append(displayApp)
        }
    }
}