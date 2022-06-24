/**
 * Created by andrew on 5/27/2022.
 */

const displayToyList = (toyList) => {
    var toys = [];
    
    $.each(toyList, function(idx, item) {
        toys.push("<li license=\"" + item.license + "\">" + item.name + "</li>");
    });
    
    $("<ul/>", {
        class: "toyList",
        html: toys.join("")
    }).appendTo("body");
}

const loadToyList = () => {
    $.getJSON( "/toys/data", function( data ) {
        displayToyList(data.toys);
    });
}