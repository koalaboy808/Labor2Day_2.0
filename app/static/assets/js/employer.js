var laborer_array = [];


$.ajax({
	 url: "/loadlaborers",
	 type: "post",
	// contentType: 'application/json;charset=UTF-8',
	 success: function(response){
		console.log(response);
		var data = jQuery.parseJSON(response);
		console.log("testing it out")
		console.log(data)
		for (i=0; i < data.length; i++) {
		// laborer_array[i]['laborer_name'] = data[i]['laborer_name']
		// laborer_array[i]['laborer_phone_num'] = data[i]['laborer_phone_num']
		// laborer_array[i]['laborer_availability'] = data[i]['laborer_availability']
		// laborer_array[i]['laborer_skill'] = data[i]['laborer_skill']
		laborer_array.push(data[i])
		}
				createlaborcard();
				$('.modal-trigger').leanModal();
	}
});

console.log(laborer_array)

$.ajax({
	 url: "/profile_cards",
	 type: "post",
	// contentType: 'application/json;charset=UTF-8',
	 success: function(response){
	 	// print('success profile_cards')
	 	var data = jQuery.parseJSON(response);
		for(i=0;i<data.length;i++)
			{
				console.log("this is the " + i + " th card")
				var _request_id = data[i]["request_id"]
				var title_input = data[i]["request_title"];
		 		var description_input = data[i]["request_description"];
		 		var number_input = data[i]["request_num_ppl"];
		 		var time_input = data[i]["request_time"];
				var laborer_string = ""
				for(j=0;j<data[i]["laborer_data"].length;j++)
					{
						laborer_string +=  "<h5 class='laborer-dark' id = '"+data[i]["laborer_data"][j]["id"]+"' style='padding-top:1em'>" + data[i]["laborer_data"][j]["name"] + "</h5>"
						//console.log("ace venture" + data[i]["laborer_data"][j]["name"])

					}
			// console.log(laborer_string)
		 		// $(".make-laborer").append("<div class='move-laborer'> <button2 id='"+_request_id+"'>" + title_input + "</button2> </div>")
		 		$("#profile-cards").append($("<article class='col s12 m5 l5 mini-post' style='margin:1em'>" +
		 			"<header class='" + title_input  +  "'>" +
		 			"<h3><a href='#'>" + title_input + "</a></h3>" + "<p class='minipost-margin'>" + description_input + "</p>" +
		 			"<p id='number_workers' class='minipost-margin'>" + number_input + " workers</p>" +
		 			"<p class='minipost-margin'>" + time_input + "</p>" +
		 			// "</br>" +
		 			// "<button class='"+ _request_id +"' id='make-done'> Done </button>" +
		 			"<time class='published date-margin' datetime='2015-10-20'>October 20, 2015</time> "+laborer_string +"</header>" +
		 			 " <a href='#' class='image'><img src= '/static/images/pic04.jpg' alt='' /></a> </article>"

		 		));


		}
	}
});


$.ajax({
	 url: "/loadjobcards",
	 type: "post",
	// contentType: 'application/json;charset=UTF-8',
	 success: function(response){
		console.log(response);
		console.log(response[0])
		var data = jQuery.parseJSON(response);
		console.log(data[0]["request_title"])

		for(i=0;i<data.length;i++)
		{
			console.log("this is the " + i + " th card")
			var _request_id = data[i]["request_id"]
			var title_input = data[i]["request_title"];
	 		var description_input = data[i]["request_description"];
	 		var number_input = data[i]["request_num_ppl"];
	 		var time_input = data[i]["request_time"];
			var laborer_string = ""
			for(j=0;j<data[i]["laborer_data"].length;j++)
			{
				laborer_string +=  "<h5 class='laborer-dark' id = '"+data[i]["laborer_data"][j]["id"]+"' style='padding-top:1em'>" + data[i]["laborer_data"][j]["name"] + "</h5>"
				//console.log("ace venture" + data[i]["laborer_data"][j]["name"])

		}
		var modalID = 'modal_job' + String(i);
		console.log(laborer_string)
	 		$(".make-laborer").append("<div class='move-laborer'> <button2 id='"+_request_id+"'>" + title_input + "</button2> </div>")
	 		$(".mini-posts").append($("<article class='mini-post '>" +
	 			"<header class='" + title_input  +  "'>" +
	 			"<h3><a class = 'modal-trigger' href='#"+modalID+"'>" + title_input + "</a></h3>" + "<p class='minipost-margin'>" + description_input + "</p>" +
	 			"<p id='number_workers' class='minipost-margin'>" + number_input + " workers</p>" +
	 			"<p class='minipost-margin'>" + time_input + "</p>" +
	 			"</br>" +
	 			"<button class='"+ _request_id +"' id='make-done'> Done </button>" +


	 			"<time class='published date-margin' datetime='2015-10-20'>October 20, 2015</time>"+laborer_string +"</header>" +
	 			 " <a href='#' class='image'><img src= '/static/images/pic04.jpg' alt='' /></a>" +"<div id='" + modalID + "'class = 'modal modal-fixed-footer'> <div class = 'modal-content'>" +
				 "<h5>Job Title: "+title_input+"</h5>" +
 				"<p>Job Description: "+description_input+"</p><h5>Your selected Laborers</h5>"+laborer_string+
				 "<p></br> Reviews and Verification to come! </p></div>"
				 + "<div class='modal-footer'>"+
				 "<a href='#!' class='modal-action modal-close waves-effect waves-green btn-flat'>CLOSE</a>"+
				 "</div></div>"+ "</article>"

	 		));
$('.modal-trigger').leanModal();

	}
}
});




// console.log(laborer_array.length);

// // n=1
// for (i=0; i < laborer_array.length; i++) {
//   var modalID = 'modal_laborer' + String(i);
// 	$("#card-right")
//           .append($("<div class='card-panel blue-grey col s12 m3 l3 hoverable laborer-margin make-laborer'><div class='card-action buttonpadding'> <button id='prof' class='btn-floating modal-trigger' data-toggle='modal' data-target='" + modalID + "' name=" + laborer_array[i] + "><i class='material-icons'>info</i></button> </div>" +
//                 "<h5>" + laborer_array[i] + "</h5>" +
//                 // "</p> <div class='card-action'> <button id='prof' class='btn modal-trigger' data-toggle='modal' data-target='#modal_laborer' name=" + laborer_array[i] + "> Profileeee </button> </div> </div>"
//                 "<div id='" + modalID + "' class = 'modal bottom-sheet'> <div class = 'modal-content'> <h4>" + laborer_array[i] +
//                 "</h4><p>I am checking if i see this text</br>We will be populating the data from our backend integration</p></div></div> </div>"
//                 ));
// 	console.log(laborer_array[i]);
// }

// var practice = ["hello","goodbye"]
function list_skills(_list) {
	var out = "";
	for (i=0; i < _list.length; i++) {
		if (i==_list.length) {
			out+= _list[i];
		} else {
			out += _list[i] + ", ";
		}
	}
	return out;
}

// alert(list_skills(practice));
// $(document).ready(function(){
	// var out_list = []
	// for (i=0; i < laborer_array.length; i++) {
	// 	var laborer_skills = laborer_object[i]['laborer_skills']
	// 	out_list.push(laborer_skills.join())
	//
	// 	// var out_skills = list_skills(laborer_skills)
	// 	// console.log(out_skills)
	// }
	// console.log(out_list)

function createlaborcard(){
console.log("checking2")
	for (i=0; i < laborer_array.length; i++) {
		console.log("checking")
		var laborer_id = laborer_array[i]['laborer_id']
		var laborer_name = laborer_array[i]['laborer_name']
		var laborer_skills = laborer_array[i]['laborer_skill']
		var laborer_phone_num = laborer_array[i]['laborer_phone_num']
		console.log(laborer_name)
		// var out_skills = list_skills(laborer_skills)
	  var modalID = 'modal_laborer' + String(i);
		$("#card-right")
	          .append($("<div class='card-panel grey darken-3 col s12 m3 l3 hoverable laborer-margin make-laborer'>" +
	          		"<div class='row'>" +
	          			"<div>" +
	                		"<h5 class='card-add-name' id = '"+laborer_id+"' style='padding-top:1em'>" + laborer_name + "</h5>" +
	                	"</div>" +
	          			"<div class='card-action buttonpadding' style='float:right;'>" +
	          				"<button id='prof' class='btn-floating btn-small modal-trigger' data-toggle='modal' data-target='" + modalID + "' name=" + laborer_name + "><i class='material-icons'>menu</i></button>" +
	          			"</div>" +
	                "</div>" +
	                "<p class='text-light'>" + "Skills: " + laborer_skills + "</p>" +
	                // "</p> <div class='card-action'> <button id='prof' class='btn modal-trigger' data-toggle='modal' data-target='#modal_laborer' name=" + laborer_array[i] + "> Profileeee </button> </div> </div>"
	                "<div id='" + modalID + "' class = 'modal bottom-sheet'> <div class = 'modal-content'>" +
	                "<h5>" + laborer_name + "</h5>" +
	                "<p>" + "Skills: " + laborer_skills + "</p>" +
	                "<p> Reviews and Verification to come! </p></div></div> </div>"
	                ));
		// console.log(laborer_object[i]['laborer_first_name']);
	}
}
// });


// $(document).ready(function(){
// 	// the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
// 	$('.modal-trigger').leanModal();
// });

$('#job_submit').on('click', function callAPI() {
	var title_input = $("input[name=title_input]").val();
	var description_input = $("input[name=description_input]").val();
	var number_input = $("input[name=number_input]").val();
	var time_input = $("input[name=time_input]").val();
  	// $(".make-laborer").append("<div class='move-laborer'> <button2>" + title_input + "</button2> </div>")

	$(".reset-label").on("focus", function(){
        $(".reset-label").val("");
    });
	$(this).parent().hide(400,"swing");

	console.log(document.getElementById("username").innerText);

	// stringy data from job_submit into object so can pass to ajax /CreateJobCard
	var data = {
	    data: JSON.stringify({
			"username": document.getElementById("username").innerText,
            "cardtitle": title_input,
			"description": description_input,
			"numberofworkers": number_input,
			"timeofjob": time_input
	    })
	};
	console.log(data);

	// pass data to route /CreateJobCard so can put in DB
	$.ajax({
	    url: "/CreateJobCard",
	    type: "post",
		data: data,
    // contentType: 'application/json;charset=UTF-8',
	   success: function(response){
			console.log(response)
			var modalID = 'modal_job' + String(response);
			var laborer_string = "NA"
			$(".make-laborer").append("<div class='move-laborer'> <button2 id='"+response+"'>" + title_input + "</button2> </div>")

			$(".mini-posts").append($("<article class='mini-post '>" +
				"<header class='" + title_input  +  "'>" +
					"<h3><a class = 'modal-trigger' href='#"+modalID+"'>" + title_input + "</a></h3>" + "<p class='minipost-margin'>" + description_input + "</p>" +
					"<p id='number_workers' class='minipost-margin'>" + number_input + " workers</p>" +
					"<p class='minipost-margin'>" + time_input + "</p>" +
					"</br>" +
					"<button class='"+ response +"' id='make-done'> Done </button>" +
					"<time class='published date-margin' datetime='2015-10-20'>October 20, 2015</time> </header>" +

				" <a href='#' class='image'><img src= '/static/images/pic04.jpg' alt='' /></a>"+ "<div id='" + modalID + "'class = 'modal modal-fixed-footer'> <div class = 'modal-content'>" +
				"<h5>Job Title: "+title_input+"</h5>" +
				"<p>Job Description: "+description_input+"</p><h5 class='lovely'>Your selected Laborers</h5>"+laborer_string+
				"<p> </br>Reviews and Verification to come! </p></div>"
				+ "<div class='modal-footer'>"+
				"<a href='#!' class='modal-action modal-close waves-effect waves-green btn-flat'>CLOSE</a>"+
				"</div></div>"+ "</article>"


	// 			"<div id='modal1' class='modal'>" +
  //   "<div class='modal-content'>" + "
  //     <h4>Modal Header</h4>"+"
  //     <p>A bunch of text</p>"+"
  //   </div>"+"
  //   <div class='modal-footer'>"+"
  //     <a href='#!' class='modal-action modal-close waves-effect waves-green btn-flat'>Agree</a>"+"
  //   </div>"+"
  // </div>"
			));
$('.modal-trigger').leanModal();
	    }
	});
});

// jquery to show and hide job create form
jQuery(document).ready(function(){
    jQuery('#hideshow').on('click', function(event) {
         jQuery('#to_show').toggle('show');
    });
});


$('#card-right').on('click', 'button2', function() {
	var lab_id = $(this).parent().parent().find(".card-add-name")[0].id
	var req_id = $(this)[0].id
	var _put = $(this).parent().parent()
	var to_append = $(this).html();
	var wtf = $(this).parent().parent().find(".card-add-name")[0]

	console.log("lab id " + lab_id)
	console.log("req id " + req_id)

	var lab_name = $(this).parent().parent().find(".card-add-name")
	console.log(to_append)
	var parent_parent = $(this).parent().parent()

	var data_tosend = {
	    data: JSON.stringify({
			"request_id": req_id,
      		"laborer_id": lab_id
	    })
	};
	console.log(data_tosend);

	// pass data to route /CreateJobCard so can put in DB
	$.ajax({
	    url: "/Createfulfillment",
	    type: "post",
		data: data_tosend,
	    success: function(response){
	    	if (response=="love") {
	    		console.log("love")
	    		parent_parent.remove()

				lab_name = lab_name.addClass("laborer-dark")
				lab_name = lab_name.removeClass("card-add-name")

				var appendit = "."+to_append
				lab_name.appendTo("."+to_append)
				// lab_name.appendTo($(" ' " + appendit + " #laborers_modal_job ' "))
				lab_name.appendTo($("." + to_append + " .modal-content"))
	    	} else {
	    		alert("Jobcard already full")
	    	}
	    }
	});


});

$('.mini-posts').on('click', 'button', function() {

	var list_of_ids = []
	// var number_workers = parseInt($(this).parent().find("#number_workers").html()[0])
	var _request_id    = $(this).attr('class')
	var _laborer_id    = $(this).parent().find(".laborer-dark")
	var parent_parent  = $(this).parent().parent()
	for(i=0;i<_laborer_id.length;i++)
	{
		list_of_ids.push(_laborer_id[i].id)

	}

	console.log("laborer id: " + _laborer_id)
	console.log("list" + list_of_ids)
	// console.log("number_workers: " + number_workers)
	console.log("_request_id: " + _request_id)

	parent_parent.remove()

	var data_tosend = {
	    data: JSON.stringify({
			"request_id": _request_id,
			"list_of_ids": list_of_ids
	    })
	};

	$.ajax({
		url: "/jobcard_done",
	    type: "post",
		data: data_tosend,
	    success: function(response){
	    	console.log(response)
		}
	});
});
