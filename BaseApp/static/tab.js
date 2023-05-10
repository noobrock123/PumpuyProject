//Loop Input
// var currentTab = 0; // Current tab is set to be the first tab (0)
// showTab(currentTab); // Display the current tab

window.onload = function() {
  add_loop();
  add_loop();
  add_loop();
}

var loopField = document.getElementById("LoopField");

function add_loop() {
  var loopField = document.getElementById("LoopField");

  var div = document.createElement("div");
  var num = document.getElementsByClassName('loop_field').length + 1
  div.setAttribute('class', "loop_field");
  div.setAttribute("name", "Loop" + num );
  div.textContent = "Loop " + num 

  let x1 = document.createElement("input");
  x1.setAttribute('type', 'text');
  x1.setAttribute('name', 'x1');
  x1.setAttribute('placeholder', 'x1');
  
  let x2 = document.createElement("input");
  x2.setAttribute('type', 'text');
  x2.setAttribute('name', 'x2');
  x2.setAttribute('placeholder', 'x2');

  let y1 = document.createElement("input");
  y1.setAttribute('type', 'text');
  y1.setAttribute('name', 'y1');
  y1.setAttribute('placeholder', 'y1');

  let y2 = document.createElement("input");
  y2.setAttribute('type', 'text');
  y2.setAttribute('name', 'y2');
  y2.setAttribute('placeholder', 'y2');

  div.appendChild(x1)
  div.appendChild(x2)
  div.appendChild(y1)
  div.appendChild(y2)

  loopField.appendChild(div)
}

function remove_loop() {
  var loopField = document.getElementById("LoopField");
  var loopClass = document.getElementsByClassName('loop_field')
  if(loopClass.length > 2) {
    loopField.removeChild(loopClass[(loopClass.length) - 1]);
  }
}

// function showTab(n) {
//   // This function will display the specified tab of the form
//   var x = document.getElementsByClassName("looptab");
//   x[n].style.display = "block";
//   // fix the Previous/Next buttons:
//   if (n == 0) {
//     document.getElementById("prevBtn").style.display = "none";
//   } else {
//     document.getElementById("prevBtn").style.display = "inline";
//   }
//   if (n == (x.length - 1)) {
//     document.getElementById("nextBtn").innerHTML = "Submit";
//   } else {
//     document.getElementById("nextBtn").innerHTML = "Next";
//   }
//   //... and run a function that will display the correct step indicator:
//   fixStepIndicator(n)
// }

// function nextPrev(n) {
//   // This function will figure out which tab to display
//   var x = document.getElementsByClassName("looptab");
//   // Exit the function if any field in the current tab is invalid:
//   if (n == 1 && !validateForm()) return false;
//   // Hide the current tab:
//   x[currentTab].style.display = "none";
//   // Increase or decrease the current tab by 1:
//   currentTab = currentTab + n;
//   // if you have reached the end of the form...
//   if (currentTab >= x.length) {
//     // ... the form gets submitted:
//     document.getElementById("regForm").submit();
//     return false;
//   }
//   // Otherwise, display the correct tab:
//   showTab(currentTab);
// }

// function validateForm() {
//   // This function deals with validation of the form fields
//   var x, y, i, valid = true;
//   x = document.getElementsByClassName("looptab");
//   y = x[currentTab].getElementsByTagName("input");
//   // A loop that checks every input field in the current tab:
//   for (i = 0; i < y.length; i++) {
//     // If a field is empty
//     if (y[i].value == "") {
//       // add an "invalid" class to the field:
//       y[i].className += " invalid";
//       // and set the current valid status to false
//       valid = false;
//     }
//   }
//   // If the valid status is true, mark the step as finished and valid:
//   if (valid) {
//     document.getElementsByClassName("step")[currentTab].className += " finish";
//   }
//   return valid; // return the valid status
// }

// function fixStepIndicator(n) {
//   // This function removes the "active" class of all steps...
//   var i, x = document.getElementsByClassName("step");
//   for (i = 0; i < x.length; i++) {
//     x[i].className = x[i].className.replace(" active", "");
//   }
//   //... and adds the "active" class on the current step:
//   x[n].className += " active";
// }


// //Add loop script on maitainance by KayKon

// function openCity(evt, cityName) {
//   var i, tabcontent, tablinks;
//   tabcontent = document.getElementsByClassName("tabcontent");
//   for (i = 0; i < tabcontent.length; i++) {
//     tabcontent[i].style.display = "none";
//   }
//   tablinks = document.getElementsByClassName("tablinks");
//   for (i = 0; i < tablinks.length; i++) {
//     tablinks[i].className = tablinks[i].className.replace(" active", "");
//   }
//   document.getElementById(cityName).style.display = "block";
//   evt.currentTarget.className += " active";
// }

// // Get the element with id="defaultOpen" and click on it
// document.getElementById("defaultOpen").click();