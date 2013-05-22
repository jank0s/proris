function load(){
        $("tbody > tr:odd").addClass("odd");

        var url = window.location.href;
        $("#yearSelect option").each(function(){
            $(this).attr('selected', false);
            if(url.indexOf($(this).text()) !== -1)
            {
                $(this).prop('selected', true).change();
            }
        });
};