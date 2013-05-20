function load(){ 
	$("tbody > tr:odd").addClass("odd");

	var url = window.location.href;
	$("#yearSelect option").each(function(){
	    if(url.indexOf($(this).text()) !== -1)
	    {
			$(this).attr('selected', 'selected');
		}
	});
};