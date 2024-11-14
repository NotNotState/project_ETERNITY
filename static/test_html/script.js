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
    var div = document.createElement('div');
    div.appendChild(operationTXT);
    div.append(" = ");
    div.appendChild(answerTXT);
    historyHTML.appendChild(div);
    
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