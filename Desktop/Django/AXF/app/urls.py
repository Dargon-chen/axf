from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),  # 首页

    url(r'^home/$', views.home, name='home'),  # 首页

    url(r'^market/(\d+)/(\d+)/(\d+)$', views.market, name='market'),  # 山沟超市
    url(r'^cart/$', views.cart, name='cart'),  # 购物车
    url(r'^mine/$', views.mine, name='mine'),  # 我的

    # 注册
    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', views.login, name='login'),  # 登录
    url(r'^logout/$', views.quit, name='logout'),  # 退出登录
    url(r'checkuser/$', views.checkuser, name='checkuser'),  # 用户名验证

    # 添加到购物车
    url(r'^addtocart/$', views.addtocart, name='addtocart'),

    # 删除
    url(r'^deltocart/$',views.deltocart,name='deltocart'),

    # 修改选中状态
    url(r'^changecartstatus/$',views.changecartstatus,name='changecartstatus'),

    # 全选
    url(r'^changecartselect/$',views.changecartselect,name='changecartselect'),

]