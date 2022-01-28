document.getElementById("location-submit").addEventListener("click", getDirections);

async function getDirections() {
    const currentRoom = document.getElementById("initial-location").value;
    const destination = document.getElementById("destination").value;
    const directions = await requestDirections(currentRoom, destination);
    const directionDisplay = document.getElementById("direction-display");
    const currentDirection = document.getElementById("current-direction");
    const nextStepBtn = document.getElementById("next-direction");
    const backStepBtn = document.getElementById("previous-direction");
    let currentDirectionNum = 0

    directionDisplay.innerHTML = directions;

    // add error handling for if no directions are recieved
    document.getElementById("location-input").style.display = "none";
    bottomBar(currentRoom, destination, directions);
    document.getElementById("en-route-ui").style.display = "block";
    currentDirection.innerHTML = directions[currentDirectionNum];
    nextStepBtn.addEventListener("click", () => {
        currentDirection.innerHTML = directions[currentDirectionNum + 1];
        currentDirectionNum += 1;
    });
    backStepBtn.addEventListener("click", () => {
        currentDirection.innerHTML = directions[currentDirectionNum - 1];
        currentDirectionNum -= 1;
    });
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

function bottomBar(start, end, directionList) {
    const bottomHUD = document.getElementById("bottom-bar");
    const numofSteps = directionList.length - 1;
    const nextStepBtn = document.getElementById("next-direction");
    const backBtn = document.getElementById("previous-direction");
    let remainingSteps = directionList.length - 1;

    bottomHUD.style.display = "block";
    document.getElementById("start-id").innerHTML = start;
    document.getElementById("end-id").innerHTML = end;
    document.getElementById("steps-id").innerHTML = remainingSteps;
   
    nextStepBtn.addEventListener("click", () => {
        remainingSteps -= 1;
        document.getElementById("steps-id").innerHTML = remainingSteps;
        if (remainingSteps === 0) {
            nextStepBtn.style.display = "none";
        }
        if (remainingSteps !== numofSteps) {
            backBtn.style.display = "inline";
        }
    });
    if (remainingSteps > 0) {
        nextStepBtn.style.display = "inline";
    }
    backBtn.addEventListener("click", () => {
        remainingSteps += 1;
        document.getElementById("steps-id").innerHTML = remainingSteps;
        if (remainingSteps > 0) {
            nextStepBtn.style.display = "inline";
        }
        if (remainingSteps === numofSteps) {
            backBtn.style.display = "none";
        }
    });
}