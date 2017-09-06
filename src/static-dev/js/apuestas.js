function open_modal_register(){
    $('#modal-register').modal('show');
}

function cancel_modal_register(){
    clear_form();
    $('#modal-register').modal('hide');
    $.each($('#id_form_register').find('form-control'), function(index, objects_i){
        $(objects_i).val('');
    })
}

function clear_form(){
    $.each($('#id_form_register').find('input'), function(index, objects_i){
        $(objects_i).removeClass('is-invalid');
        $(objects_i).removeAttr('data-toggle');
        $(objects_i).removeAttr('data-placement');
        $(objects_i).removeAttr('title');
        $(objects_i).tooltip('dispose');
    })
}

function send_register_form(){
    clear_form();
    $.ajax({
        type: "POST",
        url: $('#id_form_register').attr('action'),
        data: $('#id_form_register').serialize(),
        success: function(response){
            if (response.status == 'ok'){
                alert('Congratulaciones!!!');
                cancel_modal_register();
            }
            else{
                $.each(response.errors, function(index, objects_i){
                    $('#id_' + objects_i[0]).addClass('is-invalid');
                    $('#id_' + objects_i[0]).attr('data-toggle', 'tooltip');
                    $('#id_' + objects_i[0]).attr('data-placement', 'right');
                    $('#id_' + objects_i[0]).attr('title', objects_i[1]);
                    $('#id_' + objects_i[0]).tooltip('show');
                })
            }

        }
    })
}
