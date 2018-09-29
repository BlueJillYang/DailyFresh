$(function () {
    total1=0;
    total_count=0;
    $('.col07').each(function () {
        amount=$(this).prev().text();
        price=$(this).prev().prev().text();
        total0=parseFloat(amount)*parseFloat(price)
        $(this).text(total0.toFixed(2)+'元');
        total1+=total0
        total_count++;
    });
    $('#gtotal').text(total1.toFixed(2));
    $('#total_count1').text(total_count);
    translate=$('#transit').text();
    final=total1+parseFloat(translate);
    $('#final_total').text(final.toFixed(2));

    $('#order_btn').click(function () {
        confirm('是否前往支付页面');
    });
});