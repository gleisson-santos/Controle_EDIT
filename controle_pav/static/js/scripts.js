const btn = document.querySelector("#show"); /* Buttton */
const container2 = document.querySelector(".alert-success");

btn.addEventListener("click", function() {
    
    if(container2.style.display === 'block') {
        container2.style.display = 'none';
    } else {
        container2.style.display = 'block';
    }
    
    setTimeout(fechar,  4000) 
    
    // console.log('Fui clicado!!');
});

function fechar () {
    container2.style.display = 'none';
}


