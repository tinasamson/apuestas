function open_modal_register(){
    $('#modal_register').modal('show');
}

function cancel_modal_register(){
  $('modal_register').find('#id_username').val();
  $('modal_register').find('#id_password1').val();
  $('modal_register').find('#id_password2').val();
  $('modal_register').model('hide');
}

function send_register_modal() {

  $.ajax({
    type: "POST",
    url: $('#id_form_register').atrr('action'),
    data: $('#id_form_register').serialize(),
    succes: function(response){
      alert(response)
    }
  })
}
