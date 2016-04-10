var laborer_array = ["Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash",
	"Jose Cuervo","Mr Potato","Miso Horny","Ching Chong","Mexican Rash"
]

console.log(laborer_array.length);

// n=1
for (i=0; i < laborer_array.length; i++) {
  var modalID = 'modal_laborer' + String(i);
	$("#card-right")
		// console.log(laborer_array[i]);
		// .append("<button> Play </button>" + n + ". " + data[i].title + "; " + data[i].permalink_url + "</br></br>");



          .append($("<div class='card-panel blue-grey col s12 m3 l3 hoverable laborer-margin make-laborer'><div class='card-action buttonpadding'> <button id='prof' class='btn-floating modal-trigger' data-toggle='modal' data-target='" + modalID + "' name=" + laborer_array[i] + "><i class='material-icons'>info</i></button> </div>" +
                "<h5>" + laborer_array[i] + "</h5>" +
                // "</p> <div class='card-action'> <button id='prof' class='btn modal-trigger' data-toggle='modal' data-target='#modal_laborer' name=" + laborer_array[i] + "> Profileeee </button> </div> </div>"
                "<div id='" + modalID + "' class = 'modal bottom-sheet'> <div class = 'modal-content'> <h4>" + laborer_array[i] +
                "</h4><p>I am checking if i see this text</br>We will be populating the data from our backend integration</p></div></div> </div>"
                ));

                // .append($("<div class='card-panel blue-grey col s12 m3 l3 hoverable laborer-margin make-laborer'> <p>" +
                //       "<h5>" + laborer_array[i] + "</h5>" +
                //       // "</p> <div class='card-action'> <button id='prof' class='btn modal-trigger' data-toggle='modal' data-target='#modal_laborer' name=" + laborer_array[i] + "> Profileeee </button> </div> </div>"
                //       "</p> <div class='card-action'> <a id='prof' class='btn-floating modal-trigger buttonpadding' data-toggle='modal' data-target='" + modalID + "' name=" + laborer_array[i] + "><i class='material-icons'>info</i></a> </div> <div id='" + modalID + "' class = 'modal bottom-sheet'> <div class = 'modal-content'> <h4>" + laborer_array[i] +
                //       "</h4><p>I am checking if i see this text</br>We will be populating the data from our backend integration</p></div></div> </div>"
                //       ));

		// .append($("<div class='card-panel grey col s12 m3 l3 hoverable laborer-margin make-laborer'><p>" +
		// 	"</p><div><h5>" + laborer_array[i] + "</h5></div>" +
		// 	"<div class='card-action'><a href='#'> Profile </a> </div> </div>"));
      // n+=1;
	// n+=1;
	console.log(laborer_array[i]);
}

$(document).ready(function(){
	// the "href" attribute of .modal-trigger must specify the modal ID that wants to be triggered
	$('.modal-trigger').leanModal();
});

$('#job_submit').on('click', function callAPI() {
	var title_input = $("input[name=title_input]").val();
	var description_input = $("input[name=description_input]").val();
	var number_input = $("input[name=number_input]").val();
	var time_input = $("input[name=time_input]").val();
  $(".make-laborer").append("<div class='move-laborer'> <button2>" + title_input + "</button2> </div>")
  $(".mini-posts").append($("<article class='mini-post '>" +
		"<header class='" + title_input  +  "'>" +
			"<h3><a href='#'>" + title_input + "</a></h3>" + "<p class='minipost-margin'>" + description_input + "</p>" +
			"<p class='minipost-margin'>" + number_input + "</p>" +
			"<p class='minipost-margin'>" + time_input + "</p>" +
			"<time class='published date-margin' datetime='2015-10-20'>October 20, 2015</time> </header>" +

		" <a href='#' class='image'><img src='images/pic04.jpg' alt='' /></a> </article>"
		));
	$(".reset-label").on("focus", function(){
        $(".reset-label").val("");
    });
	$(this).parent().hide(400,"swing");
});

jQuery(document).ready(function(){
    jQuery('#hideshow').on('click', function(event) {
         jQuery('#to_show').toggle('show');
    });
});


$('#card-right').on('click', 'button2', function() {
	var _button2 = $(this);
	var _put = $(this).parent().parent()
	// alert($("#h5")).html();
	// alert($(this).parent().parent().html());
	// alert($("h5").html())
	var to_append = $(this).html();
	console.log(to_append);
	var lab_name = $(this).parent().parent().find("h5")
	console.log($(this).parent().parent().find("h5").html());
	$(this).parent().parent().remove()
	lab_name.appendTo("."+to_append)
});
