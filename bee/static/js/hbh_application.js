function testfunc(params){
    console.info("hola", params);
}

$( document ).ready(function() {
    $(document).on("submit", ".ajax-form-data", function(evt){
        evt.preventDefault();

        var form = $( this );
        var posting = $.post(form.attr("action"), form.serialize());

        posting.done(function(data, status, xhr) {
            /*
            TODO colocar el elemento en su posicion, quizas retornando un json con la funcion
            TODO a invocar y los datos de parámetro
            TODO window[functionName](parameters)
            */
            console.info(data, status, status);
            window[data.function](data.params);
            if(form.hasClass("cbx-close"))
                $.colorbox.close();
        });
        posting.fail(function(data, status, xhr) {
            /*
            TODO colocar el error en su posicion, quizas retornando un json con la funcion
            TODO a invocar y los datos de parámetro
            TODO window[functionName](parameters)
            */
            console.info(data, status, xhr );
        });
    });

    $(document).on("submit", ".ajax-form-script", function(evt){
        evt.preventDefault();
        var form = $( this );
        var posting = $.post(form.attr("action"), form.serialize());
    });
});