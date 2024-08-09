# JavaScript Sprint

## Overview

This project fetches JSON data from a local file (`person.json`) and displays information about people on a web page. The data includes names, ages, games played, hours played, and status. The application dynamically creates and appends HTML elements to show this information in a styled format.

## Files

- **`index.html`**: The main HTML file for your project.
- **`styles.css`**: The CSS file to style the HTML elements.
- **`script.js`**: The JavaScript file that handles fetching data and manipulating the DOM.
- **`person.json`**: The JSON file containing the data about people.

1. **Open `index.html`**

   Open `index.html` in your browser to view the project in action. Ensure that the JSON file (`person.json`) is in the correct directory (`JSON/person.json`).

## How It Works

1. **Fetch Data**: The `script.js` file uses the Fetch API to request `person.json`.
2. **Parse JSON**: The JSON data is parsed into JavaScript objects.
3. **Create Elements**: For each person in the data, a new `div` element is created and appended to the document body.
4. **Display Data**: Additional details about each person (name, age, games played, hours played, status) are appended to the respective `div` elements.
