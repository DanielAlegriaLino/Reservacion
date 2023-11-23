document.addEventListener("DOMContentLoaded", ()=>{
    let states = [false,true,true,false,true]
    reservedTables(states)
})

function reservedTables(arr){
    const tables = document.getElementsByClassName("mesa")
    for(let i = 0; i < arr.length; i++){
        if(arr[i]){
            const table = tables[i].querySelector('.table-img')
            table.removeAttribute('data-bs-target')
            table.classList.remove('table-img')
            const text = tables[i].querySelector('.table-state')
            text.classList.remove('text-success')
            text.classList.add('text-danger')
            text.textContent = "Ocupada"
        }
    }
} 