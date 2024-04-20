const user = document.getElementById("id_username");
const pwrd = document.getElementById("id_password");

const evento_vacio = function (element) {
  element.addEventListener('blur', () => {
    if (element.value == "") {
      element.style.borderColor = 'salmon';
    } else {
      element.style.borderColor = 'skyblue';
    }
  })
}

const minLength = function(element) {
  element.addEventListener('blur',() => {
    if (element.value.length < 8) {
      element.style.borderColor = 'salmon';
    } else {
      element.style.borderColor = 'skyblue';
    } 
  })
} 

evento_vacio(user);
evento_vacio(pwrd);
minLength(pwrd);
