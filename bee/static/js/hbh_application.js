$( document ).ready(function() {
    $(document).on("submit", ".ajax-form-data", function(evt){
        evt.preventDefault();

        var form = $( this );
        var posting = $.post(form.attr("action"), form.serialize());
        posting.done(function(data, status, xhr) {
            console.info(data, status, xhr);
        });
        posting.fail(function(data, status, xhr) {
            console.info(data, status, xhr );
        });
    });

    $(document).on("submit", ".ajax-form-script", function(evt){
        evt.preventDefault();
        var form = $( this );
        var posting = $.post(form.attr("action"), form.serialize());
        posting.fail(function(data, status, xhr) {
            console.info(data, status, xhr );
        });
    });
});