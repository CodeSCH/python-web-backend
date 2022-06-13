/* PARA ABRIR EL MODAL DELETE*/ 
const oprenModalDelete = document.querySelector(".button-delete");
oprenModalDelete.addEventListener("click", () =>{
    document.querySelector(".content-modal-delete").classList.toggle("open");
})
/* PARA CERRAR EL MODAL DELETE*/ 
const closeModalDelete = document.querySelector(".button-cancelar");
closeModalDelete.addEventListener("click", () =>{
    document.querySelector(".content-modal-delete").classList.toggle("open");
})
/* PARA ABRIR EL MODAL EDIT*/ 
const oprenModalEdit = document.querySelector(".button-edit");
oprenModalEdit.addEventListener("click", () =>{
    document.querySelector(".content-modal-edit").classList.toggle("open");
})
/* PARA CERRAR EL MODAL EDIT*/ 
const closeModalEdit = document.querySelector(".cancel-button");
closeModalEdit.addEventListener("click", () =>{
    document.querySelector(".content-modal-edit").classList.toggle("open");
})

