document.getElementById("location-submit").addEventListener("click", getDirections);

async function getDirections() {
    const currentRoom = document.getElementById("initial-location").value;
    const destination = document.getElementById("destination").value;
    const initialDirections = await requestDirections(currentRoom, destination);
    const directionDict = {
        "left": "Turn left at the next intersection",
        "right": "Turn right at the next intersection",
        "continue straight": "Continue straight through the next intersection",
        "room door is on the left": "Room door is on the left",
        "room door is on the right": "Room door is on the right",
        "room door is straight ahead": "Room door is straight ahead",
        "enter stairs straight ahead": "Enter stairs straight ahead",
        "enter stairs on right": "Enter stairs on right",
        "enter stairs on left": "Enter stairs on left",
        "exit left": "Exit the room to the left",
        "exit right": "Exit the room to the right"
    }
    const directionDisplay = document.getElementById("direction-display");
    const currentDirection = document.getElementById("current-direction");
    const nextStepBtn = document.getElementById("next-direction");
    const backStepBtn = document.getElementById("previous-direction");
    let convertedDirections = []
    let currentDirectionNum = 0
    const directionKeys = Object.keys(directionDict);

    for (item of initialDirections) {
        if (directionKeys.includes(item)) {
            convertedDirections.push(directionDict[item]);
        }
        else {
            convertedDirections.push(item);
        }
    }

    // directionDisplay.innerHTML = convertedDirections;

    // add error handling for if no directions are recieved
    document.getElementById("location-input").style.display = "none";
    bottomBar(currentRoom, destination, convertedDirections);
    document.getElementById("en-route-ui").style.display = "block";
    currentDirection.innerHTML = convertedDirections[currentDirectionNum];
    nextStepBtn.addEventListener("click", () => {
        currentDirection.innerHTML = convertedDirections[currentDirectionNum + 1];
        currentDirectionNum += 1;
    });
    backStepBtn.addEventListener("click", () => {
        currentDirection.innerHTML = convertedDirections[currentDirectionNum - 1];
        currentDirectionNum -= 1;
    });
    return convertedDirections;
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

    // rework zone color thing so it's more clear -- add more variables
    bottomHUD.style.display = "block";
    document.getElementById("start-id").innerHTML = start;
    const startZoneColor = zoneColor(start);
    document.getElementById("start-id").style.color = startZoneColor;
    const endZoneColor = zoneColor(end);
    document.getElementById("end-id").innerHTML = end;
    document.getElementById("end-id").style.color = endZoneColor;
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

function zoneColor(roomNum) {
    const zoneNum = roomNum[1];
    if (zoneNum === '3') {
        return "#122aff";
    }
    else if (zoneNum === '2') {
        return "#35e84a";
    }
    else if (zoneNum === '4') {
        return "#6ee4ff";
    }
    else if (zoneNum === '1') {
        return "#e62e2e";
    }
    
}