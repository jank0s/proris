function load(){ 
	$("tbody > tr:odd").addClass("odd");

	var url = window.location.href;
	$("#yearSelect option").each(function(){
		$(this).attr('selected', false);
	    if(url.indexOf($(this).text()) !== -1)
	    {
			$(this).attr('selected', true);
			alert($(this).text());
			// $("#yearSelect").val($(this).text());
			$("#yearSelect").val("v kuraccc");
		}
	});
};