from django.shortcuts import render

# Create your views here.

# 首页
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods, User



def home(request):
    # 轮播圖数据
    wheels = Wheel.objects.all()

    # 导航数据
    navs = Nav.objects.all()

    # 每日必抢
    mustbuys = Mustbuy.objects.all()

    # 部分商品
    shops = Shop.objects.all()
    shophead = shops[0]  # 头部区块
    shoptab = shops[1:3]  # 长条数据
    shopclass = shops[3:7]  # 分类
    shopcommend = shops[7:11]  # 推荐


    # 主体数据
    mainlist = Mainshow.objects.all()

    data = {
        'title':'首页',
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptab':shoptab,
        'shopclass':shopclass,
        'shopcommend':shopcommend,
        'mainlist':mainlist,
    }

    return render(request,'home.html',context=data)

# 山沟超市
def market(request,categoryid,childid,sortid):
    # 分类数据
    foodtypes = Foodtypes.objects.all()

    # 获取点击 历史
    typeIndex = int(request.COOKIES.get('typeIndex',0))
    categoryid = foodtypes[typeIndex].typeid

    # 分类中的子类
    # 子分类名称
    childstr = foodtypes.get(typeid=categoryid).childtypenames
    # childstr = Foodtypes.objects.get(typeid=categoryid).childtypenames
    # 子类数据
    childlist = []
    arr1 = childstr.split('#')
    for str in arr1:
        # 全部分类：0
        arr2 = str.split(':')
        obj = {'childname':arr2[0],'childid':arr2[1]}
        childlist.append(obj)

    if childid == '0':
        goodslist = Goods.objects.filter(categoryid=categoryid)
    else:
        goodslist = Goods.objects.filter(categoryid=categoryid,childcid=childid)

    # 排序
    if sortid =='1':
        goodslist = goodslist.order_by('productnum')
    elif sortid == '2':
        goodslist = goodslist.order_by('price')
    elif sortid == '3':
        goodslist = goodslist.order_by('-price')

    # 商品显示个数，需登陆
    token = request.session.get('token')
    cartlist = []
    if token:
        user = User.objects.get(userToken = token)
        # cartlist = Cart.objects.filter(userAccount = user.userAccount)


    data = {
        'title':'闪购超市',
        'foodtypes':foodtypes,
        'goodslist':goodslist,
        'childlist':childlist,
        "cartlist":cartlist,
        'categoryid':categoryid,
        'childid':childid,
    }
    return render(request,'market.html',context=data)

# 购物车
def cart(request):
    return render(request,'cart.html')

# 我的
def mine(request):
    return render(request,'mine.html')


def register(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    return None