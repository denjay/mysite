$('.form').find('input, textarea').on('blur focus', function (e) {

    var $this = $(this),
        label = $this.prev('label');

        if (e.type === 'focus') {
            label.addClass('active highlight');
        } 

        if (e.type === 'blur') {
            if ($this.val() === '') {
                label.removeClass('active highlight');
            } 
            else {
                label.removeClass('highlight');
            }
        }

});

$('.tab a').on('click', function (e) {
    e.preventDefault();
    $(this).parent().addClass('active');
    $(this).parent().siblings().removeClass('active');
    target = $(this).attr('href');
    $('.tab-content > div').not(target).hide();
    $(target).fadeIn(600);
});

if ($.cookie('message') == "register_successful") {
    alert('注册成功！请登录');
}
else if ($.cookie('message') == "register_failed") {
    alert('注册失败，请填写正确的信息');
    $('a[href="#signup"]').trigger('click');
}
else if ($.cookie('message') == "login_failed") {
    alert('登录失败，请重试');
};
$.removeCookie('message', { path: '/' });
