fetch("JSON/games.json")
	.then(response => response.json())
	.then((data) => {
		console.log(data);
		data.forEach((game) => {
			console.log(game.gameName);
		});
	})

fetch("JSON/person.json")
    .then(response => response.json())
    .then(data => {
        console.log(data);
        data.forEach((person) => {
            console.log(`${person.fName} ${person.lName}`)
        });
    })

