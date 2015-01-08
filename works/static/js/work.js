$(function() {
    $('#albums').sortable({
        cursor: 'crosshair',
        update: function(event, ui) {
            ids = [];
            $('.album', event.target).each(function(i, item){
                ids.push($(item).data('id'));
            });
            $.ajax({
                url: $(event.target).data('url'),
                data: {'ids': ids.join(',')}
            });
        },
        items: '>li:not(.ui-state-disabled)',
    });

    $('#albums .works').sortable({
        cursor: 'crosshair',
        scroll: true,
        update: function(event, ui) {
            if (ui.item.parent()[0] != event.target) return;
            ids = [];
            $('.work', event.target).each(function(i, item){
                ids.push($(item).data('id'));
            });
            $.ajax({
                url: $(event.target).data('url'),
                data: {
                    'ids': ids.join(','),
                    'album_id': ui.item.parent().data('id'),
                }
            });
        },
        connectWith: '.works',
        placeholder: 'ui-state-highlight',
        items: '>li:not(.ui-state-disabled)',
    });

    $('.toggle-work').click(function(){
        var $this = $(this);
        $.getJSON($(this).data('url'), function(response){
            if (response.visible) {
                $('span', $this).prop('class', 'glyphicon glyphicon-eye-open');
            } else {
                $('span', $this).prop('class', 'glyphicon glyphicon-eye-close');
            }
        });
    });
});
