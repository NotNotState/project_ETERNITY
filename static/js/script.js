//Include general user-input validator
import Validators from './mathOperators.js';

document.getElementById("submitButton").addEventListener("click", submitCalculation);

function validatorFactory(operation, userInput) {
    let calcObj;
    switch(operation) {
        case "standard_deviation":
        case "mean_absolute_deviation":
            calcObj = new Validators.StatisticValidator(operation, userInput);
            break;
        case "gamma_function":
        case "arccos":
            calcObj = new Validators.SingleParamFloatValidator(operation, userInput);
            break;
        case "power_function":
        case "log_function":
            calcObj = new Validators.DoubleParamFloatValidator(operation, userInput);
            break;
        case "exponential_growth"://takes 3 args!
            calcObj = new Validators.ThreeParamFloatValidator(operation, userInput);
            break;
        case "arithmetic_expression":
            calcObj = new Validators.ArithmeticExpressionValidator(operation, userInput);
            break;
        default:
            throw new Error(`Object Assignment Failed for "${operation}" with "${userInput}"`);
    }

    return calcObj;
}

function getCalculationPackage(calculationObject){
    return {
        data_operation : calculationObject.getOperation(),
        data : calculationObject.getData()
    }
}

async function submitCalculation() {
    const operation = document.getElementById("operation").value;
    const dataInput = document.getElementById("data").value;

    if (dataInput == "") {
        document.getElementById("result").textContent = "Please enter some data.";
        console.log(dataInput);
        return;
    }   

    const calcObj = validatorFactory(operation, dataInput); //Raise Error if function not present

    // console.log(calcObj.getData());
    // console.log(typeof calcObj.getData());
    // console.log(calcObj.getOperation());
    // console.log(calcObj.isInputValid());

    const url = "/calculate_call";
    let calcPackage = {};

    if (calcObj.isInputValid()){
        calcPackage = getCalculationPackage(calcObj);
    }else{
        console.log("ERROR NOT VALID");
        document.getElementById("result").textContent = "The data you entered was not in the right format!";
        return;
    }

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(calcPackage),
        });

        // Parse response and display result
        const result = await response.json();
        document.getElementById("result").textContent = result?.calculation_result ?? "A Backend Processing Error Occured";
    } catch (error) {
        document.getElementById("result").textContent = "An error occurred.";
    }


}