function createUserTable(tableId, users) {
    // console.log(users.length)
    $('#' + tableId).empty();
    for (i = 0; i < users.length; i++) {

        markup = '<tr>' +
            '<th scope="row">' + parseInt(i + 1) + '</th>' +
            '<td>' + users[i].name + '</td>' +
            '<td><i class="fas fa-edit blue-text"></i> &ensp; <i class="fas fa-trash pink-text"></i>' +
            '</td>' +
            '<td> <a href="">See Details</a> </td>' + '</tr>';
        $('#' + tableId).append(markup);
        console.log(markup)
    }

}

function getUsersAjax(dbName, tableId) {
    var currdbName = dbName;
    var currTableID = tableId;
    $.ajax({
        type: "POST",
        url: "/ajaxGetUsers",
        dataType: 'json',
        data: {
            'lol': 34,
            'dbName': JSON.stringify(currdbName),
            access_token: $("#access_token").val()
        },

        success: function (result) {
            console.log("Success is Reached")
            users = JSON.parse(JSON.parse(result.users))
            createUserTable(currTableID, users);
        },
        error: function (result) {
            alert('Internal Server Error 😐, Please Reload & Try Again!!!');
        },
        complete: function () {
            // console.log("Ajax Request Completetd");

        }
    });
}

function cardUpdate(i) {
    if (i == 1) {
        var dbName = $('#chosen_db_1').val();
        $('#connected_1').text(dbName);
        getUsersAjax(dbName, 'card1body');
    } else if (i == 2) {
        var dbName = $('#chosen_db_2').val();
        $('#connected_2').text(dbName);
        getUsersAjax(dbName, 'card2body');
    }

}

$(document).ready(function () {
    $('#connected_1').text($('#chosen_db_1').val());
    $('#connected_2').text($('#chosen_db_2').val());
    cardUpdate(1);
    setTimeout(function(){ cardUpdate(2); }, 200);
    // cardUpdate(2);

    $('#chosen_db_1').on('change', function () {
        cardUpdate(1);
    });

    $('#chosen_db_2').on('change', function () {
        cardUpdate(2);
    });

});