var laborer_array = [];

//Ajax Call to load laborers on the landing page from the datbase
$.ajax({
	 url: "/loadlaborers",
	 type: "post",

	 success: function(response){
		var data = jQuery.parseJSON(response);
		for (i=0; i < data.length; i++) {
		laborer_array.push(data[i])
		}
				createlaborcard();
				$('.modal-trigger').leanModal();
	}
});

//Ajax Call to load all the completed employer job cards on the profile page of the employer

$.ajax({
	 url: "/profile_cards",
	 type: "post",
	 success: function(response){
	 	var data = jQuery.parseJSON(response);
		for(i=0;i<data.length;i++)
			{
				var _request_id = data[i]["request_id"]
				var title_input = data[i]["request_title"];
		 		var description_input = data[i]["request_description"];
		 		var number_input = data[i]["request_num_ppl"];
		 		var time_input = data[i]["request_time"];
				var laborer_string = ""
				for(j=0;j<data[i]["laborer_data"].length;j++)
					{
						laborer_string +=  "<h5 class='laborer-dark' id = '"+data[i]["laborer_data"][j]["id"]+"' style='padding-top:1em'>" + data[i]["laborer_data"][j]["name"] + "</h5>"

					}

		 		$("#profile-cards").append($("<article class='col s12 m5 l5 mini-post' style='margin:1em'>" +
		 			"<header class='" + title_input  +  "'>" +
		 			"<h3><a href='#'>" + title_input + "</a></h3>" + "<p class='minipost-margin'>" + description_input + "</p>" +
		 			"<p id='number_workers' class='minipost-margin'>" + number_input + " workers</p>" +
		 			"<p class='minipost-margin'>" + time_input + "</p>" +
		 			"<time class='published date-margin' datetime='2015-10-20'>October 20, 2015</time> "+laborer_string +"</header>" +
		 			 " <a href='#' class='image'><img src= '/static/images/pic04.jpg' alt='' /></a> </article>"

		 		));


		}
	}
});

//Ajax Call to load all the open job cards from the datbase on the landing page
$.ajax({
	 url: "/loadjobcards",
	 type: "post",
	 success: function(response){
		var data = jQuery.parseJSON(response);

		for(i=0;i<data.length;i++)
		{
			var _request_id = data[i]["request_id"]
			var title_input = data[i]["request_title"];
	 		var description_input = data[i]["request_description"];
	 		var number_input = data[i]["request_num_ppl"];
	 		var time_input = data[i]["request_time"];
			var laborer_string = ""
			for(j=0;j<data[i]["laborer_data"].length;j++)
			{
				laborer_string +=  "<div class='row ' style='padding-bottom:5px'>" + "<div > <button3 id='cancel-laborer' style='color:#009688' class='btn-floating'><i class='material-icons'>delete_forever</i></button3> </div> <h5 style='margin-top:17px' class='laborer-dark' id = '"+data[i]["laborer_data"][j]["id"]+"' style='padding-top:1em'>" + data[i]["laborer_data"][j]["name"] + "</h5>" + "</div>"


		}
		var modalID = 'modal_job' + String(i);

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

//Function the create and display the laborer profiles on the front end

function createlaborcard(){
	for (i=0; i < laborer_array.length; i++) {
		var laborer_id = laborer_array[i]['laborer_id']
		var laborer_name = laborer_array[i]['laborer_name']
		var laborer_skills = laborer_array[i]['laborer_skill']
		var laborer_phone_num = laborer_array[i]['laborer_phone_num']
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
	                "<div id='" + modalID + "' class = 'modal bottom-sheet'> <div class = 'modal-content'>" +
	                "<h5>" + laborer_name + "</h5>" +
	                "<p>" + "Skills: " + laborer_skills + "</p>" +
	                "<p> Reviews and Verification to come! </p></div></div> </div>"
	                ));
	}
}



$('#job_submit').on('click', function callAPI() {
	var title_input = $("input[name=title_input]").val();
	var description_input = $("input[name=description_input]").val();
	var number_input = $("input[name=number_input]").val();
	var time_input = $("input[name=time_input]").val();
	$(".reset-label").on("focus", function(){
        $(".reset-label").val("");
    });
	$(this).parent().hide(400,"swing");


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
	   success: function(response){
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


	var lab_name = $(this).parent().parent().find(".card-add-name")
	var parent_parent = $(this).parent().parent()

	var data_tosend = {
	    data: JSON.stringify({
			"request_id": req_id,
      		"laborer_id": lab_id
	    })
	};

	// pass data to route /CreateJobCard so can put in DB
	$.ajax({
	    url: "/Createfulfillment",
	    type: "post",
		data: data_tosend,
	    success: function(response){
	    	if (response=="love") {
	    		parent_parent.remove()

				inner_lab = lab_name.html()
				lab_name = "<div id='cancel-laborer' class='row' style='padding-bottom:5px'>" + "<div > <button3 style='color:#009688' class='btn-floating cancel-laborer'><i class='material-icons'>delete_forever</i></button3> </div> <h5 style='margin-top:17px' class='laborer-dark' id = '"+lab_id+"' style='padding-top:1em'>" + inner_lab + "</h5>" + "</div>"
				$("."+to_append).append(lab_name)
				window.location.reload()

	    	} else {
	    		alert("Jobcard already full")
	    	}
	    }
	});


});

$('.mini-posts').on('click', 'button', function() {

	var list_of_ids = []
	var _request_id    = $(this).attr('class')
	var _laborer_id    = $(this).parent().find(".laborer-dark")
	var parent_parent  = $(this).parent().parent()
	for(i=0;i<_laborer_id.length;i++)
	{
		list_of_ids.push(_laborer_id[i].id)

	}


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
				window.location.reload()
		}
	});
});

$('.mini-posts').on('click', 'button3', function() {

    req_id = $(this).parent().parent().parent().find("#make-done").attr('class')
		lab_id = $(this).parent().parent().find(".laborer-dark")[0].id

		$(this).parent().parent().remove()

		var data_tosend = {
		    data: JSON.stringify({
				"laborer_id": lab_id,
				"request_id": req_id
		    })
		};

		$.ajax({
			url: "/removelaborer",
				type: "post",
			data: data_tosend,
				success: function(response){

					window.location.reload()
			}
		});
});
