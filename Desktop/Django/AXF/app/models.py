from django.db import models

# Create your models here.

# 基础 类
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# 轮播图 模型类
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'



# 导航
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'

# 每日必抢
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'


# 商品
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'

# 主体内容
class Mainshow(models.Model):
    trackid = models.CharField(max_length=10) # 跳转页面id
    name = models.CharField(max_length=100)  # 商品分类名称
    img = models.CharField(max_length=255)  # 分类图片
    categoryid = models.CharField(max_length=10)  # 分类id
    brandname = models.CharField(max_length=50)  # 品牌名

    img1 = models.CharField(max_length=200)   # 商品图片
    childcid1 = models.CharField(max_length=10)  # 子类id
    productid1 = models.CharField(max_length=10)#  商品嗯id
    longname1 = models.CharField(max_length=200)  # 商品名名称
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=200)  # 商品图片
    childcid2 = models.CharField(max_length=10)  # 子类id
    productid2 = models.CharField(max_length=10)  # 商品嗯id
    longname2 = models.CharField(max_length=200)  # 商品名名称
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=200)  # 商品图片
    childcid3= models.CharField(max_length=10)  # 子类id
    productid3 = models.CharField(max_length=10)  # 商品嗯id
    longname3 = models.CharField(max_length=200)  # 商品名名称
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'

    def __str__(self):
        return self.name


# 闪购超市
class Foodtypes(models.Model):
    # 分类id
    typeid = models.CharField(max_length=10)
    # 分类名称
    typename = models.CharField(max_length=100)
    # 子类名称
    childtypenames = models.CharField(max_length=255)
    # 分类排序
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'

    def __str__(self):
        return self.typename


# 商品信息
# 商品列表数据
class Goods(models.Model):
    # 商品id
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=150)
    # 商品名称(不一定有)
    productname = models.CharField(max_length=50)
    # 商品长名称
    productlongname = models.CharField(max_length=100)
    # 是否精选
    isxf = models.NullBooleanField(default=False)
    # 是否买一赠一
    pmdesc = models.CharField(max_length=10)
    # 规格
    specifics = models.CharField(max_length=20)
    # 价格
    price = models.CharField(max_length=10)
    # 超市价格
    marketprice = models.CharField(max_length=10)
    # 组id
    categoryid = models.CharField(max_length=10)
    # 子类组id
    childcid = models.CharField(max_length=10)
    # 子类组名称
    childcidname = models.CharField(max_length=10)
    # 详情页id
    dealerid = models.CharField(max_length=10)
    # 库存
    storenums = models.IntegerField()
    # 销量
    productnum = models.IntegerField()
    # 是否删除
    # isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.pruductname

    class Meta:
        db_table = 'axf_goods'


class Chen(Base):
    class Meta:
        db_table = 'axf_chen'









# 用户模型类
class User(models.Model):
    # 用户账号，要唯一
    userAccount = models.CharField(max_length=20,unique=True)
    # 密码
    userPasswd  = models.CharField(max_length=255)
    # 昵称
    userName    =  models.CharField(max_length=20)
    # 手机号
    userPhone   = models.CharField(max_length=20)
    # 地址
    userAdderss = models.CharField(max_length=100)
    # 头像路径
    userImg     = models.CharField(max_length=150)
    # 等级
    userRank    = models.IntegerField()
    # touken验证值，每次登陆之后都会更新
    userToken   = models.CharField(max_length=50)
    # 是否删除
    isDelete = models.BooleanField(default=False)
    @classmethod  # 定义一个类方法创建对象
    def createuser(cls,account,passwd,name,phone,address,img,rank,token):
        u = cls(userAccount = account,userPasswd = passwd,userName=name,userPhone=phone,userAdderss=address,userImg=img,userRank=rank,userToken=token)
        return u


# 购物车
class Cart(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 商品
    goods = models.ForeignKey(Goods)
    # 选择数量
    number = models.IntegerField()
    # 是否选中
    isselect = models.BooleanField(default=True)


# 订单模型类
class Order(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 订单号
    number = models.CharField(max_length=255)
    # 状态
    # 1 未付款
    # 2 已付款，未发货
    # 3 已发货，未收获
    # 4 已收获，未评价
    # 5 已评价
    # 6 退款...
    status = models.IntegerField(default=1)
    # 创建时间
    createtime = models.DateTimeField(auto_now=True)



# 订单 商品
# 一个 订单，对应 多个商品
# 主 订单
# 从 订单商品[声明关系]
class OrderGoods(models.Model):
    # 订单
    order = models.ForeignKey(Order)
    # 商品
    goods = models.ForeignKey(Goods)
    # 数量
    number = models.IntegerField(default=1)



