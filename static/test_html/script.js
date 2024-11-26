function save(){
    let History_serialized = JSON.stringify(History);
    localStorage.setItem("History", History_serialized); 
}

let History = JSON.parse(localStorage.getItem("History"));
if(History == null){
    History = {
        last_was_equal: false,
        count: 0,
        entries: []
    };
}
document.getElementById('equal').addEventListener('click', function(){
    submitCalculation()
    var entry = {
        operation: document.getElementById('previous').value.toString().slice(0,-1),
        answer: document.getElementById('display').value
    };
    if(entry.operation.valueOf() == ""){
        console.log("yep");
    }
    History.entries.push(entry);
    console.log(History);
    History.last_was_equal = true;
    
    var historyHTML = document.getElementById('history');
    var operationTXT = document.createTextNode(entry.operation);
    var answerTXT = document.createTextNode(entry.answer);
    var big_div = document.createElement('div')
    var div_op = document.createElement('div');
    div_op.classList.add("history_value")
    div_op.appendChild(operationTXT);
    div_op.onclick = function(){display.value = div_op.innerHTML}
    big_div.append(div_op)
    big_div.append(" = ");
    var div_ans = document.createElement('div');
    div_ans.classList.add("history_value")
    div_ans.appendChild(answerTXT);
    div_ans.onclick = function(){display.value = div_ans.innerHTML}
    big_div.append(div_ans)
    historyHTML.appendChild(big_div);
    
})

var number_buttons = document.getElementsByClassName('number');
for (var i = 0;i < number_buttons.length; i++){
    let btn = number_buttons[i];
    let val = btn.value;
    btn.addEventListener('click', function(){
        if(History.last_was_equal){
            document.getElementById('display').value = val;
            History.last_was_equal = false;
        }
    });
}
var operator_buttons = document.getElementsByClassName('operator');
for (var i = 0;i < operator_buttons.length; i++){
    let btn = operator_buttons[i];
    btn.addEventListener('click', function(){
        if(History.last_was_equal){
            History.last_was_equal = false;
        }
    });
}

var display = document .getElementById("display");
display.addEventListener("keypress", function(event){
    if(event.key == "Enter"){
        document.getElementById('equal').click();
    }
})

async function submitCalculation() {
    const dataInput = document.getElementById("display").value;
    const url = "/calculate_call";
    let calcPackage = {
        data : dataInput
    }

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(calcPackage),
        });
        console.log("yay")

        // Parse response and display result
        const result = await response.json();
        document.getElementById("display").value = result?.calculation_result ?? "A Backend Processing Error Occured";
        console.log("ya2y")
    } catch (error) {
        document.getElementById("display").textContent = "An error occurred.";
        console.log("ya5y")
    }
}
