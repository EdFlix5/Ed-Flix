if ($(window).innerHeight() > $('.footer').offset().top) {
    var offset = $(window).innerHeight() - $('.footer').outerHeight();
    $('.footer').css('margin-top', parseInt($('.footer').css('marginTop'), 10) + offset - $('.footer ').offset().top);
}