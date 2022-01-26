document.getElementById("location-submit").addEventListener("click", getDirections);

async function getDirections() {
    const currentRoom = document.getElementById("initial-location").value;
    const destination = document.getElementById("destination").value;
    const directions = await requestDirections(currentRoom, destination);
    const directionDisplay = document.getElementById("direction-display");
    directionDisplay.innerHTML = directions;
    // add error handling for if no directions are recieved
    document.getElementById("location-input").style.display = "none";
    bottomBar(currentRoom, destination, directions);
    mainUI();
    return directions;
}


async function requestDirections(start, end) {
    const url = `/directions-${start}-${end}`;
    let directionsJson = await fetch(url)
        .then(response => response.json());
    return directionsJson;
}

async function mainUI() {
    // rework to use request already made, no need to make another request for the same thing
    const directionList = await getDirections();
    const directionDisplay = document.getElementById("current-direction");
    document.getElementById("en-route-ui").style.display = "block";
    directionDisplay.innerHTML = directionList[0];
}

const destinationForm = document.getElementById("destination-form");
const nextBtn = document.getElementById("next");
destinationForm.style.display = "none";
nextBtn.addEventListener("click", () => {
    destinationForm.style.display = "block";
    nextBtn.style.display = "none";
});

function bottomBar(start, end, directionList) {
   const bottomHUD = document.getElementById("bottom-bar");
   bottomHUD.style.display = "block";
   document.getElementById("start-id").innerHTML = start;
   document.getElementById("end-id").innerHTML = end;
   const remainingSteps = directionList.length;
   document.getElementById("steps-id").innerHTML = remainingSteps;
}