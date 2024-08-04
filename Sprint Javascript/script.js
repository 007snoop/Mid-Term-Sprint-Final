// promise all is used to open multiple files in one code block

Promise.all([fetch("JSON/games.json"), fetch("JSON/person.json")])
	// .then to read the json files
	.then(([gamesResponse, personResponse]) =>
		Promise.all([gamesResponse.json(), personResponse.json()])
	)

	// this .then is now used to manipulate the data from the json files
	.then(([gamesData, personData]) => {
		personData.forEach((person) => {
			const personBox = document.createElement("div");

			personBox.id = "personContainer";
			personBox.innerText = `${person.fName} ${person.lName}`;

			document.body.appendChild(personBox);
		});
        gamesData.forEach((game) => {
            const gameBox = document.createElement("div");

            gameBox.id = "gameContainer";
            gameBox.innerText = `${game.gameName}`;
            
            document.body.appendChild(gameBox);
    })});
