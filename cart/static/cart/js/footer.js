$(document).ready(function (){
  var button = $('footer').find('button')
  var btnMsg = $(button).find('.btn-msg').text()
  
  var checkout = 'CHECKOUT'
  //for some reason we can compare the "CHECKOUT" directly to the btnMsg (btnMsg=='CHECKOUT')
  
  $(button).click(function (){
    if(btnMsg==checkout){
      
      $.ajax({
        url:orderPreviewUrl,
        method:'POST',
        headers:{
          'X-CSRFToken':csrfToken,
          'Content-Type':'application/json'
        },
        data:JSON.stringify({
          'products':toCheckOut
        }),
        success:function(response){
          window.location.href=response.redirect_url
        },
        error:function(xhr,status){
          alert('error')
          toCheckOut = []
        }
      });
    }else{
      alert(btnMsg)
    }
  });
  
});