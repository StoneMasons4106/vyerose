$(window).resize(function(){
    var windowHeight = $(window).height();
    var documentHeight = $(document).height();
        
    if (documentHeight == windowHeight) {
        $("#footer").css({'position': 'fixed', 'bottom': '0px', 'width': '100%'})
    }
})