    function total() {
        total1=0;
        total_count=0;
        $('.col07').each(function () {
            //获取数量
            count=$(this).prev().find('input').val();
            //获取单价
            price=$(this).prev().prev().text();
            //计算小计
            total0=parseFloat(count)*parseFloat(price);
            $(this).text(total0.toFixed(2));
            total1+=total0;
            total_count++;
        });
        //显示总计
        $('#gtotal').text(total1.toFixed(2));
        $('.total_count1'.text(total_count));
    }

$(function () {
    total();
    //加
    $('#add').click(function () {
        txt=$(this).next();
        txt.val(parseFloat(txt.val())+1).blur();
    });
    //减
    $('#minus').click(function () {
        txt=$(this).prev();
        txt.val(parseFloat(txt.val())-1).blur();
    });

    $('#num_show').blur(function () {
        count=$(this).val()
        if(count<=0){
            alert('请输入正确的数量');
            $(this).focus();
            return;
        }else if(count>=100){
            alert('数量不能超过100');
            $(this).focus();
            return;
        }
        cart_id=$(this).parents('.cart_list_td').attr('id');
        $.get('/cart/edit'+cart_id+'_'+count+'/', function (data) {
            if(data.ok==0){
                total();
            }else{
                $(this).val(data.ok);
            }
        })
    });

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
        }
    });
});

