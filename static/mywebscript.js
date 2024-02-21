// Function to run addition operation
let runAddition = () => {
    // Get the value of 'num1' input and convert to float
    let num1 = parseFloat(document.getElementById("num1").value);
    // Get the value of 'num2' input and convert to float
    let num2 = parseFloat(document.getElementById("num2").value);

    // Perform addition
    let result = num1 + num2;

    // Display the result in the 'system_response' element
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

// Function to run subtraction operation
let runSubtraction = () => {
    // Get the value of 'num1' input and convert to float
    let num1 = parseFloat(document.getElementById("num1").value);
    // Get the value of 'num2' input and convert to float
    let num2 = parseFloat(document.getElementById("num2").value);

    // Perform subtraction
    let result = num1 - num2;

    // Display the result in the 'system_response' element
    document.getElementById("system_response").innerHTML = "Result: " + result;
};

// Function to run multiplication operation
let runMultiplication = () => {
    // Get the value of 'num1' input and convert to float
    let num1 = parseFloat(document.getElementById("num1").value);
    // Get the value of 'num2' input and convert to float
    let num2 = parseFloat(document.getElementById("num2").value);

    // Perform multiplication
    let result = num1 * num2;

    // Display the result in the 'system_response' element
    document.getElementById("system_response").innerHTML = "Result: " + result;
};
