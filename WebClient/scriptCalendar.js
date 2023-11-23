document.addEventListener("DOMContentLoaded", function() {
    const calendarBody = document.getElementById("calendar-body");

    const maxDays = 31;
    const rows = Math.ceil(maxDays / 7);

    for (let row = 0; row < rows; row++) {
        const tr = document.createElement("tr");

        for (let col = 0; col < 7; col++) {
            const dayNumber = row * 7 + col + 1;

            if (dayNumber <= maxDays) {
                const button = document.createElement("button");
                button.className = "btn btn-outline-secondary calendar-btn";
                button.textContent = dayNumber;

                button.addEventListener("click", function() {
                    window.location.href = "reservacion.html";
                });

                const td = document.createElement("td");
                td.appendChild(button);
                tr.appendChild(td);
            } else {
                tr.appendChild(document.createElement("td"));
            }
        }

        calendarBody.appendChild(tr);
    }
});
