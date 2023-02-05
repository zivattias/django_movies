console.log("Inside my_script.js");

function showAlert() {
    window.alert("Loaded")
}

function changeHeaderToRed() {
    elem = document.getElementById('my-header')
    elem.style.cssText = 'color: red !important'
}

function switchColor(className) {
    const elems = document.getElementsByClassName(className)
    for (let index = 0; index < elems.length; index++) {
        const elem = elems[index];
        let currClass = null;
        let newClass = null;
        if (elem.classList.contains('btn-primary')) {
            currClass = 'btn-primary'
            newClass = 'btn-danger'
        } else {
            currClass = 'btn-danger'
            newClass = 'btn-primary'
        }
        elem.classList.replace(currClass, newClass);
    }
}