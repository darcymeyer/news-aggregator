// for sending the request to server

function _getNews(callback) {
	$.ajax({
		url: "ec2-13-58-231-72.us-east-2.compute.amazonaws.com/main",
		success: function(text) {
			callback(JSON.parse(text));
		}
	});
}