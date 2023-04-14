$(document).ready(function(){
    $('.loader').hide()
    $('#imgicon').click(function(){
       if(textarea.value == '')
       {
          alert("Enter Something............")
       }
       else{
//          alert(textarea.value)
        $('#interface').hide()
        $('.loader').show()
        $.getJSON('http://localhost:8000/openaiapi',{imagetext:textarea.value},function(data){
        })
        $( "#interface" ).delay( 8500 ).fadeIn( 400 );
        $( ".loader" ).delay( 8500 ).fadeOut( 400 );

       }
    })
    $('#searchicon').click(function(){
      if(textarea.value == '')
      {
         alert("Enter Something............")
      }
      else
      {
         asktextid.value=''
         $('#modal4').modal('open')
         $.getJSON('http://localhost:8000/asktext',{asktext:textarea.value},function(asktext){
//              alert(asktext.asktext)
         asktextid.value=asktext.asktext

         })
      }
    })
     $('#Generate').click(function(){
      if(inputcode.value == '')
      {
         alert("Enter Something............")
      }
      else
      {
         $.getJSON('http://localhost:8000/addcomment',{addcomment:inputcode.value},function(outputcode){
//         alert(outputcode.outputcode)
         outputcomment.value=outputcode.outputcode
//         alert(outputcode.value)

         })
      }
    })
 })