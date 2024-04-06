const user = document.getElementById("user");
const pwrd1 = document.getElementById("password_try");
const pwrd2 = document.getElementById("password_except");
const email = document.getElementById("email");

const evento_vacio = function (element) {
  element.addEventListener('blur', () => {
    if (element.value == "") {
      element.style.borderColor = "salmon";
    } else {
      element.style.borderColor = 'black';
    }
  })
}

const minimo = function (element) {
  element.addEventListener('blur', () => {
    if (!elemento.value.length >= 8) {
      element.style.borderColor = 'salmon';
    } else {
      element.style.borderColor = 'blue';
    }
  })
}

const validar_email = function (elemento) {
  elemento.addEventListener('blur', () => {
    const patt_email = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!patt_email.test(elemento.value)) {
      console.log(`Campo '${elemento.name}' invalido.`);
      elemento.style.borderColor = "salmon";
    } else {
      console.log(`Campo '${elemento.name}' valido.`);
      elemento.style.borderColor = 'skyblue';
    }
  })
}


evento_vacio(user);
evento_vacio(pwrd1);
evento_vacio(pwrd2);
evento_vacio(email);
minimo(pwrd1);
validar_email(email);