const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const { window } = new JSDOM(`<!DOCTYPE html>`);
const $ = require('jQuery')(window);

$(function() {
    $('#testSlider').bind('input', function() {
        $.getJSON("http://127.0.0.1:5001" + '/data', {
            volume: document.getElementById("testSlider").value
        }, function(data) {
            $("#result").text(data.result);
        });
        console.log("why")
        return false;
    });
});