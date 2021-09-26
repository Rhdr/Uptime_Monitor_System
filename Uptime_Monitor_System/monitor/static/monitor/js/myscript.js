var a_add = document.querySelector("#a_add")
var a_edit_tbl = document.querySelectorAll("#a_edit_tbl")
var a_delete_tbl = document.querySelectorAll("#a_delete_tbl")
// var a_delete_modal = document.querySelector("#a_delete_modal")

var modal_addedit = new bootstrap.Modal(document.getElementById("btn_add_site"), {});
var modal_delete = new bootstrap.Modal(document.getElementById("btn_delete_site"), {});
var modal_to_open = "NONE";
var delete_pk = -1;


a_add.addEventListener("click", function () {
    modal_to_open = "ADD_EDIT"
    localStorage.setItem("modal_to_open_key", modal_to_open);
    a_add.click()
})

a_edit_tbl.forEach(edit_list_listener);
function edit_list_listener(a_edit) {
    a_edit.addEventListener("click", function () {
        modal_to_open = "ADD_EDIT"
        localStorage.setItem("modal_to_open_key", modal_to_open);
        a_edit.click()
    })
}

a_delete_tbl.forEach(delete_list_listener);
function delete_list_listener(a_delete) {
    a_delete.addEventListener("click", function () {
        modal_to_open = "DELETE"
        localStorage.setItem("modal_to_open_key", modal_to_open);
        // localStorage.setItem("modal_to_open_key", modal_to_open);
        a_delete.click()
    })
}

window.onload = function () {
    var modal_to_open = localStorage.getItem("modal_to_open_key");
    console.log(modal_to_open)

    if (modal_to_open == "ADD_EDIT") {
        modal_addedit.show()
    } else if (modal_to_open == "DELETE") {
        modal_delete.show()
    }

    modal_to_open = "NONE"
    localStorage.setItem("modal_to_open_key", modal_to_open)
};