$(function(){
    $('.order').width(innerWidth)


    $('#alipay').click(function(){
        var orderid = $(this).attr('orderid')
        $.get('/app/changeorderstatus/',{'orderid':orderid,'status':2},function(response){
            console.log(response)
            window.open('/app/mine/',target='_self')
        })
    })

})