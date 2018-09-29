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
        }else if(count>200){
            alert('土豪啊!')
        };
        //alert(parseFloat($('#gtotal').text())*20);
        //判断库存
        $('#reserve').each(function () {
            reserve=parseFloat($(this).text());
            gname=$(this).parent().prop('id');
            count=$(this).parent().next().next().next().find('input').val();
            if(parseFloat(reserve) < parseFloat(count)){
                alert(gname+'库存:'+$(this).text()+', 库存不足,抱歉!');
                //$(this).parent().next().next().next().find('input').val(reserve);
                $('#pay_btn').attr('disabled', true);
            }
        });

        //计算小计和总计
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
            if($(this).prev().prev().prev().prev().prev().prev().children().prop('checked')){
                total1+=total0;
                total_count++;
            }
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
                    if($(this).prev().prev().prev().prev().prev().prev().children().prop('checked')){
                        total1+=total0;
                        total_count++;
                    }
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

    //遍历选中对象计算总价
            //alert($(this).parents('.cart_list_td').prop('id'));
            //alert($(this).parents().next().next().next().next().next().next().text());
            //x=$(this).parents().next().next().next().next().next().next().text();
            //alert(x);
    // $(function () {
    //     total1=0;
    //     total_count=0;
    //     $(':checkbox:not(#check_all)').each(function () {
    //         oPrice=$(this).next().next().next().next().text();
    //         oCount=$(this).next().next().next().next().next().find('input').val();
    //         if($(this).prop('checked')){
    //             count=oCount.val();
    //             price=oPrice.text();
    //             alert(oCount);
    //             alert(oPrice);
    //             total0=parseFloat(count)*parseFloat(price);
    //             total1+=total0;
    //             total_count++;
    //         }
    //     });
    //     $('#gtotal').text(total1.toFixed(2));
    //     $('#total_count1').text(total_count);
    //
    // });
    $(':checkbox').click(function () {
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
            if($(this).prev().prev().prev().prev().prev().prev().children().prop('checked')){
                total1+=total0;
                total_count++;
            }
        });
        //显示总计
        $('#gtotal').text(total1.toFixed(2));
        $('#total_count1').text(total_count);
    });

    //点击立即结算 get方法请求域名 ?cart_id=...&cart_id=...
    $('#pay').click(function () {
        //域名请求
        cid_list='';
        $('.col01').each(function () {
            if($(this).children().prop('checked')){
                if($(this).children().prop('id')=='check_all'){
                    return;
                }
                cid=$(this).parents('.cart_list_td').attr('id');
                cid_list+=('cart_id='+cid+'&')
            }
        });
        //alert('/order/?'+cid_list);
        cid_list=cid_list.substring(0,cid_list.length-1);
        if(cid_list==''){
            alert('买点吧,亲!');
            return;
        }
        $(this).children().prop('href','/order/?'+cid_list);
    });
});

