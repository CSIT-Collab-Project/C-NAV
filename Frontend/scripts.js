const directionList = document.getElementById("location-submit").addEventListener("click", () => {
    const currentRoom = document.getElementById("initial-location").value;
    const destination = document.getElementById("destination").value;
    const directions = requestDirections (currentRoom, destination);
    const directionDisplay = document.getElementById("direction-display");
    directionDisplay.innerHTML = directions;
}
);


async function requestDirections (start, end) {
    const url = `/directions-${start}-${end}`;
    let directionsJson = await fetch(url);
    console.log(directionsJson);
    directionsJson = "hello world";
    return directionsJson;
}