// $(function() {
//     // 为了滚动条的隐藏处理
//     $('.register').width(innerWidth)
//
//     // 账号验证
//     $('#accunt').bind('focus',function () {
//         $('#accunterr').css('display', 'none')
//         $('#checkerr').css('display', 'none')
//     })
//
//     $('#accunt').bind('blur',function () {
//         str = $(this).val()
//         // 显示错误
//         if (str.length<6 || str.length>12){
//             $('#accunterr').css('display', 'block')
//         } else {
//             // 发起请求，账号是否存在
//             $.post('/checkuserid/',{'userid': str},function (data) {
//                 if (data.status == 'error'){
//                     $('#checkerr').css('display', 'block')
//                 }
//                 console.log(data)
//             })
//         }
//     })
//
//
//     // 密码验证
//     $('#pass').bind('focus',function () {
//         $('#passerr').css('display', 'none')
//         $('#passerr').css('display', 'none')
//     })
//
//     $('#pass').bind('blur',function () {
//         str = $(this).val()
//         // 显示错误
//         if (str.length<6 || str.length>12){
//             $('#passerr').css('display', 'block')
//         }
//     })
//
//     $('#passwd').bind('focus',function () {
//         $('#passwderr').css('display', 'none')
//         $('#passwderr').css('display', 'none')
//     })
//
//     $('#passwd').bind('blur',function () {
//         str = $(this).val()
//         // 显示错误
//         if (str.length<6 || str.length>12){
//             $('#passwderr').css('display', 'block')
//         }
//     })
//
// })



$(function () {
    $('.register').width(innerWidth)


    // 失去焦点
    // 用户名输入完成，发起ajax请求，验证该用户名是否能用
    $('#account').blur(function () {
        $.get('/app/checkuser/', {'account':$(this).val()}, function (response) {
            console.log(response)
            if(response['status'] == '-1'){ // 用户存在
                $('#accounterr').show().html(response['msg'])
            } else {
                $('#accounterr').hide()
            }
        })
    })
})