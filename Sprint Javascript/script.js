fetch("JSON/person.json")
	.then((response) => {
		if (!response.ok) {
			throw new Error("Did not read JSON");
		}
		return response.json();
	})
	.then((personData) => {
		createPersonDiv();
		personData.forEach((person) => {
			getPersonName(person);
			getAge(person);
			getGamesPlayed(person);
			getHoursPlayed(person);
			getStatus(person);
		});
	})
	.catch((error) => {
		console.error("ISSUE GO FIX:", error);
	});

function createPersonDiv() {
	// creates a div element with the class name of personContainer
	let personbox = document.createElement("div");
	personbox.className = "personContainer";
	document.body.appendChild(personbox);
}

function getPersonName(person) {
	// create the person box first here
	// this is used to get the name of the person from the person json
	let personBoxes = document.getElementsByClassName("personContainer");
	// target last child of div element
	let lastPersonBox = personBoxes[personBoxes.length - 1];
	if (lastPersonBox) {
		lastPersonBox.innerHTML += `
        <p> - ${person.fName} ${person.lName} </p>`;
	}
}

function getAge(person) {
	// this is used to get the age of the person from the person json
	let personBoxes = document.getElementsByClassName("personContainer");
	// target the last child of the personContainer
	let lastPersonBox = personBoxes[personBoxes.length - 1];
	if (lastPersonBox) {
		lastPersonBox.innerHTML += `<p> - Age: ${person.age} </p>
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
        <p> - Hours played: ${person.hoursPlayed} </p>`;
	}
}
