
$(function(){
    // 为了滚动条的隐藏处理
    $('.home').width(innerWidth)

    var topSwiper = new Swiper('#topSwiper', {
        speed: 500, // 图片切换的速度
        autoplay: 2000, // 间隔时间
        pagination: '.swiper-pagination',   // 下标元素
        loop : true,    // 是否允许循环
        paginationClickable: true,  // 下标是否可以点击
    })

    var mustbuySwiper = new Swiper('#mustbuySwiper',{
        // 即一屏幕显示3个
        slidesPerView: 3,
        // 间隔
        spaceBetween: 2,
        // 可以循环
        loop: true,
    })
})
