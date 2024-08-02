fetch("Sprint Javascript/JSON/games.json")
    .then(response => response.json())
    .then(data => {
        data.forEach(game => {
            console.log(getGameName(game))
        });
    })
fetch("Sprint Javascript/JSON/person.json")
    .then(response => response.json())
    .then(data => {
        data.forEach(person => {
            console.log(getPersonName(person))
        });
    })


