$(function () {
    $('#login1').click(function () {
        if($('#username1').text()){
            if(confirm('已登录账户,是否继续前往登录/注册页面')){
                submit();
            }else {
                return false;
            }
        }
    });
    $('#register1').click(function () {
        if($('#username1').text()){
            if(confirm('已登录账户,是否继续前往登录/注册页面')){
                submit();
            }else {
                return false;
            }
        }
    });
    $('#user_center1').click(function () {
        if($('#username1').text()==''){
            if(confirm('请先登录,是否继续前往登录页面')){
                submit();
            }else {
                return false;
            }
        }
    });
    $('#cart1').click(function () {
        if($('#username1').text()==''){
            if(confirm('请先登录,是否继续前往登录页面')){
                submit();
            }else {
                return false;
            }
        }
    });
    $('#user_center_order1').click(function () {
        if($('#username1').text()==''){
            if(confirm('请先登录,是否继续前往登录页面')){
                submit();
            }else {
                return false;
            }
        }
    });
});