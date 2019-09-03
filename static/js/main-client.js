$(document).ready(function(){

  $('body').on('click','tr',function(){
    var id=$(this).attr('data-id')
    $.get({
      url:'update/'+id,
      success:function(st){
        $('.client-info').html(st)
        $('.update-client-form').attr('action','update/'+id)
        $( ".datepicker" ).datepicker({"dateFormat":'dd/mm/yy'});
        $('.photo-input-wrapper label,.photo-input-wrapper input[type="checkbox"],.photo-input-wrapper a').hide()
        $('.photo-input-wrapper').html($('.photo-input-wrapper').html().replace('Currently:','').replace('Change:',''))
        $('.photo-label').show()
      }
    })
  })

    $( ".datepicker" ).datepicker({"dateFormat":'dd/mm/yy'});


})
