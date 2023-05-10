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
  var num = document.getElementsByClassName('loop_field').length + 1;
  var text = "";

  text = `<div class="loop_field" id="Loop${num}" name="Loop${num}">Loop${num}`
  text += '</br>';
  text += `<table>`;

  for (let init = 1; init < 5; init++) { 
    text += `<tr>`;
    text += `<td><input name="x${init}" id="x${init}" placeholder="x${init}"></input></td>`;
    text += `<td><input name="y${init}" id="y${init}" placeholder="y${init}"></input></td>`;
    text += `</tr>`;
  }

  text += `</table>`;
  text += `</div>`;

  loopField.insertAdjacentHTML("beforebegin", text);
}

function remove_loop() {
  var loopField = document.getElementById('LoopField')
  var loopClass = document.getElementsByClassName('loop_field')
  // console.log(loopClass.length)
  if(loopClass.length > 2) {
    document.getElementById(`Loop${loopClass.length}`).remove();
  }
}

var video = document.getElementById('video');
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext('2d');

// var loop1_x1 = document.getElementsByName("Loop1");
// console.log(loop1_x1.getElementById('x1'))
// loop1_x1.addEventListener("Keydown", function() {
//   console.log(loop1_x1)
// });

// set canvas size = video size when known
video.addEventListener('loadedmetadata', function() {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
});

video.addEventListener('play', function() {  
  var $this = this; //cache
  (function loop() {
    if (!$this.paused && !$this.ended) {
      ctx.lineWidth = 8;
      ctx.strokeStyle = '#00FF00';
      
      ctx.drawImage($this, 0, 0);
      ctx.beginPath(); // Start a new path
      ctx.moveTo(900, 600); // x1, y1
      ctx.lineTo(900, 300); // x2, y2
      ctx.lineTo(400, 300); // x3, y3
      ctx.lineTo(400, 600); // x4, y4
      ctx.lineTo(900, 600); // x1, y1 to close the loop
      ctx.stroke(); // Render the path  

      setTimeout(loop, 1000 / 30); // drawing at 30fps
    }
  })();
}, 0);

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