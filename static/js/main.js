$(document).ready(function(){


// $('*').not('.rfid-search-input').blur(function(){
//   setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
// })
//rfid search

$('.rfid-search-input').keyup(function(e){
  if(e.which == 13) {
        $.ajax({
          url:'/client/get/rfid',
          method:'post',
          data:{'rfid':$(this).val()},
          success:function(st){

            $('.client-info').html(st)
            $('.modal-part').hide()
            $('#client-form-update').show()
            $( ".datepicker" ).datepicker({"dateFormat":'dd/mm/yy'});
            $('.photo-input-wrapper label,.photo-input-wrapper input[type="checkbox"],.photo-input-wrapper a').hide()
            $('.photo-input-wrapper').html($('.photo-input-wrapper').html().replace('Currently:','').replace('Change:',''))
            $('.photo-label').show()
            $('#modal').modal('show');
            setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
          },
          error:function (xhr, ajaxOptions, thrownError){
              if(xhr.status==404) {
                setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
            }
        }
        })
    }
})

//auto focus rfid
$('.modal').on('hidden.bs.modal', function (e) {
  setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
  $('.marquer-seance').show()
})

$('.modal').on('shown.bs.modal', function (e) {
  setTimeout(function(){$('.rfid-search-input').val('').focus()},300)
})

//marquer seance

$('body').on('click','.marquer-seance',function(){

  $.get({
    url:'/client/seance/'+$('.client-id-hidden').html(),
    success:function(st){
      $('.marquer-seance').hide()
      var iframe = document.getElementById('presence');
      iframe.src = iframe.src;

    }

  })
})


//modal navigation
$('body').on('click','.modal-navigate',function(){
  $('.modal-part').hide()
  $($(this).attr('data-show')).show()
})

//auto calcul des prix lors de l'abonement

$('body').on('change','#id_abonnement-forfait,#id_abonnement-nbr_mois,#id_abonnement-remise',function(){
  var unitaire=parseInt($("#id_abonnement-forfait option:selected").text().split(" ")[4])
  var unite=$('#id_abonnement-nbr_mois').val()
  var remise=$('#id_abonnement-remise').val()
  $('#id_abonnement-montant,#id_abonnement-versement').val(unitaire*unite-remise)

})

})
