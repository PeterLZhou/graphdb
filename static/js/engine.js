var outcome = function(){
    var text = document.getElementById("form").elements[0].value;
    var length = text.length;
    if (length % 3 == 0){
	document.getElementById("answer").innerHTML = "Yes";
    }
    else if (length % 3 == 1){
	document.getElementById("answer").innerHTML = "No";
    }
    else{
	document.getElementById("answer").innerHTML = "Not Sure";
    }
    return false;
}

