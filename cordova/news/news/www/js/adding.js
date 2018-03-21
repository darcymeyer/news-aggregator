function process(jsondata) {
	console.log("process called");
	jsondata['stories'].forEach(function(story) {
		addStory(story);
	});
}

function addStory(story) {
	console.log("addStory called");
	var sourcetext = ""
	story['sources'].forEach(function(source) {
		console.log("SOURCE:", source)
		var st = '<tr>'+
                    '<td>'+
                        '<h4>'+source['title']+'</h4>'+
                        '<p><a href="'+source['link']+'">'+source['source']+'</a> '+
                            '<span style=color:#AAA>'+source['pubdate']+"</span>"+
                        '</p>'+
                        '<p>'+source['blurb']+'</p>'+
                    '</td>'+
                '</tr>';
        sourcetext = sourcetext+st;
	});
	var breaking = $("#breaking"); // we'll just handle breaking for now
	breaking.append(
		
		'<div class="story">'+
            '<div class="summary">'+
                '<h3>'+story['title']+'</h3>'+
                '<p>'+story['brief']+'</p>'+
            '</div>'+
            '<div class="sources">'+

                '<table cellspacing="0" cellpadding="5" border="1" width="100%">'+
                    sourcetext+
                '</table>'+

            '</div>'+
        '</div>'
		)
}
