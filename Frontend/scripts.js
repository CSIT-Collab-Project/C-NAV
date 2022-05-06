async function requestDirections(start, end) {
    const url = `/directions-${start}-${end}`;
    let directionsJson = await fetch(url)
        .then(response => response.json());
    return directionsJson;
}

window.addEventListener("load", aprilFools);
function aprilFools() {
    const date = new Date();
    if (date.getMonth() === 4 && date.getDay() === 1) {
        document.body.style.fontFamily = "Comic Sans MS";
    }
}

function goHome() {
    window.location = "/";
}

async function getDirections() {
    document.getElementById("main-ui").style.display = "block";
    const currentRoom = document.getElementById("initial-location").value;
    const destination = document.getElementById("destination").value;
    const initialDirections = await requestDirections(currentRoom, destination);
    const directionDict = {
        "left": ["Turn left at the next intersection", "turn-left"],
        "right": ["Turn right at the next intersection", "turn-right"],
        "continue straight": ["Continue straight through the next intersection", "straight-arrow"],
        "room door is on the left": ["Room door is on the left", "left-arrow"],
        "room door is on the right": ["Room door is on the right", "right-arrow"],
        "room door is straight ahead": ["Room door is straight ahead", "straight-arrow"],
        "enter stairs straight ahead": ["Enter stairs straight ahead", "straight-arrow"],
        "enter stairs on right": ["Enter stairs on right", "right-arrow"],
        "enter stairs on left": ["Enter stairs on left", "left-arrow"],
        "exit left": ["Exit the room to the left", "curve-left"],
        "exit right": ["Exit the room to the right", "curve-right"],
        "exit stairs left": ["Exit the stairs to the left", "curve-left"],
        "exit stairs right": ["Exit the stairs to the right", "curve-right"],
        "exit stairs straight": ["Exit the stairs straight ahead", "straight-arrow"],
        "go up 1 floor": ["Go up one floor", " "],
        "go down 1 floor": ["Go down one floor", " "],
        "go up 2 floors": ["Go up two floors", " "],
        "go down 2 floors": ["Go down two floors", " "],
        "go up 3 floors": ["Go up three floors", " "],
        "go down 3 floors": ["Go down three floors", " "],
        "go up 4 floors": ["Go up four floors", " "],
        "go down 4 floors": ["Go down four floors", " "],
        "enter doors in stairwell": ["Enter doors in stairwell", " "],
        "through doors to left" : ["Through doors to the left", " "],
        "through doors to right" : ["Through doors to the right"]
    }
    const currentDirection = document.getElementById("current-direction");
    const nextStepBtn = document.getElementById("next-direction");
    const backStepBtn = document.getElementById("previous-direction");
    const currentIcon = document.getElementById("current-icon");
    const currentMap = document.getElementById("current-map");
    const directionKeys = Object.keys(directionDict);
    let convertedDirections = [];
    let currentDirectionNum = 0;
    let currentFloorNum = parseInt(currentRoom[0]);

    for (item of initialDirections) {
        if (directionKeys.includes(item)) {
            convertedDirections.push(directionDict[item]);
        }
        else {
            convertedDirections.push(item);
        }
    }
    let currentDirectionText = convertedDirections[currentDirectionNum][0];
    // add error handling for if no directions are recieved
    document.getElementById("location-input").style.display = "none";
    bottomBar(currentRoom, destination, convertedDirections);
    directionTable(convertedDirections);
    document.getElementById("en-route-ui").style.display = "block";

    currentDirection.innerHTML = currentDirectionText;
    let icon = convertedDirections[currentDirectionNum][1];
    currentIcon.src = `/icon-${icon}`;
    currentMap.src = `/map${currentFloorNum}`;
    let stepCount = 1;
    let stepCountNode = document.createTextNode(` (${stepCount} of ${convertedDirections.length})`);
    currentDirection.appendChild(stepCountNode);

    nextStepBtn.addEventListener("click", () => {
        stepCount ++;
        currentDirectionNum ++;
        currentDirectionText = convertedDirections[currentDirectionNum][0];
        currentDirection.innerHTML = currentDirectionText;
        stepCountNode = document.createTextNode(` (${stepCount} of ${convertedDirections.length})`);
        currentDirection.appendChild(stepCountNode);
        let icon = convertedDirections[currentDirectionNum][1];
        currentIcon.src = `/icon-${icon}`;
        // FIX ISSUE WITH FLOORS AND MAPS - only goes up by one floor rn, needs to adjust the map based on how many floors you're going up
        if (currentDirectionText.includes("Go up")) {
            if (currentDirectionText.includes("two")) {
                currentFloorNum += 2;
            }
            else if (currentDirectionText.includes("three")) {
                currentFloorNum += 3;
            }
            else if (currentDirectionText.includes("four")) {
                currentFloorNum += 4;
            }
            else {
                currentFloorNum++;
            }
            currentMap.src = `/map${currentFloorNum}`;
        }
        else if ((currentDirectionText.includes("Go down"))) {
            if (currentDirectionText.includes("two")) {
                currentFloorNum -= 2;
            }
            else if (currentDirectionText.includes("three")) {
                currentFloorNum -= 3;
            }
            else if (currentDirectionText.includes("four")) {
                currentFloorNum -= 4;
            }
            else {
                currentFloorNum--;
            }
            currentMap.src = `/map${currentFloorNum}`;
        }
    });

    backStepBtn.addEventListener("click", () => {
        if (currentDirectionText.includes("Go up")) {
            if (currentDirectionText.includes("two")) {
                currentFloorNum -= 2;
                console.log(currentFloorNum);
            }
            else if (currentDirectionText.includes("three")) {
                currentFloorNum -= 3;
            }
            else if (currentDirectionText.includes("four")) {
                currentFloorNum -= 4;
            }
            else {
                currentFloorNum--;
            }
            currentMap.src = `/map${currentFloorNum}`;
        }
        else if ((currentDirectionText.includes("Go down"))) {
            if (currentDirectionText.includes("two")) {
                currentFloorNum += 2;
            }
            else if (currentDirectionText.includes("three")) {
                currentFloorNum += 3;
            }
            else if (currentDirectionText.includes("four")) {
                currentFloorNum += 4;
            }
            else {
                currentFloorNum++;
            }
            currentMap.src = `/map${currentFloorNum}`;
        }
        stepCount--;
        currentDirectionNum --;
        currentDirectionText = convertedDirections[currentDirectionNum][0]
        currentDirection.innerHTML = currentDirectionText;
        stepCountNode = document.createTextNode(` (${stepCount} of ${convertedDirections.length})`);
        currentDirection.appendChild(stepCountNode);
        let icon = convertedDirections[currentDirectionNum][1];
        currentIcon.src = `/icon-${icon}`;
    });
    return convertedDirections;
}

const submitBtn = document.getElementById("location-submit")
submitBtn.addEventListener("click", submitDirections);

function submitDirections() {
    submitBtn.removeEventListener("click", submitDirections);
    getDirections();
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
    const startZoneCall = zoneColor(start);
    const startZoneColor = startZoneCall[1];
    const endZoneCall = zoneColor(end);
    const endZoneColor = endZoneCall[1];
    const startRoom = document.getElementById("start-id");
    const endRoom = document.getElementById("end-id");
    const dirTableElement = document.getElementById('direction-table');
    const tableBtn = document.getElementById("table-btn");
    let remainingSteps = directionList.length - 1;

    // rework zone color thing so it's more clear -- add more variables
    bottomHUD.style.display = "block";
    startRoom.innerHTML = start;
    endRoom.innerHTML = end;
    startRoom.style.background = startZoneColor;
    endRoom.style.background = endZoneColor;
    if (startZoneCall[0] === '3' || startZoneCall[0] === '1' || startZoneCall[0] === '5') {
        startRoom.style.color = 'white';
    }
    if (endZoneCall[0] === '3' || endZoneCall[0] === '1' || endZoneCall[0] === '5') {
        endRoom.style.color = 'white';
    }
    else {
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
    let tableShows = false;
    tableBtn.addEventListener("click", () => {
        if (!tableShows) {
            dirTableElement.style.display = 'block';
            tableShows = true;
        }
        else if (tableShows) {
            dirTableElement.style.display = 'none';
            tableShows = false;
        }
    });
}

function directionTable(directionList) {
    const table = document.getElementById("direction-table");
    // creates table with directions and icons that correspond
    for (item of directionList) {
        const currentStepRow = document.createElement('tr');
        const currentStepCell = document.createElement('td');
        const currentIconCell = document.createElement('td');
        const currentStepDirection = document.createTextNode(item[0]);
        const currentIcon = document.createElement('img');
        currentIcon.setAttribute('src', `/icon-${item[1]}`);
        currentIconCell.appendChild(currentIcon);
        currentStepRow.appendChild(currentIconCell);
        currentStepCell.appendChild(currentStepDirection);
        currentStepRow.appendChild(currentStepCell);
        table.appendChild(currentStepRow);
    }
}

function zoneColor(roomNum) {
    const zoneNum = roomNum[1];
    const zoneColors = {
        '3' : '#1e4275',
        '2' : '#1e7b1b',
        '4' : '#5673ab',
        '1' : '#681c1c',
        '5' : '#8f5f25',
        '6' : '#ed890e'
    }
    if (Object.keys(zoneColors).includes(zoneNum)) {
        return [zoneNum, zoneColors[zoneNum]];
    }   
}