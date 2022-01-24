document.getElementById("location-submit").addEventListener("click", getDirections);

async function getDirections() {
    const currentRoom = document.getElementById("initial-location").value;
    const destination = document.getElementById("destination").value;
    const directions = await requestDirections(currentRoom, destination);
    const directionDisplay = document.getElementById("direction-display");
    directionDisplay.innerHTML = directions;
    return directions;
}


async function requestDirections(start, end) {
    const url = `/directions-${start}-${end}`;
    let directionsJson = await fetch(url)
        .then(response => response.json());
    return directionsJson;
}

const destinationForm = document.getElementById("destination-form");
const nextBtn = document.getElementById("next");
destinationForm.style.display = "none";
nextBtn.addEventListener("click", () => {
    destinationForm.style.display = "block";
    nextBtn.style.display = "none";
});

