/*
IDEA: 
-- Add one singular switch to assign calc object
-- Calc objects will perform simple userInput checks
-- Pass object (if valid) to PostCalculation class
    -- will perform final checks
    -- send and await post

2nd :: Have logger class for history
*/

class OperatorInterface {
    constructor(operation, userInput) {
        if (this.constructor === OperatorInterface) {
            throw new Error("Cannot instantiate abstract class OperationInterface");
        }
        this.operation = operation;
        this.userInput = userInput;
    }

    processInput() {
        throw new Error("Method 'processInput()' must be implemented.");
    }

    // Another abstract method (optional)
    isInputValid() {
        throw new Error("Method 'isInputValid()' must be implemented.");
    }

    getData(){
        return this.data;
    }

    getOperation(){
        return this.operation;
    }
}

 class StatisticValidator extends OperatorInterface {
    constructor(operation, userInput){

        super(operation, userInput);
        this.data = this.processInput();
        console.log(`"${this.operation}" validator object sucessfully constructed with params: 
                        Data : "${this.data}", 
                        Validity : "${this.isInputValid()}"`)

    }

    //returns list of number types
    //Private not supported in older versions of JS
    processInput() {
        return this.userInput.split(",")
                        .map(item => item.trim())
                        .filter(item => item !== "")
                        .map(Number)
                        .filter(value => !isNaN(value));
    }

    //checks that list is not empty or contains null values
    isInputValid(){
        return !(this.data.some(isNaN) || this.data.length == 0);
    }
    
}

class SingleParamFloatValidator extends OperatorInterface {
    constructor(operation, userInput){

        super(operation, userInput);
        this.data = this.processInput();
        console.log(`"${this.operation}" validator object sucessfully constructed with params: 
                        Data : "${this.data}", 
                        Validity : "${this.isInputValid()}"`)

    }

    //returns list of number types
    //Private not supported in older versions of JS
    processInput() {
        return Number(this.userInput.trim());
    }

    //checks that list is not empty or contains null values
    isInputValid(){

        return !(isNaN(this.data));

    }

}

class DoubleParamFloatValidator extends OperatorInterface {
    constructor(operation, userInput){

        super(operation, userInput);
        this.data = this.processInput();
        console.log(`"${this.operation}" validator object sucessfully constructed with params: 
                        Data : "${this.data}", 
                        Validity : "${this.isInputValid()}"`)

    }

    //returns list of number types
    //Private not supported in older versions of JS
    processInput() {
        return this.userInput.split(",")
                        .map(item => item.trim())
                        .filter(item => item !== "")
                        .map(Number);
    }

    //checks that list is not empty or contains null values
    isInputValid(){
        if (this.operation === "log_function"){
            console.log(`Evaluating data for logarithmic function, data : "${this.data}"`);
            return !( this.data.some(isNaN) || this.data[1] <= 0 || (this.data.length != 2));       
        }
        //return !((this.data.some(isNaN)) || (this.data.length != 2) || (this.data[0] < 0));
        return !((this.data.some(isNaN)) || (this.data.length != 2));
    }

}

class ThreeParamFloatValidator extends OperatorInterface {

    constructor(operation, userInput){

        super(operation, userInput);
        this.data = this.processInput();
        console.log(`"${this.operation}" validator object sucessfully constructed with params: 
                        Data : "${this.data}", 
                        Validity : "${this.isInputValid()}"`)

    }

    //returns list of number types
    //Private not supported in older versions of JS
    processInput() {
        return this.userInput.split(",")
                        .map(item => item.trim())
                        .filter(item => item !== "")
                        .map(Number);
    }

    //checks that list is not empty or contains null values
    isInputValid(){
        //return !((this.data.some(isNaN)) || (this.data.length != 2) || (this.data[0] < 0));
        return !((this.data.some(isNaN)) || (this.data.length != 3));
    }

}


class ArithmeticExpressionValidator extends OperatorInterface {
    constructor(operation, userInput){

        super(operation, userInput);
        this.data = this.processInput();
        console.log(`"${this.operation}" validator object sucessfully constructed with params: 
                        Data : "${this.data}", 
                        Validity : "${this.isInputValid()}"`)

    }

    //Private not supported in older versions of JS
    processInput() {
        return this.userInput; // just assigns input string here
    }

    //checks that list is not empty or contains null values
    isInputValid(){
        let regex = /^[0-9+\-*/()\s]*$/;
        return regex.test(this.data);
    }

}

export default { StatisticValidator, SingleParamFloatValidator, DoubleParamFloatValidator, ThreeParamFloatValidator, ArithmeticExpressionValidator };