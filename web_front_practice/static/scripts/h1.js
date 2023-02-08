// Ex 1:
const today = new Date();
const yyyy = today.getFullYear();
let mm = today.getMonth() + 1; // Months start at 0!
let dd = today.getDate();


function dateToggle(elem) {
    datePar = document.getElementById('date-par');
    if (elem.innerHTML == 'Show Date') {
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
function changeOpacity(link) {
    const parentDiv = link.parentNode;
    const image = parentDiv.querySelector("img");
    if (image.style.opacity == 1) {
        image.style.opacity = 0;
        link.innerHTML = 'Display Image';
    } else {
        image.style.opacity = 1;
        link.innerHTML = 'Hide Image';
    }
}