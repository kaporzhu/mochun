$(document).ready(function(){
    $('a.confirm').click(function(){
        if(confirm($(this).data('confirm'))) {
            location.href = $(this).data('url');
        }
    });

    $('.album-icon').click(function(){
        $('#album-works').load($(this).data('url'));
    });
});