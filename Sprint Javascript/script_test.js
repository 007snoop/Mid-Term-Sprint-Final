// promise all is used to open multiple files in one code block

Promise.all([fetch("JSON/games.json"), fetch("JSON/person.json")])
	// .then to read the json files
	.then(([gamesResponse, personResponse]) =>
		Promise.all([gamesResponse.json(), personResponse.json()])
	)

	// this .then is now used to manipulate the data from the json files
	// this will be populated with functions that will be called
	.then(([gamesData, personData]) => {
		personData.forEach((person) => {
            createPersonDiv()
			getPersonName(person);
			getAge(person);
			getGamesPlayed(person);
            getStatus(person);
            getHoursPlayed(person);
		});

		gamesData.forEach((game) => {
            game = game.gameName;
		});



        let gameBox = document.createElement("div");
        gameBox.className = "gameContainer";
        document.body.appendChild(gameBox);
        getGameName();

	});

function createPersonDiv() {
    // creates a div element with the name of personContainer
    let personbox = document.createElement('div');
    personbox.className = "personContainer"
    document.body.appendChild(personbox)
}

function getPersonName(person) { // create the person box first here
	// this is used to get the name of the person from the person json
    let personBoxes = document.getElementsByClassName("personContainer");
    // target last child of div element
    let lastPersonBox = personBoxes[personBoxes.length - 1];
    if (lastPersonBox) {
        lastPersonBox.innerHTML += `
        <p> - ${person.fName} ${person.lName}`
    }
}

function getAge(person) {
	// this is used to get the age of the person from the person json
	let personBoxes = document.getElementsByClassName("personContainer");
	// target the last child of the personContainer
	let lastPersonBox = personBoxes[personBoxes.length - 1];
	if (lastPersonBox) {
		lastPersonBox.innerText += ` - Age: ${person.age}
        `;
	}
}

function getGamesPlayed(person) {
	// this is used to get the games played by the person json
	let personBoxes = document.getElementsByClassName("personContainer");
	// again, target the last child of the personContainer
	let lastPersonBox = personBoxes[personBoxes.length - 1];
	if (lastPersonBox) {
		lastPersonBox.innerHTML += `
        <p> - Games played: ${person.gamesPlayed} </p>
        `;
	}
}

function getStatus(person) {
    // this is used to get the status of the person json relationship
    let personBoxes = document.getElementsByClassName("personContainer");
    // again, target the last child of the personContainer
    let lastPersonBox = personBoxes[personBoxes.length - 1];
    if (lastPersonBox) {
        lastPersonBox.innerHTML += `
        <p> - Status: ${person.status} </p>
        `;
    }
}

function getHoursPlayed(person) {
    // this is used to get the hours played for the games in the person json
    let personBoxes = document.getElementsByClassName("personContainer");
    // target the last child of the personContainer
    let lastPersonBox = personBoxes[personBoxes.length - 1];

    if (lastPersonBox) {
        lastPersonBox.innerHTML += `
        <p> - Hours played: ${person.hoursPlayed} </p>`
    };
}



function getGameName(game) {
    let gameBox = document.getElementsByClassName("gameContainer");
    let lastGameBox = gameBox[gameBox.length - 1];
    if (lastGameBox) {
        lastGameBox.innerHTML += `
        <h3> ${game.gameName} </h3>`
    }
}

function getGameType(game) {}

function getNumPlayer(game) {}

function getPlatform(game) {}
