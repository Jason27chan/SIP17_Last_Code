var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  var userPassword = document.getElementById("pw").value;
  console.log(userPassword);

for (var i =0; i< wordsList.length; i++) {
   if(wordsList[i] == userPassword){
      document.getElementById("results").innerHTML = "YOU SUCK";
       break;
    
   }
    else if (i == (wordsList.length - 1)) {
        document.getElementById("results").innerHTML = "YOU SUCK LESS";
    }
} 
}


//
//
//



function checkPassword() {
  var userPassword = document.getElementById("pw").value;
  console.log(userPassword);
    

for (var i =0; i< wordsList.length; i++) {
   if(wordsList[i] == userPassword){
      document.getElementById("results").innerHTML = "YOU SUCK";
       break;
    
   }
    else if (i == (wordsList.length - 1)) {
        document.getElementById("results").innerHTML = "YOU SUCK LESS";
    }
} 
}






