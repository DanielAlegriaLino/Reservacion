document.addEventListener("DOMContentLoaded", ()=>{
    fetch(`http://127.0.0.1:8000/RevisarMesas/2023-11-${localStorage.getItem("date")}`)
    .then(response => {
        return response.json();
    })  
    .then(data => {
        reservedTables(data);
    })
    generateRes()

})

function sendRes(key){
    // fetch()
}

function generateRes(){
    const tables = document.getElementsByClassName("table-img");
    for (let i = 0; i < tables.length; i++) {
        tables[i].addEventListener("click", () => {
            localStorage.setItem('table',i)
            fetch(`http://127.0.0.1:8000/GenerarReservacion/2023-11-${localStorage.getItem("date")}`,{
                method:'POST'
            })
            .then(response => {
                return response.text()
            })
            .then(data => {
                localStorage.setItem('key',data)
            })
        }); 
    }
}

function clearLocal(){
    const home = document.querySelector('.navbar-brand');
    home.addEventListener('click', () => {
        localStorage.clear();
    })
}

function reservedTables(arr){
    const tables = document.getElementsByClassName("mesa")
    for(let i = 0; i < tables.length; i++){
        if(arr[i]){
            const table = tables[i].querySelector('.table-img')
            table.removeAttribute('data-bs-target')
            table.removeAttribute('data-bs-toggle')
            table.classList.remove('table-img')
            const text = tables[i].querySelector('.table-state')
            text.classList.remove('text-success')
            text.classList.add('text-danger')
            text.textContent = "Ocupada"
        }
    }
} 

const btn_establecerReservacion = document.getElementById("btn_EstablecerReservacion")
btn_establecerReservacion.addEventListener("click", () => establecerReservacion())
function establecerReservacion(){
    let mesa_reservacion = localStorage.getItem('table')
    let id_reservacion = localStorage.getItem('key')
    let date_reservacion = `2023-11-${localStorage.getItem("date")}`

    //fetch( ) -> hacer fetch y ver si se logro hacer la reservacion, si no retornar false   
    console.log(id_reservacion)
    console.log(date_reservacion)
    console.log(mesa_reservacion)
    console.log(1231234)
    let url =  `http://127.0.0.1:8000/EstablecerReservacion/${date_reservacion}/${id_reservacion}/${mesa_reservacion}`
    alert(url)
    fetch(url)
    .then(response => response.json())
    .then(response => console.log(response))
    location.reload(); 
}
