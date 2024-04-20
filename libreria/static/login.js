const user = document.getElementById("user");
const pwrd = document.getElementById("password");

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
