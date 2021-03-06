#  第8章  网站窗体的应用

# 网页程序不同于一般程序可以在程序中使用input来取得用户的输入数据,而是通过窗体form的形式,先呈现在客户端的网页中,等用户填入数据并点击提交(submit)
# 按钮后,经由网页服务器从request把用户填写的内容传送到处理的函数,让网站开发人员可以解析数据的数据做出回应

#  在前面已经熟悉了如何把数据存放在数据库中,也可以轻松地把数据通过我们想要的方式取出以及呈现在网页上,本章将进一步使用窗体的功能提供网站
# 和浏览者之间的互动,让网站的功能更加完整

# 8.1  网站与窗体

# 设计一个高互动性的网站,窗体绝对是不可或缺的功能,因为它是取得用户输入最直接也最传统的渠道.本节说明HTML语句中form窗体写法,可以使用的元素和属性
# 以及如何在django程序中取得窗体的数据

# 8.1.1  HTML<form>的窗体简介


#　在django的网站中放在template文件中就可以了．那如何接收输入的值呢？前面提到过通过request对象．在处理的views.index函数中会接收一个request对象
#  而使用GET方法送进来的内容，只要使用request.GET['input_name']就可以取得了，因此
#  由于窗体的内容有可能会是空值(None),因此在输入的时候一定要使用try/except例外处理机制才不会造成网站程序异常异常中断执行．那么，如果要做密码判断呢？
#  接下来只要在index.html中取出verified变量来检查，根据它的内容是True还是False来显示相对应的字符串即可，修改index.html＃

# 这里只有在输入账号和密码的时候才会显示结果,此时网站的程序并不会记住用户的相关信息,要通过后面的Session功能来实现真正的用户权限管理功能或
#　输入一次密码后可以把用户这次活动过程中的信息记录下来

#　８．１．２　　活用窗体的标签

#　窗体除了可以输入文字和密码的text和password外，其他常用组件如下

#　<select>  下拉式菜单
#　<input type='ratio'＞　　单选按钮(单选)
#　<input type='checkbox'>  复选框(多选)
#　<input type='hidden'>  隐藏字段
#　　<input type='button'>  自定义按钮
#　<textarea>   多列文字内容

#　在使用这些标签的过程中，也可以充分使用程序的循环功能，不用把选项固定写死在程序代码中


#　８．１．３　　建立本章可范例汪涵的数据模型

#　可以开始设计一个让用户以窗体和网站互动的使用网站．延续前面的Template基础，需要一个Model，另外，张贴的信息要有一个Model来存储，

# 上午Model经由makemigrations和migrate同步到数据库后,可以到admin.py中再加入入戏爱吃呢个徐,

#  数据建立完毕后,可以在views.index处理函数中把这些数据先读取出来,放在各个变量中备用

#　８．１．４　网站窗体的建立与数据显示

# 8.1.5  接收窗体数据存储在数据库中

#  8.1.6  加上栓出贴文的功能