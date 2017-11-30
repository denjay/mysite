// 自动换背景
var image = 0;
setInterval(function () {
    image = image<3 ? image+1 : 0;
    url = 'url(/static/images/top_login_' + image + '.jpg)'
    $('body').css({'backgroundImage': url});
},5000);

// 增加label动画
$('.form').find('input').on('blur focus', function (e) {
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

// 点击遮罩时隐藏
$('.shade, .message').click(function () {
    $('.shade, .message').hide();
})

// 弹出提示信息
function showMessage(str){
    $('.message b').text(str);
    $('.shade, .message').show();
    setTimeout(function (){
        $('.shade, .message').hide();
    }, 3000);
}

// 以下几个验证表单信息
$("#signup input").eq(1).blur(function () {
    if ($(this).val().length > 20) {
        $(this).next().fadeIn()
    }
    else {
        $(this).next().fadeOut()
    }
});

$("#signup input").eq(2).blur(function () {
    var label = $(this).next();
    var re = /^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}$/;
    if (re.test($(this).val())) {
        $.get('/user/check_email/', {"email": $(this).val()}, function (data){
            if (data.exist) {
                // console.log($(this));
                label.text('邮箱已存在，请更换').fadeIn();
            }
            else {
                label.fadeOut();
            };
        });
    }
    else {
        $(this).next().text('填写正确的邮箱格式').fadeIn();
    };
});

$("#signup input").eq(3).blur(function () {
    var re = /^[a-zA-Z0-9]{6,20}$/;
    if (re.test($(this).val())) {
        $(this).next().fadeOut()
    }
    else {
        $(this).next().fadeIn()
    }
});

// 提交表单
$('input[type=button]').click(function (){
    if ($('.field-wrap p:visible').length == 0 && $("#signup input").slice(1,4).val()) {
        $(this).parent().submit();
    }
    else{
        showMessage('请填写正确的信息！');
    }
});

// 切换显示login和signup表单
$('.tab a').on('click', function (e) {
    e.preventDefault();
    $(this).parent().addClass('active');
    $(this).parent().siblings().removeClass('active');
    target = $(this).attr('href');
    $('.tab-content > div').not(target).hide();
    $(target).fadeIn(600);
});

// 弹出登录和注册结果信息
if ($.cookie('message') == "register_successful") {
    showMessage('注册成功！请登录');
}
else if ($.cookie('message') == "register_failed") {
    showMessage('注册失败，请填写正确的信息');
    $('a[href="#signup"]').trigger('click');
}
else if ($.cookie('message') == "login_failed") {
    showMessage('登录失败，请重试');
};
$.removeCookie('message', { path: '/' });
