// for sending the request to server

function _getNews(callback) {
	console.log("_getNews called");
	$.ajax({
		url: "http://ec2-13-58-231-72.us-east-2.compute.amazonaws.com/main",
		type: 'GET',
		//url: "http://localhost:8001/main",
		success: function(text) {
			console.log("success function called");
			// console.log("text", text);
			// callback(JSON.parse(text));
			callback(text);
			$( ".summary" ).click(function() {
				if (!$(this).hasClass("open")) {
					var prev = $(this).parent().parent().find(".open");
					prev.parent().find(".sources").slideUp(150);
					prev.removeClass("open");
					var next = $(this).parent().find(".sources");
					next.slideDown(150);
					$(this).addClass("open");
				} else {
					var curr = $(this).parent().find(".sources");
					curr.slideUp(150);
					curr.parent().find(".summary").removeClass("open");
				}
			});
		}
	});
}