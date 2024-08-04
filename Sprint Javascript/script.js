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

        const peopleContainer = document.createElement("div");
        peopleContainer.id = "people";

        console.log(data);

        data.forEach((person) => {
            const personItem = document.createElement("li");
            personItem.textContent = `${person.fName} ${person.lName}`

            peopleContainer.appendChild(personItem);

   
        });
        document.body.appendChild(peopleContainer);
    })

