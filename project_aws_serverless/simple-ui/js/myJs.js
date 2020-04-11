var app = angular.module('myAjs', []);
var myNav = document.getElementById("myNav");

$(document).keyup(function (e) {
    if (e.keyCode == 27) { // escape key maps to keycode `27`
        closeNav();
    }
});

app.controller('linksSummary', function ($scope, $http) {
    $http.get("./resources/links.json").then(function (res) {
        $scope.linksData = res.data.links;
    });

    $scope.setHref = function (url,heading) {
        var content = "";
        content = "<iframe class='pdfView' src='" + url + "' style='background-color:white;' frameborder=0></iframe>";
        $("#mTag").html(heading);
        $("#mContent").html(content);
        $("#mImages").html("");
        document.getElementById("myNav").style.width = "100%";
    }
});

function hide(id) {
    $("#" + id).hide();
}

function show(id) {
    $(id).show();
}




function closeNav() {
    document.getElementById("myNav").style.width = "0%";
}