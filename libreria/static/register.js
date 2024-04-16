const firstName = document.getElementById("id_first_name");
const lastName = document.getElementById("id_last_name");
const user = document.getElementById("id_user_name");
const pwrd = document.getElementById("id_password");
const email = document.getElementById("id_email");

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
    if (!element.value.length >= 8) {
      element.style.borderColor = 'salmon';
    } else {
      element.style.borderColor = 'blue';
    }
  })
}

const validar_email = function (element) {
  element.addEventListener('blur', () => {
    const patt_email = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!patt_email.test(element.value)) {
      console.log(`Campo '${element.name}' invalido.`);
      element.style.borderColor = "salmon";
    } else {
      console.log(`Campo '${element.name}' valido.`);
      element.style.borderColor = 'skyblue';
    }
  })
}


evento_vacio(firstName);
evento_vacio(lastName);
evento_vacio(user);
evento_vacio(pwrd);
evento_vacio(email)
minimo(pwrd);
validar_email(email);