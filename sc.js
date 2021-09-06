$(document).ready(function(){
  
  $('.angle').click(function(e){
    $('.angle').toggleClass('arrow');
  });
  
  $('.angle').first().addClass('first');
  $('.angle').last().addClass('last');
  
});