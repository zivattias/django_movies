// Ex 1:
const today = new Date();
const yyyy = today.getFullYear();
let mm = today.getMonth() + 1; // Months start at 0!
let dd = today.getDate();


function dateToggle(elem) {
    if (elem.innerHTML == 'Show Date') {
        const d = new Date();
        datePar = document.getElementById('date-par');
        datePar.style.opacity = 1;
        datePar.innerHTML = dd + '/' + mm + '/' + yyyy;
        elem.innerHTML = 'Hide Date';
    } else {
        elem.innerHTML = 'Show Date'
        datePar.style.opacity = 0;
        datePar.innerHTML = null;
    }
}

// Ex 2:
