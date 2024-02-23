$(document).ready(function(){
  var addToCart = $('.button-container');
  
  $(addToCart).each(function(){
    $(this).children().first().click(function(){
      var p = $(this).closest('.product');
      var product_id = $(p).attr('id');
      
      $.ajax({
        url:addToCartUrl,
        method:'POST',
        headers:{
          'X-CSRFToken':csrfToken
        },
        data:{
          id_:product_id
        },
        success:function(response){
          alert(response.message)
        },
        error:function(xhr,status){
          var response = xhr.responseJSON;
          
          alert(response.message)
        }
      });
      
    });
  });
  
  
});