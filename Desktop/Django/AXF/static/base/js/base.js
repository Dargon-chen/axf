$(function(){

    // 设计高宽度320ｐｘ
    //　默认自体大小为16ｐｘ
    //　1rem =16px (根据body的自体大小)
    document.documentElement.style.fontSize=innerWidth / 320*16+'px'

    $('#content').width(innerWidth + 20)
})