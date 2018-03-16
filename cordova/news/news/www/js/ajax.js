// for sending the request to server

function _getNews(callback) {
	console.log("_getNews called");
	$.ajax({
		url: "http://ec2-13-58-231-72.us-east-2.compute.amazonaws.com/main",
		//url: "http://localhost:8001/main",
		success: function(text) {
			console.log("success function called");
			callback(JSON.parse(text));
		}
	});
}