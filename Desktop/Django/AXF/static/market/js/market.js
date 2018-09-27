// $(function () {
//     // 为了滚动条的隐藏处理
//     $('.market').width(innerWidth)
//
//
//     // 读取Storage中的typeid
//     var typeid = window.sessionStorage.getItem('typeid')
//     if(!typeid){    // 空时
//         $('.type-slider li:first').addClass('action')
//     } else { // 根据下标设置对应的li
//         $('.type-slider li').eq(typeid).addClass('action')
//     }
//
//     // 获取到对应页面url
//     href = $('.type-slider li.action a').attr('href')
//     // 跳转到登录页面
//     url = 'http://' + window.location.host + href
//     // /market/104749/0/0/
//     if (window.location.pathname != href){
//          window.location.href = url
//     }
//
//     // 分类点击操作(点击后页面会重新刷新，导致效果没出来)
//     $('.type-slider li').click(function () {
//         // $('.type-slider .action').removeClass('action')
//         // $(this).addClass('action')
//         // 记录即可
//         window.sessionStorage.setItem('typeid', $(this).index());
//     })
//
//     // 全部类型
//     var alltypebtn = false
//     var showsortbtn = false
//     $('#alltypebtn').click(function () {
//         alltypebtn = !alltypebtn
//         if(alltypebtn){
//             $('.main-content .type-child').show()
//             $('#alltypebtn > i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
//         } else {
//             $('.main-content .type-child').hide()
//             $('#alltypebtn > i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
//         }
//     })
//     $('#showsortbtn').click(function () {
//         alltypebtn = !alltypebtn
//         if(alltypebtn){
//             $('.main-content .sort-view').show()
//             $('#showsortbtn > i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
//         } else {
//             $('.main-content .sort-view').hide()
//             $('#showsortbtn > i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
//         }
//     })
//
//     // 分类点击后，显示隐藏处理
//     $('.main-content .type-child').click(function () {
//         alltypebtn = false
//         $(this).hide()
//         $('#alltypebtn > i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
//     })
//     $('.main-content .sort-view').click(function () {
//         showsortbtn = false
//         $(this).hide()
//         $('#showsortbtn > i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
//     })
//
//
//     // 按钮默认是否显示问题
//     $('.content-wrapper .bt-wrapper .glyphicon-minus').hide()
//     $('.content-wrapper .bt-wrapper .num').hide()
//     $('.content-wrapper .bt-wrapper .num').each(function () {
//         if (parseInt($(this).html())){   // 有内容，说明有值
//             $(this).show()
//             $(this).prev().show()
//         }
//     })
//
//
//     // 添加商品
//     $('.content-wrapper .bt-wrapper .glyphicon-plus').click(function () {
//         num = $(this).prev().html()
//         num++;
//         $(this).prev().show()
//         // $(this).prev().html(num)
//         $(this).prev().prev().show()
//         current = $(this)
//
//         // 发起ajax请求
//         productid = $(this).attr('productid')
//         // flag:1 表示添加数据
//         $.post('/changecart/', {'flag': 1,'productid':productid},function (data) {
//             if(data.status == 1){ // 添加成功
//                 // 添加成功，显示对应的个数
//                 console.log(data.content)
//                 current.prev().html(num)
//             } else if(data.status == -1) {    // 未登录操作
//                 // 跳转到登录页面
//                 url = 'http://' + window.location.host + data.content
//                 window.location.href = url
//             } else if(data.status == -2){   // 没有库存
//                 return
//             }
//         })
//     })
//     // 删减商品
//     $('.content-wrapper .bt-wrapper .glyphicon-minus').click(function () {
//         num = $(this).next().html()
//         num--;
//         // $(this).next().html(num)
//         current = $(this)
//
//         productid = $(this).attr('productid')
//         $.post('/changecart/', {'flag':-1, 'productid':productid},function (data) {
//             if(data.status == '1'){ // 操作成功
//                 // $('.content-wrapper .bt-wrapper .num').html(data.content)
//                 current.next().html(num)
//             }
//         })
//
//         if (num == 0){
//             $(this).next().hide()
//             $(this).hide()
//         }
//     })
// })


$(function () {
    // 滚动条处理
    $('.market').width(innerWidth)


    // 获取下标 typeIndex
    typeIndex = $.cookie('typeIndex')
    console.log(typeIndex)
    if(typeIndex){  // 存在，对应分类
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    } else {    // 不存在，默认就是热榜
        $('.type-slider .type-item:first').addClass('active')
    }


    // 侧边栏点击处理 (页面会重新加载)
    $('.type-slider .type-item').click(function () {
        // 保存下标
        // console.log($(this).index())
        // 保存下标 cookie
        $.cookie('typeIndex', $(this).index(),{exprires:3, path:'/'})
    })


    var allbtn = false
    var sortbtn = false
    $('#alltypebtn').click(function(){
        allbtn = !allbtn
        if(allbtn){
            $('.bounce-view.type-child').show()
            $('#alltypebtn i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
            if(sortbtn){
                 sortbtn = false
                 $('.bounce-view.sort-view').hide()
                 $('#showsortbtn i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
            }
        }else{
            $('.bounce-view.type-child').hide()
            $('#alltypebtn i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')

        }
    })

    $('#showsortbtn').click(function(){
        sortbtn = !sortbtn
        if(sortbtn){
            $('.bounce-view.sort-view').show()
            $('#showsortbtn i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
            if(allbtn){
                allbtn=false
                $('.bounce-view.type-child').hide()
                $('#alltypebtn i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
            }
        }else{
            $('.bounce-view.sort-view').hide()
            $('#showsortbtn i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
        }
    })

    $('.bounce-view').click(function(){
        if(sortbtn){
            sortbtn = false
            $('.bounce-view.sort-view').hide()
            $('#showsortbtn i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
        }
        if(allbtn){
            allbtn=false
            $('.bounce-view.type-child').hide()
            $('#alltypebtn i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
        }

    })



})