document.addEventListener("DOMContentLoaded", function () {
  let btnBack = document.getElementById('btnBack');
  //if (btnBack) {
    btnBack.addEventListener('click', function () {
      window.history.back();
    });
  //}
});

function toggleMenu() {
  let menu = document.getElementById("menu");
  menu.classList.toggle("hidden");
}
//cerrar el menu al dar click afuera
window.addEventListener('click', function (event) {
  let menu = document.getElementById("menu");
  let btnMenu = document.getElementById("btnMenu");
  if (event.target != menu && event.target != btnMenu) {
    menu.classList.add("hidden")
  }
});