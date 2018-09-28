$(function(){
    $('.cart').width(innerWidth)

    total()
    // 商品，讯中，状态
    $('.cart .confirm-wrapper').click(function(){
        var cartid = $(this).attr('cartid')
        var $that =$(this)

        $.get('/app/changecartstatus',{'cartid':cartid},function(response){
            console.log(response)
            if (response['status']==1){
                var isselect = response['isselect']
                $that.attr('isselect',isselect)
                // 先清空
                $that.children().remove()
                if (isselect){  //选中
                    $that.append('<span class="glyphicon glyphicon-ok"></span>')
                }else{   //未选中
                    $that.append('<span class="no"></span>')
                }
            }else{

            }

            total()

        })
    })

    // 全选/取消全讯
    $('.cart .bill .all').click(function(){
        var isall = $(this).attr('isall')
        isall = (isall == 'false')?true:false
        $(this).attr('isall',isall)

        // 自身状态
        $(this).children().remove()
        if (isall){  // 全选
            $(this).append('<span class="glyphicon glyphicon-ok"></span>').append('<b>全选</b>')
        }else{  //取消全选
            $(this).append('<span class="no"></span>').append('<b>全选</b>')
        }

        // 发起ajax请求
        $.get('/app/changecartselect/',{'isall':isall},function(response){
            console.log(response)
            if(response['status']==1){
                // 便利
                $('.confirm-wrapper').each(function(){
                    $(this).attr('isselect',isall)
                    $(this).children().remove()
                    if(isall){
                        $(this).append('<span class="glyphicon glyphicon-ok"></span>')
                    }else{
                        $(this).append('<span class="no"></span>')
                    }
                })
                total()

            }else{

            }
            total()
        })

    })

    // 计算中枢
    function total(){
        var sum = 0

        $('.goods').each(function(){
            var $confirm = $(this).find('.confirm-wrapper')
            var $content = $(this).find('.content-wrapper')

            // 选中，计算
            if ($confirm.find('.glyphicon-ok').length){
                var price = parseInt($content.find('.price').attr('str'))
                var num = parseInt($content.find('.num').attr('str'))
                sum = sum+price*num
                console.log('price'+price)
                console.log('num'+num)
            }


        })

        $('.bill .total b').html(sum)


    }

    // 下单
    $('#generate-order').click(function(){
        $.get('/app/generateorder/',function(response){
            console.log(response)
            if(response['status']=='1'){
                var orderid=response['orderid']
                window.open('/app/orderinfo/?orderid='+orderid,target='_self')
            }
        })
    })

})