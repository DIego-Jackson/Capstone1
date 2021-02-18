
$(document).ready(function(){
  console.log("going back in there"); 

  var row = [];
  $.ajax({
      type: "POST",
      url: 'sql.php',
      data: {functionname: 'selectEPS_DataLocationSQL', arguments: []},

      success: function (data) {
	window.alert(data);
	var response = JSON.parse(data);
        $.each(data, function(key, value){
          row.push(value);
          });
      }
  });
 
  console.log(row);
/*	
  row.forEach(addingOptions);

  function addingOptions(item, index) {
    var x = document.getElementById("location");
    var option = document.createElement("option");
    //option.text = row[index];
    console.log("hi");
    option.text = "1";
    x.add(option);
  }
  /*
      document.getElementById("filterCrimeBtn").onclick = function(){
          }
  */
      /* End */

});


function isChecked(){
	var assaultCheck = document.getElementById("assault");
        var BreakEnterCheck = document.getElementById("breakAndEnter");
        var homicideCheck = document.getElementById("homicide");
        var robberyCheck = document.getElementById("robbery");
        var sexualAssaultCheck = document.getElementById("aexualAssault");
        var theftofVehicleCheck = document.getElementById("theftOfVehicle");
        var theftfromVehicleCheck = document.getElementById("theftFromVehicle");


	//change this deoending on what is clicked
	if (assaultCheck.checked == true) {
		console.log("assault");
	}
	else if (BreakEnterCheck.checked == true) {
		console.log("break");
	}
	else if (homicideCheck.checked == true) {
		console.log("homicide");
        }
	else if (robberyCheck.checked == true) {
                console.log("robbery");
        }
	else if (sexualAssaultCheck.checked == true) {
                console.log("sexualAssault");
        }
	else if (theftofVehicleCheck.checked == true) {
                console.log("of");
        }
        else if (theftfromVehicleCheck.checked == true) {
                console.log("from");
	}
	else{
                console.log("if this runs ait's after many things were turned off");
        }
}
