function open_modal_register(){
    $('#modal-register').modal('show');
}

function cancel_modal_register(){
  $('#modal-register').find('#id_username').val();
  $('#modal-register').find('#id_password1').val();
  $('#modal-register').find('#id_password2').val();
  $('#modal-register').modal('hide');
}
function clear_form(){
  $.each($('#id_form_register').find('input'), function(index, objects_i){
      $(objects_i[0]).removeAddClass('is-invalid');
      $(objects_i[0]).removeAttr('data_toggle');
      $(objects_i[0]).removeAttr('data-placement');
      $(objects_i[0]).removeAttr('title');
      $(objects_i[0]).tooltip('dispose');
  })
}

function send_register_modal() {
  $.each(response.errors, function(index, objects_i){
      $(objects_i).removeClass('is-invalid')
  })
  
  $.ajax({
    type: "POST",
    url: $('#id_form_register').atrr('action'),
    data: $('#id_form_register').serialize(),
    succes: function(response){
        if (response.status == 'ok'){
            alert('Congratulaciones!!');
            cancel_modal_register();
      }
        else{
            $.each(response.errors, function(index, objects_i){
                $('#id_' + objects_i[0]).addClass('is-invalid');
                $('#id_' + objects_i[0]).attr('data_toggle', 'tooltip');
                $('#id_' + objects_i[0]).attr('data-placement', 'right');
                $('#id_' + objects_i[0]).attr('title', objects_i[1]);
                $('#id_' + objects_i[0]).tooltip('show');

            })
      }
    }
  })
}
