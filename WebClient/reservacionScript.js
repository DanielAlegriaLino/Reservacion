document.addEventListener("DOMContentLoaded", ()=>{
    fetch(`http://127.0.0.1:8000/RevisarMesas/2023-11-${localStorage.getItem("date")}`)
    .then(response => {
        return response.json()
    })  
    .then(data => {
        reservedTables(data)
        localStorage.clear()
    })
})

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