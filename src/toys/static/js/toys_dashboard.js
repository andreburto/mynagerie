/**
 * Created by andrew on 5/27/2022.
 */

const tableId = "#toyList";
const divId = "#toyContent";

const makeHeader = () => {
    //noinspection JSAnnotator
    return [
        $("<tr>").append($("<th>", {colspan: 3, id: "tableTitle"}).text("TOYS")),
        $("<tr>").append($("<th>").text("NAME"), $("<th>").text("LICENSE"), $("<th>").text("LINE"))
    ];
};

const displayToyList = (toyList) => {
    var rows = makeHeader();
    
    $.each(toyList, function(idx, item) {
        rows.push($("<tr>").append(
            $("<td>").text(item.name), $("<td>").text(item.license), $("<td>").text(item.line)
        ));
    });

    $("<table>", {class: "toyList", id: "toyList"}).appendTo(divId);

    $.each(rows, function (idx, item) {
        $(tableId).append(item);
    });
};

const centerDisplay = () => {
    var top = Math.floor($(window).height() - $(tableId).outerHeight()) / 2;
    var left = Math.floor($(window).width() - $(tableId).outerWidth()) / 2;
    $(divId).css({position:"absolute", margin:0, top: (top>0?top:0)+"px", left: (left>0?left:0)+"px"});
};

const loadToyList = (data_url) => {
    $("<div>", {id: "toyContent"}).appendTo("body");
    $.getJSON(data_url, function( data ) {
        displayToyList(data.toys);
        centerDisplay();
    });
}
