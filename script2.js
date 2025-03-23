document.addEventListener("DOMContentLoaded", function () {
    const eventForm = document.getElementById("eventForm");
    const eventsContainer = document.getElementById("eventsContainer");

    eventForm.addEventListener("submit", function (e) {
        e.preventDefault(); 

        const eventName = document.getElementById("title").value.trim();
        const eventDescription = document.getElementById("description").value.trim();
        const eventDate = document.getElementById("date").value;

        if (!eventName || !eventDescription || !eventDate) {
            alert("Please fill all fields!");
            return;
        }

        const eventItem = document.createElement("div");
        eventItem.classList.add("event-item"); 
        eventItem.innerHTML = `
            <h3>${eventName}</h3>
            <p>${eventDescription}</p>
            <small>${new Date(eventDate).toLocaleString()}</small>
            <button class="delete-btn">Delete</button>
        `;

        eventsContainer.appendChild(eventItem);

        eventItem.querySelector(".delete-btn").addEventListener("click", function () {
            eventItem.remove();
        });

        eventForm.reset();
    });
});
