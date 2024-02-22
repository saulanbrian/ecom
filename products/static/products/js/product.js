$(document).ready(function(){
  $('.button-container').each(function(){
    $(this).children().first().click(function(){
      $(this).text('added');
      
      
      $.ajax({
        url:addToCartUrl,
        method:'POST',
        headers:headers,
        data:{
          any:'data'
        },
        success:function(response){
          alert(response.message);
        },
        error:function(xhr,error,status){
          
        console.log(error)
          
          var r = xhr.responseJSON;
          
          console.log(error)
          console.log(r.message)
        }
        
      });
      
    });
  });
});