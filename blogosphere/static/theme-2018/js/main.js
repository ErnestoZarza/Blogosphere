
var header = document.getElementById("header-area");
var sticky = header.offsetHeight;

$().ready(function() {
    var $scrollingDiv = $("#scrollingDiv");
    var $nav = $('#navbar_sticky');
    var $site = $('#container-site');

    $(window).resize(function () {
        sticky = header.offsetHeight;
        if ($(window).width()+17 < 991 ) {
            document.getElementById("scrollingDiv").style.top = "auto";

        }
    });

    $(".dropdown").hover(function () {
        if ($(window).width()+17 > 991 ) {
            jQuery(this).children(".dropdown-menu").addClass('show');
        }
    }, function () {
        if ($(window).width()+17 > 991 ) {
            jQuery(this).children(".dropdown-menu").removeClass('show');
        }
    });

    if ($(window).width()+17 > 991 ) {
        $scrollingDiv
            .stop()
            .animate({"top": ($(window).scrollTop() + sticky + 56) + "px"}, "slow" );
    }
    if (window.pageYOffset >= sticky) {
        $nav.addClass('fixed-top');
        $site.addClass('fixed-container');
    } else {
        $nav.removeClass('fixed-top');
        $site.removeClass('fixed-container');
    }

    $(window).scroll(function(){
        if ($(window).width()+17 > 991 ) {
            $scrollingDiv
                .stop()
                .animate({"top": ($(window).scrollTop() + sticky + 56) + "px" }, "slow" );
        }
        if (window.pageYOffset >= sticky) {
            $nav.addClass('fixed-top');
            $site.addClass('fixed-container');
        } else {
            $nav.removeClass('fixed-top');
            $site.removeClass('fixed-container');
        }
    });
});