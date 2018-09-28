import hashlib
import os
import uuid

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.

# 首页


from AXF import settings
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods, User, Cart, Order, OrderGoods


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

    return render(request, 'home/home.html', context=data)

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
        cartlist = Cart.objects.filter(user = user).exclude(number=0)


    data = {
        'title':'闪购超市',
        'foodtypes':foodtypes,
        'goodslist':goodslist,
        'childlist':childlist,
        "cartlist":cartlist,
        'categoryid':categoryid,
        'childid':childid,
    }
    return render(request, 'market/market.html', context=data)

# 购物车
def cart(request):

    token = request.session.get('token')
    if token:   # 已经登陆
        user = User.objects.get(userToken = token)
        carts = Cart.objects.filter(user = user).exclude(number=0)
        responseData = {
            'title':'购物车',
            'carts':carts,
        }




    return render(request, 'cart/cart.html',context=responseData)

# 我的
def mine(request):
    token = request.session.get('token')


    responseData = {
        'title': '我的',
        'payed' : 0,
        'wait_pay':0
    }

    if token:   # 登录
        user = User.objects.get(userToken=token)
        responseData['name'] = user.userName
        responseData['rank'] = user.userRank
        responseData['img'] = '/static/uploads/' + user.userImg
        responseData['islogin'] = True

        # 获取订单信息
        orders = Order.objects.filter(user = user)
        payed = 0 # 已付款
        wait_pay = 0 # 待付款

        for order in orders:
            if order.status == 1:
                wait_pay += 1
            elif order.status == 2:
                payed +=1

        responseData['payed']=payed
        responseData['wait_pay']=wait_pay

    else:       # 未登录
        responseData['name'] = '未登录'
        responseData['rank'] = '无等级(未登录)'
        responseData['img'] = '/static/uploads/temp.jpeg'
        responseData['islogin'] = False



    return render(request, 'mine/mine.html', context=responseData)

# 注册
def register(request):
    if request.method == 'POST':
        user = User()
        user.userAccount = request.POST.get('account')
        user.userPasswd = generate_password(request.POST.get('password'))
        user.userName = request.POST.get('name')
        user.userPhone = request.POST.get('tel')
        user.userAdderss = request.POST.get('address')
        user.userRank=0

        # 头像
        imgName = user.userAccount + '.png'
        imgPath = os.path.join(settings.MEDIA_ROOT, imgName)
        print(imgPath)
        file = request.FILES['file']
        print(file)
        with open(imgPath,'wb') as fp:
            print(1)
            for data in file.chunks():
                fp.write(data)
        user.userImg = imgName

        # token
        user.userToken = str(uuid.uuid5(uuid.uuid4(), 'register'))

        # 保存到数据库
        user.save()

        # 状态保持
        request.session['token'] = user.userToken

        # 重定向
        return redirect('app:mine')

    elif request.method == 'GET':
        return render(request, 'mine/register.html')


# 密码
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()

# 退出登录
def quit(request):
    # request.session.flush()
    logout(request)
    return redirect('app:mine')

# 登录
def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')

        try:
            user = User.objects.get(userAccount=account)
            if user.userPasswd != generate_password(password):    # 密码错误
                return render(request, 'mine/login.html', context={'error': '密码错误!'})
            else:   # 登录成功
                # 更新token
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                user.save()
                # 状态保持
                request.session['token'] = user.userToken
                return redirect('app:mine')
        except:
            return render(request, 'mine/login.html', context={'error':'用户名有误，请检查后输入!'})

    elif request.method == 'GET':
        return render(request, 'mine/login.html')


def checkuser(request):
    account = request.GET.get('account')
    try:
        user = User.objects.get(userAccount=account)
        return JsonResponse({'msg':'用户名存在!', 'status':'-1'})
    except:
        return JsonResponse({'msg':'用户名可用!', 'status':'1'})


def addtocart(request):
    # goodsid
    goodsid = request.GET.get('goodsid')
    responseData = {
        'msg':'',
        'status':'',
        'number':0
    }

    token = request.session.get('token')
    if token:   # 登陆
        user = User.objects.get(userToken=token)
        goods = Goods.objects.get(pk=goodsid)
        carts = Cart.objects.filter(user=user).filter(goods=goods)
        if carts.exists():
            cart = carts.first()
            cart.number = cart.number+1
            if goods.storenums < cart.number:
                cart.number = goods.storenums
            cart.save()
            responseData['msg'] = '添加成功'
            responseData['status'] = 1
            responseData['number'] = cart.number
            return JsonResponse(responseData)
        else:
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.number = 1

            cart.save()

            responseData['msg']='添加成功'
            responseData['status'] = 1
            responseData['number'] = cart.number
            return JsonResponse(responseData)
    else:  # 未登录
        # ajax不能重定向
        # return render(request,'mine/login.html')
        responseData['msg']='请登陆后操作'
        responseData['status']=-1;
        return JsonResponse(responseData)



def deltocart(request):
    # goodsid
    goodsid = request.GET.get('goodsid')
    responseData = {
        'msg':'',
        'status':'',
        'number':0
    }

    token = request.session.get('token')


    user = User.objects.get(userToken=token)
    goods = Goods.objects.get(pk=goodsid)
    carts = Cart.objects.filter(user=user).filter(goods=goods)
    cart = carts.first()
    cart.number = cart.number-1

    cart.save()

    responseData['msg'] = '删除成功'
    responseData['status'] = 1
    responseData['number'] = cart.number
    return JsonResponse(responseData)


def changecartstatus(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    responseData = {
        'msg':'修改状态成功',
        'status':1,
        'isselect':cart.isselect,
    }
    return JsonResponse(responseData)


def changecartselect(request):
    isall = request.GET.get('isall')
    if isall=='true':
        isall = True
    else:
        isall = False

    token = request.session.get('token')
    user = User.objects.get(userToken = token)

    responseData = {
        'status':1,
        'msg':'全选/全部取消成功'
    }


    return JsonResponse(responseData)


def generateorder(request):
    token = request.session.get('token')
    if token:
        user = User.objects.get(userToken = token)
        # 生成订单
        order = Order()
        order.user = user
        order.number = uuid.uuid5(uuid.uuid4(),'order')
        order.save()

        carts = Cart.objects.filter(user = user).filter(isselect=True)

        for cart in carts:
            # 订单商品
            orderGoods = OrderGoods()
            orderGoods.order = order
            orderGoods.goods = cart.goods
            orderGoods.number = cart.number
            orderGoods.save()

            # 移除购物处
            cart.delete()

            # 商品 销量和库存处理


            responseData = {
                'status':'1',
                'msg':'订单生成成功（为付款）',
                'orderid':order.id,
            }

            return JsonResponse(responseData)


    else:
        return JsonResponse({'msg':'登陆后操作'})


def orderinfo(request):
    orderid = request.GET.get('orderid')
    order = Order.objects.get(pk=orderid)

    data = {
        'title':'订单详情',
        'order':order,
    }

    return render(request,'orderinfo/orderinfo.html',context=data)


def changeorderstatus(request):
    orderid = request.GET.get('orderid')
    status = request.GET.get('status')

    order = Oreder.objects.get(pk=orderid)
    order.status = 2
    order.save()

    data = {
        'msg':'付款成功',
        'status':1
    }

    return JsonResponse(data)