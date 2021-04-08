var toDoTable = document.getElementById("tableBody");
var theme = 'dark';

function newValue(formValues) {
    //Add new row to the end of the table
    var newRow = toDoTable.insertRow(-1);
    //Add the form information as cells in the new row
    for (var i = 0; i < formValues.length - 1; i++) {
        var x = newRow.insertCell();
        x.innerHTML = formValues[i].value;
    }
    //Create a button to clear the task
    var buttonHome = newRow.insertCell();
    buttonHome.innerHTML = '<input type="button" value="Complete" onclick="clearTask(this);"></input>'
    
}

function clearTask(deathRow) {
    //Take the selected row and clear it
    var indexRow = deathRow.parentElement.parentElement.rowIndex;
    toDoTable.deleteRow(indexRow - 1);
}

function clearForm() {
    //Clear the form of all data and return to null
    var formElem = document.getElementsByName("newTask");
    
    for(var i = 0; i < formElem.length; i++) {
        formElem[i].value = null;
    }
}

function toggleTheme() {
    //Javascript is being super dumb about this and is complaining about the document.getElementsByTagName function
    //and I cannot tell you why. I may have to take a different approach, since the function may not accept arrays
    //is my best guess atm
    if (theme == 'dark') {
        document.getElementById('html').style.color = "#062122";
        document.getElementById('toDoList').style.borderColor = "#062122";
        document.getElementById('inputForm').style.borderColor = "#062122";
        
        theme = 'light';
    }
    else {
        document.getElementById('html').style.color = "#bbd8d9";
        document.getElementById('toDoList').style.borderColor = "#bb8d9";
        document.getElementById('inputForm').style.borderColor = "#bbd8d9";
        
        theme = 'dark';
    }
}