$(function () {
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

