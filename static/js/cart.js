$(function () {
    //刷新时个数全为1
    $(window).load(function () {
        $('.num_show').focus();
    });

    $('.add').click(function () {
        //alert($('.add').next().val());
        txt=$(this).next();
        txt.val(parseFloat(txt.val())+1).blur();
    });

    $('.minus').click(function () {
        //alert($('.minus').prev().val());
        txt=$(this).prev();
        txt.val(parseFloat(txt.val())-1).blur();
    });

    $('.num_show').blur(function () {
        count=$(this).val();
        //alert(count);
        if(count<1){
            alert('买一个吧,亲! 再想想');
            $(this).val(1);
            return;
        }else if(count>100){
            alert('土豪啊,膜拜!')
        };
        //alert(parseFloat($('#gtotal').text())*20);
        total1=0;
        total_count=0;
        $('.col07').each(function () {
            //获取数量
            count=$(this).prev().find('input').val();
            //获取单价
            price=$(this).prev().prev().text();
            //计算小计
            total0=parseFloat(count)*parseFloat(price);
            $(this).text(total0.toFixed(2)+'元');
            total1+=total0;
            total_count++;
        });
        //显示总计
        $('#gtotal').text(total1.toFixed(2));
        $('#total_count1').text(total_count);

        //显示
        cart_id=$(this).parents('.cart_list_td').attr('id');
        count=$(this).val();
        $.get('/cart/edit'+cart_id+'_'+count+'/', function (data) {
            if(data.ok==0){
                total1=0;
                total_count=0;
                $('.col07').each(function () {
                    //获取数量
                    count=$(this).prev().find('input').val();
                    //获取单价
                    price=$(this).prev().prev().text();
                    //计算小计
                    total0=parseFloat(count)*parseFloat(price);
                    $(this).text(total0.toFixed(2)+'元');
                    total1+=total0;
                    total_count++;
                });
                //显示总计
                $('#gtotal').text(total1.toFixed(2));
                $('#total_count1').text(total_count);

            }else{
                $(this).val(data.ok);
            };
        })
    });

    //全选全消
    $('#check_all').click(function () {
        state=$(this).prop('checked');
        $(':checkbox:not(#check_all)').prop('checked',state);
    });

    $(':checkbox:not(#check_all)').click(function () {
        if($(this).prop('checked')){
            if($(':checked').length+1==$(':checkbox').length){
                $('#check_all').prop('checked', true);
            }
        }else{
            $('#check_all').prop('checked', false);
        };
    });

    $(':checkbox:not(#checkall)').each(function () {
        if($(this).prop('checked')){
            //alert($(this).parents('.cart_list_td').prop('id'));
            alert($(this).parents().next().next().next().next().next().next().attr('class'));
        }
    });

});

