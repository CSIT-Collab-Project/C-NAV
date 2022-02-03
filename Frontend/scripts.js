async function requestDirections(start, end) {
    const url = `/directions-${start}-${end}`;
    let directionsJson = await fetch(url)
        .then(response => response.json());
    return directionsJson;
}

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
        "exit right": "Exit the room to the right",
        "exit stairs left": "Exit the stairs to the left",
        "exit stairs right": "Exit the stairs to the right",
        "exit stairs straight": "Exit the stairs straight ahead"
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
    directionTable(convertedDirections);
    document.getElementById("en-route-ui").style.display = "block";
    currentDirection.innerHTML = convertedDirections[currentDirectionNum];
    nextStepBtn.addEventListener("click", () => {
        currentDirection.innerHTML = convertedDirections[currentDirectionNum + 1];
        currentDirectionNum ++;
    });
    backStepBtn.addEventListener("click", () => {
        currentDirection.innerHTML = convertedDirections[currentDirectionNum - 1];
        currentDirectionNum --;
    });
    return convertedDirections;
}

document.getElementById("location-submit").addEventListener("click", getDirections);


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
    const startZoneCall = zoneColor(start);
    const startZoneColor = startZoneCall[1];
    const endZoneCall = zoneColor(end);
    const endZoneColor = endZoneCall[1];
    const startRoom = document.getElementById("start-id");
    const endRoom = document.getElementById("end-id");
    let remainingSteps = directionList.length - 1;

    // rework zone color thing so it's more clear -- add more variables
    bottomHUD.style.display = "block";
    startRoom.innerHTML = start;
    endRoom.innerHTML = end;
    startRoom.style.background = startZoneColor;
    endRoom.style.background = endZoneColor;
    if (startZoneCall[0] === '3') {
        startRoom.style.color = 'white';
    }
    if (endZoneCall[0] === '3') {
        endRoom.style.color = 'white';
    }

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

function directionTable(directionList) {
    document.getElementById('direction-table').style.display = "block";
    const table = document.getElementById("direction-table");
    let stepNum = 1
    for (item of directionList) {
        const currentStepRow = document.createElement('tr');
        const currentStepCell = document.createElement('td');
        const currentStepNumCell = document.createElement('td');
        const currentStepDirection = document.createTextNode(item);
        const currentStepNum = document.createTextNode(stepNum);
        currentStepNumCell.appendChild(currentStepNum);
        currentStepRow.appendChild(currentStepNumCell);
        currentStepCell.appendChild(currentStepDirection);
        currentStepRow.appendChild(currentStepCell);
        table.appendChild(currentStepRow);
        stepNum ++;
    }
}

function zoneColor(roomNum) {
    const zoneNum = roomNum[1];
    const zoneColors = {
        '3' : '#122aff',
        '2' : '#35e84a',
        '4' : '#6ee4ff',
        '1' : '#e62e2e',
        '5' : '#8f5f25',
        '6' : '#ed890e'
    }
    if (Object.keys(zoneColors).includes(zoneNum)) {
        return [zoneNum, zoneColors[zoneNum]];
    }   
}