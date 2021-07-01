$(document).ready(function()
{
    $("#comunidades").height($("#noticiasCarousel").height());
    
    $(window).resize(function()
    {
        $("#comunidades").height($("#noticiasCarousel").height());
    });
});

$('.share-button').click(function() {
    if (navigator.share) {
      navigator.share({
        title: $(this).prev().attr('data-nombre'),
        url: window.location.origin + $(this).prev().attr('href').replace('../..','').replace('/miembro','')
      }).then(() => {
        console.log($(this).closest('h6'));
    })
    .catch(console.error);
    } else {
    console.log($(this).closest('h6'));
    // fallback
    }
  });