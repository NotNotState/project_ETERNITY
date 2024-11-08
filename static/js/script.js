//Re-name for each function
//Include general user-input validator

function validateUserInput(input, spec) {
    //process
    //1) check spec == valid operation
    //2) if not valid => HANDLE ERROR (like document.getElementById("result").textContent = "Please enter valid numbers separated by commas.";)
    //3) if ok then 
        // 1) process data based on spec
        // 2) return package wrt processor function
    let data;

    switch(spec) {
        case "standard_deviation":
        case "mean_absolute_deviation":
            data = input
                .split(",")
                .map(item => item.trim()) // Trim extra whitespace
                .filter(item => item !== "")
                .map(Number)
                .filter(value => !isNaN(value)); 
            break;
        case "arc_cosine":
            data = 0
            break;
        case "exponential_growth":
            data = 0
            break;
        case "logarithmic_function":
            data = 0
            break;
        case "sinh":
            data = 0
            break;
        case "power_function":
            data = 0
            break;
        default:
            data = NaN
        }

    if (spec == "mean_absolute_deviation" || spec == "standard_deviation"){
        data = input
            .split(",")
            .map(item => item.trim()) // Trim extra whitespace
            .filter(item => item !== "")
            .map(Number)
            .filter(value => !isNaN(value)); 
    }
    
    //Will return NaN if input doesn't match or failure in conversion ocurred
    return data;    
}

async function submitCalculationV2() {
    const operation = document.getElementById("operation").value;
    const dataInput = document.getElementById("data").value;

    if (isNaN(dataInput)) {
        document.getElementById("result").textContent = "Please enter valid numbers separated by commas.";
        console.log(dataInput)
        return;
    }

    data = validateUserInput(dataInput, operation);

    // Send request to FastAPI based on the selected operation
    // need to move this above the data validation
    let url = "";
    let requestData = {};
    
    //Will add customization for different functions and different inputs
    if (operation === "standard_deviation") {
        url = "/calculate_standard_deviation";
        requestData = { data };
    }

    validateUserInput()

    if ((data.some(isNaN)) || (data.length == 0)) {
        //adjust this to not be std specific
        document.getElementById("result").textContent = "Please enter valid numbers separated by commas.";
        return;
    }
    
}

async function submitCalculation() {
    const operation = document.getElementById("operation").value;
    const dataInput = document.getElementById("data").value; // Reads Array object

    if (isNaN(dataInput)) {
        document.getElementById("result").textContent = "Please enter valid numbers separated by commas.";
        console.log(dataInput)
        return;
    }

    console.log(typeof dataInput);
    
    // Parse the comma-separated input into an array of numbers
    //const data = dataInput.split(",").map(Number);
    const data = dataInput
        .split(",")
        .map(item => item.trim()) // Trim extra whitespace
        .filter(item => item !== "")
        .map(Number)
        .filter(value => !isNaN(value));          // Convert to number

    // Make sure the data is a valid array of numbers
    if ((data.some(isNaN)) || (data.length == 0)) {
        document.getElementById("result").textContent = "Please enter valid numbers separated by commas.";
        return;
    }

    // Send request to FastAPI based on the selected operation
    // need to move this above the data validation
    let url = "";
    let requestData = {};


    //Will add customization for different functions and different inputs
    if (operation === "standard_deviation") {
        url = "/calculate_standard_deviation";
        requestData = { data };
    }

    try {
        console.log(data);
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(requestData),
        });

        // Parse response and display result
        const result = await response.json();
        document.getElementById("result").textContent = result?.standard_deviation ?? "Error";
        //document.getElementById("result").textContent = result.standard_deviation || console.log(data);
    } catch (error) {
        document.getElementById("result").textContent = "An error occurred.";
    }
    
}