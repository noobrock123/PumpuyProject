//Loop Input
// var currentTab = 0; // Current tab is set to be the first tab (0)
// showTab(currentTab); // Display the current tab

function select_loop() {
  var hitboxs = document.getElementById('select_hitboxs');
  hitboxs.hidden = false;
}

function create_loop() {
  document.getElementById(`choice`).remove();
  var hitboxs = document.getElementById('select_hitboxs');
  hitboxs.hidden = true;
  
  var file_name = document.createElement('input');
  file_name.type = "text";
  file_name.required;
  file_name.name = "file_name";
  file_name.placeholder = "File Name";
  file_name.pattern = "[^\\/:\x22*?<>|]+";
  var container = document.getElementById("regForm");
  container.prepend(file_name);

  var remove = document.getElementById("remove");
  var add = document.getElementById("add");

  remove.hidden = false;
  add.hidden = false;
  
  // document.getElementById("select_loop").remove();
  // document.getElementById("create_loop").remove();
  
  add_loop();
  add_loop();
  add_loop();
  
  // var elem = document.getElementsById("create");  
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
    text += `<td><input name="x${init}" id="loop${num}x${init}" placeholder="x${init}"></input></td>`;
    text += `<td><input name="y${init}" id="loop${num}y${init}" placeholder="y${init}"></input></td>`;
    text += `</tr>`;
  }
  text += `<select id='orientation'>`;
  text += `<option value='clockwise'>Clockwise</option>`
  text += `<option value='counterclockwise'>Counterclockwise</option>`
  text += `</select>`

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
      
      var num = document.getElementsByClassName('loop_field').length + 1;

      ctx.drawImage($this, 0, 0);
      
      
      // console.log(num);      

      for (var i = 1; i < num; i++) {
        var x1 = document.getElementById(`loop${i}x1`);
        var y1 = document.getElementById(`loop${i}y1`);
        var x2 = document.getElementById(`loop${i}x2`);
        var y2 = document.getElementById(`loop${i}y2`);
        var x3 = document.getElementById(`loop${i}x3`);
        var y3 = document.getElementById(`loop${i}y3`);
        var x4 = document.getElementById(`loop${i}x4`);
        var y4 = document.getElementById(`loop${i}y4`);

        // console.log(x1.value);


        ctx.beginPath(); // Start a enter line
        ctx.strokeStyle = '#0000FF';
        ctx.moveTo(x1.value, y1.value); // x1, y1
        ctx.lineTo(x2.value, y2.value); // x2, y2
        ctx.stroke();
        ctx.beginPath();
        ctx.strokeStyle = '#00FF00'; // Start a box line
        ctx.lineTo(x2.value, y2.value); // x2, y2
        ctx.lineTo(x3.value, y3.value); // x3, y3
        ctx.lineTo(x4.value, y4.value); // x4, y4
        ctx.lineTo(x1.value, y1.value); // x1, y1 to close the loop
        ctx.stroke(); // Render the path  
      }

      setTimeout(loop, 1000 / 30); // drawing at 30fps
    }
  })();
}, 0);



function collect_loops() {  

  var num = document.getElementsByClassName('loop_field').length + 1;
  
  let json_loops = {
    "loops": []
  }

  for (var i = 1; i < num; i++) {
    var x1 = document.getElementById(`loop${i}x1`);
    var y1 = document.getElementById(`loop${i}y1`);
    var x2 = document.getElementById(`loop${i}x2`);
    var y2 = document.getElementById(`loop${i}y2`);
    var x3 = document.getElementById(`loop${i}x3`);
    var y3 = document.getElementById(`loop${i}y3`);
    var x4 = document.getElementById(`loop${i}x4`);
    var y4 = document.getElementById(`loop${i}y4`);    
    var orientation = document.getElementById(`orientation`)

    var loop = {
      "name": `loop${i}`,
      "id": `${i-1}`,
      "points":[
        {"x":parseInt(`${x1.value}`),"y":parseInt(`${y1.value}`)},
        {"x":parseInt(`${x2.value}`),"y":parseInt(`${y2.value}`)},
        {"x":parseInt(`${x3.value}`),"y":parseInt(`${y3.value}`)},
        {"x":parseInt(`${x4.value}`),"y":parseInt(`${y4.value}`)},
      ],
      "orientation":`${orientation.value}`,
      "summary_location":{"x":9999,"y":"9999"}
    };

    // console.log(loop["points"][0]);
  
    json_loops["loops"].push(loop);
  }

  var text_json = JSON.stringify(json_loops)
  
  document.getElementById("loops").value = text_json;

  // console.log(text_json);
    
  // $('loops').submit();
}


// Video Pixel

var vid = document.getElementById("video"); 
var HeightHolder = document.getElementById('cont_h');
var WidthHolder = document.getElementById('cont_w');
video.addEventListener('loadedmetadata', function() {
HeightHolder.innerHTML = vid.videoHeight; // returns the intrinsic height of the video
WidthHolder.innerHTML = vid.videoWidth;
});
// WidthHolder.innerHTML = vid.videoHeight; // returns the intrinsic height of the video
// HeightHolder.innerHTML = vid.videoWidth; // returns the intrinsic width of the video




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