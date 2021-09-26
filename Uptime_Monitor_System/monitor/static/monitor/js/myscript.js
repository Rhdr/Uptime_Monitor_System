var a_add = document.querySelector("#a_add")
var a_edit = document.querySelector("#a_edit")
var a_delete = document.querySelector("#a_delete")

var modal_addedit = new bootstrap.Modal(document.getElementById("btn_add_site"), {});
var modal_delete = new bootstrap.Modal(document.getElementById("btn_delete_site"), {});
var modal_to_open = "NONE";


a_add.addEventListener("click", function () {
    modal_to_open = "ADD_EDIT"
    localStorage.setItem("modal_to_open_key", modal_to_open);
    a_add.click()
})

a_edit.addEventListener("click", function () {
    modal_to_open = "ADD_EDIT"
    localStorage.setItem("modal_to_open_key", modal_to_open);
    a_edit.click()
})

a_delete.addEventListener("click", function () {
    modal_to_open = "DELETE"
    localStorage.setItem("modal_to_open_key", modal_to_open);
    a_delete.click()
})

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