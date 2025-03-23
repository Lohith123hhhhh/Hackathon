const API_URL = "http://localhost:8000";

const sampleEvents = [
    {
        id: 1,
        title: "Sample1",
        description: "This is a sample event 1.",
        date: new Date().toISOString(),
    },
    {
        id: 2,
        title: "Sample2",
        description: "This is a sample event 2.",
        date: new Date().toISOString(),
    }
];

async function loadEvents(category) {
    const container = document.getElementById('eventDetails');
    container.innerHTML = "";

    const events = sampleEvents;

    if (events.length === 0) {
        container.innerHTML = `<p>No live events available.</p>`;
        return;
    }

    events.forEach(event => {
        const card = document.createElement('div');
        card.classList.add('event-card');
        card.innerHTML = `
            <h3>${event.title}</h3>
            <p>${event.description}</p>
            <p><strong>Date:</strong> ${new Date(event.date).toLocaleString()}</p>
            <button onclick="openFeedbackForm(${event.id}, '${event.title}')">Give Feedback</button>
        `;
        container.appendChild(card);
    });
}

function openFeedbackForm(eventId, eventTitle) {
    const container = document.getElementById('eventDetails');
    container.innerHTML = `
        <h2>Feedback for ${eventTitle}</h2>
        <form id="feedbackForm">
            <label for="comment">Your Comment:</label>
            <textarea id="comment" rows="4" placeholder="Write your review..."></textarea>

            <label for="rating">Rate the Event (1-5):</label>
            <select id="rating">
                <option value="1">1 - Poor</option>
                <option value="2">2 - Fair</option>
                <option value="3">3 - Good</option>
                <option value="4">4 - Very Good</option>
                <option value="5">5 - Excellent</option>
            </select>

            <label for="imageUpload">Upload an Image:</label>
            <input type="file" id="imageUpload" accept="image/*">

            <button type="submit">Submit Feedback</button>
        </form>
    `;

    document.getElementById("feedbackForm").addEventListener("submit", function(event) {
        event.preventDefault();
        const comment = document.getElementById("comment").value;
        const rating = document.getElementById("rating").value;
        const imageFile = document.getElementById("imageUpload").files[0];

        console.log("Feedback Submitted:");
        console.log("Event:", eventTitle);
        console.log("Comment:", comment);
        console.log("Rating:", rating);
        if (imageFile) {
            console.log("Image Uploaded:", imageFile.name);
        } else {
            console.log("No Image Uploaded.");
        }

        alert("Feedback Submitted Successfully!");
        loadEvents('live'); 
    });
}

document.addEventListener("DOMContentLoaded", () => loadEvents('live'));
