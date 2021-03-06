$(document).on("click", '.btn_edit', function (event) {
    console.log("edit btn clicked!")
    //get current row & then the unique url
    var current_row = $(this).closest("tr");
    var cell_site_url = current_row.find("td:eq(2)").text();
    // console.log("cell_site_url: " + cell_site_url)

    //get slack accounts & pk
    $.ajax({
        type: 'GET',
        url: "ajax_json/",
        success: function (response) {
            for (var key in response.websites) {
                var obj_site_url = response.websites[key].site_url
                if (cell_site_url == obj_site_url) {
                    // console.log("cell_site_url:" + cell_site_url)
                    // console.log("obj_site_url:" + obj_site_url)
                    pk_website = response.websites[key].pk_website
                    site_name = response.websites[key].site_name
                    site_url = obj_site_url
                    slack_token = response.websites[key].slack_token
                    slack_channel = response.websites[key].slack_channel
                    // console.log("obj_pk_website:" + pk_website)
                    // console.log("obj_slack_token:" + slack_token)
                    // console.log("obj_slack_channel:" + slack_channel)

                    $('#modal_edit_pk_website').val(pk_website)
                    $('#modal_edit_site_name').val(site_name)
                    $('#modal_edit_site_url').val(site_url)
                    $('#modal_edit_slack_token').val(slack_token)
                    $('#modal_edit_slack_channel').val(slack_channel)
                    break;
                }
            }
        },
        error: function (data) {
            console.log("An ajax edit myscript.js error occured");
        }
    });
});


$(document).on("click", '.btn_delete', function (event) {
    console.log("delete btn clicked!")
    //get current row & then the unique url
    var current_row = $(this).closest("tr");
    var cell_site_url = current_row.find("td:eq(2)").text();

    //get pk
    $.ajax({
        type: 'GET',
        url: "ajax_json/",
        success: function (response) {
            for (var key in response.websites) {
                var obj_site_url = response.websites[key].site_url
                // console.log("cell_site_url:" + cell_site_url)
                // console.log("obj_site_url:" + obj_site_url)
                if (cell_site_url == obj_site_url) {
                    pk_website = response.websites[key].pk_website
                    // console.log("delete pk value:" + pk_website)
                    $('#delete_modal_pk_website').val(pk_website)
                    break;
                }
            }
        },
        error: function (data) {
            console.log("An ajax delete myscript.js error occured");
        }
    });
});