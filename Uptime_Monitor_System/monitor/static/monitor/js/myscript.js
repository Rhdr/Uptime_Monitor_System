// $(document).ready(function () {
//     $('.btn_edit').click(function () {
//         var btn_id = this.id; // button ID 
//         var tr_id = $(this).closest('tr').attr('id'); // table row ID 
//         console.log("btn_id")
//         console.log("tr_id")
//     });
// });

$(document).on("click", '#btn_add', function (event) {
    $('#add_edit_modal').val('ADD')
    $('#add_edit_modal_pk_website').val(-1)
    $('#add_edit_modal_site_name').val('')
    $('#add_edit_modal_site_url').val('')
    $('#add_edit_modal_slack_token').val('')
    $('#add_edit_modal_slack_channel').val('')
});

$(document).on("click", '.btn_edit', function (event) {
    // console.log("edit btn clicked!")
    //get current row & then the unique url
    var current_row = $(this).closest("tr");
    var cell_site_url = current_row.find("td:eq(1)").text();
    // console.log("cell_site_url: " + cell_site_url)

    //get slack accounts & pk
    $.ajax({
        type: 'GET',
        url: "ajax_json/",
        success: function (response) {
            for (var key in response.websites) {
                var obj_site_url = response.websites[key].site_url
                if (cell_site_url == obj_site_url) {
                    pk_website = response.websites[key].pk_website
                    site_name = response.websites[key].site_name
                    site_url = obj_site_url
                    slack_token = response.websites[key].slack_token
                    slack_channel = response.websites[key].slack_channel
                    // console.log("obj_pk_website:" + pk_website)
                    // console.log("obj_slack_token:" + slack_token)
                    // console.log("obj_slack_channel:" + slack_channel)

                    $('#add_edit_modal').val('EDIT')
                    $('#add_edit_modal_pk_website').val(pk_website)
                    $('#add_edit_modal_site_name').val(site_name)
                    $('#add_edit_modal_site_url').val(site_url)
                    $('#add_edit_modal_slack_token').val(slack_token)
                    $('#add_edit_modal_slack_channel').val(slack_channel)
                    break;
                }
            }
        },
        error: function (data) {
            console.log("An error occured");
        }
    });

});