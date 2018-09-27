from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$',views.home,name='home'),   # 首页

    url(r'^home/$',views.home,name='home'),  # 首页

    url(r'^market/(\d+)/(\d+)/(\d+)$',views.market,name='market'),   #山沟超市
    url(r'^cart/$',views.cart,name='cart'),  # 购物车
    url(r'^mine/$',views.mine,name='mine'),  # 我的

    url(r'^register/$',views.register,name='register'),

]