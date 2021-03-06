#　第６章　Template深入探讨

#　制作网站时千万别把网站的HTML/CSS/JavaScript排版以及一些高级的视觉功能和网站的程序逻辑一起设计．这样会很难维护．专业的网站一定是把视图和过程控制逻辑分开
#　之前介绍的views.py以及urls.py可以算是程序的控制逻辑，而本章主要介绍Template属于视图逻辑．


#　６．１　　Template的设置与运行
#　在使用Template之前，首先要到settings.py中做好文件夹的设置工作，安排所有.html在同一文件夹中，并把DIR指到这个文件夹．另外，如果不想使用默认的模板引擎
#　也可以自行更换

#　６．１．１　　settings.py设置


#　settings.py中与Template有关的设置如下

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 其中，在BACKEND处可以指定要使用的模板引擎，在网页模板中常用的Jinja2可以直接换成django.template.backends.jinja2.Jinja2

# 第二个设置DIR很重要,用来指定templates网页文件要存放在哪里,一般我们都会将其与主网站放在一起,所以都是使用os.path.join把templates
# 附加到BASE_DIR（主网站的目录位置），直接把templates文件夹创建在主网站的同一个文件夹下就可以了．创建完成的文件夹结构如下

#  在例子中,网站的首页如果使用了, 在views.py中编写一个index函数,语句如下

#  实际上模板引擎的输入有两个主要的部分:第一部分当然是模板文件,也就是.html的文件;第二部分是要用来显示的数据内容,这些我们会放在变量里面,
#  然而使用字典的格式把数据传送到模板引擎中.传送进去的变量可以是单纯的单一变量,也可以是复杂的列表数据,这些数据都可以在模板中通过指令
#  来设置输出的方式

#    变量views.py  +   网页模板 index.html  =======>> Template Engine  ========>   实际网页html

#  在用来当做模板的.html文件中,除了编写HTML标记内容外,也可以使用将要介绍的模板语句来编写显示数据的方法.另外,还可以进一步使用模板继承或导入的方式
#  在模板中使用别的模板,兼容便利性和弹性.通过模板引擎渲染出来的结果就是一个包含HTML标记的字符串,最后只要把这个字符串使用HttpResponse传送到
#  网页服务器即可
#  6.1.2  创建templates文件

#   设置固定的文件夹后,把所有.html文件都放在这个文件夹中就可以了.一个页面可以对应一个模板文件,但是其实哪个模板文件要由哪个函数来处理其实并没有特别的
#  规定.因此,一个个的模板文件(*.html)可以看成一个个可以使用的素材,用来显示特定排版样式的网页,需要的时候随时可以拿来使用.下面介绍模板的标准步骤
#  步骤1: 找到适用的模板,如果没有,就建立一个,存放在templates文件夹下
#  步骤2: 在views.py的处理函数中查询,计算并准备数据,把要显示在网页上的数据使用字典格式编排好
#  步骤3: 使用get_template函数取得要使用模板的执行实例instance,一般会直接命名为template
#  步骤4: 通过template把变量以字典类型的形式传入,渲染成为一个字符串html
#  步骤5: 把html通过HttpResponse传送给网页服务器

# 如果要传送的变量比较多,要编写很长的字典.有一个方法,就是使用python的locals()函数.这是一个内建的函数,功能是把当前所有的局部变量编成字典格式返回
#  有了这个数据,直接把它提供给render渲染即可

#  在template文件中,渲染器主要以2个符号来识别,分别是"{{id}}" 和 "{% cmd %}".其中两对大括号中间放置要显示的变量,看到这样的符号,渲染器就会
#  直接把变量id的内容显示出来.大括号加上百分比好代表中间是模板的控制命令,它会根据控制命令的用途执行指令(例如决策,循环)或执行模板的继承与管理等相关指令
#   以让网页首页显示系统当前时间为例,假设我们把当前的服务器系统时间放在now变量中,然后在index.html中的特定位置显示出来,那么在views.py中的index
# 处理函数应该改写如下

#　6.1.3  在templates文件中使用现有的网页框架
#　由于模板引擎只针对{{}} 和　{% %} 中的内容进行处理，原本放在.html文件中的javascript以及css程序代码并不会被改动，因此在网页排版中经常会使用到
#　的jQuery，Ajax以及Bootstrap等都可以用在模板文件中，使用这些框架需要导入一些外部的.js和.css文件，如果这些文件要放在网站的文件夹中，就会被视为静态文件
#　需要进行一些额外的处理，因此，除非有特殊的考虑，笔者建议直接使用CDN链接的方式，一些自定义的CSS和JS文件可以使用静态文件处理，以Bootstrap为例

#　可以直接把上面的这一段代码放在index.html的<head></head>之间即可，一般是放在</head>这一行的前面．而jQuery的代码
#　这一段代码放在</body>之前即可．使用Bootstrap以及jQuery就可以使用极其精简的程序代码编写写出具有充分前端互动能力的网页．当然，网页设计人员习惯使用的工具
#　也都没有问题，只要注意网页中的静态文件处理方式以及预留要显示变量的地方即可
#　６．１．４　　直播电视网站应用范例

# 也就是使用datetime模块中的now()函数取得目前的系统时间,放在now变量中,然后通过locals()内建函数把所有局部变量打包传给render.在index.html中

#　要指定显示的格式以及位置，把HTML的格式设置好之后，使用{{ now }}就可以把目前系统日期时间显示出来



#　本小节以一个直播电视网站来做综合应用的范例．现在有许多电视都提供YouTube上的24小时直播服务，本小节的目的是制作一个网站，把这些直播电视新闻集中
#　在我们的网站中，并以链接或按钮的方式来提供选台的服务
#　要把YouTube某一个视频链接到自己的网站中，需要先取得该网站的嵌入码，嵌入码的位置如下

# 比如换成 梨视频的链接

#　基本上每一个视频的嵌入码都是一样的，只有一个地方不同，就是每一个视频特有的ID,位于＂embed/＂之后，＂"＂之前的地方．因此，嵌入码在网页中只要使用一次，
#　然后填入不同的ID就会出现不同的视频．运用这个原理，我们超出任意４个直播新闻网站的ID以及对应的名称并将存储在列表中，当使用在本网站网址后面指定的
#　数字后，就按照该数字选用对应的新闻新闻网站的名称以及ID传送到index.html中进行网页显示，完成我们的程序

#　为了让网址可以接受数字,urls.py的内容编写如下
#　urlpatterns的第1行是原来首页使用的设置,第2行是增加让网址可以识别出1个数字'\d{1}'的设置,因为我们在index.html使用这行设置来对网址进行编码,所以也把
#　这个设置叫做"tv-url"

#　在views.py中的index函数程序如下

# locals()函数会以字典类型返回当前位置的全部局部变量,对于函数,方法,lambda函数式,以及实现了__call__方法的实例都换费此
#　在这个函数中，先把搜集到的２个直播视频ID放在tv_list列表中．它们的索引值分别是0和１,在这个例子中，我们只打算把要放的视频数据传送过去，因此先取得tvno,
# 也就是用户选用的频道(从网址栏中选取,例如localhost:8000/0会选用0,而localhost:8000/1会选用1),并从tv_list列表中取出选到的频道信息放在tv变量中.
#  由于tv变量是一个典型类型的变量,因此可以使用tv.name取出频道的名称,tv.tvcode取出视频的ID.在进入render之前,使用locals()内建函数加载所有
#  局部变量,传送到index.html进行网页显示
#  在<head></head>之间放的是Bootstrap的CDN链接以及网站的一般信息,在</body>之前的则是jQuery的CDN链接,这些内容可以在相关的官网上找到并复制.
#  如我们之前的叙述使用{{tv.name}}取出直播视频的名称

#  下面这段程序代码用来执行视频嵌入网站的工作:
#  注意/embed/字符串后面{{tv.tvode}},就是通过Template在从views.py传送过来的变量中取出其视频ID的部分,然后串接在嵌入码的地方,在此ID后面加上"?autoplay=1",
#  让此视频可以在选取之后立即自动播放,这样操作起来比较像电视机的选台功能
#  至于菜单的部分,在此使用了Bootstrap的功能制作菜单,编码吗如下

#  本小节使用的是固定菜单的做法,等到学习Template的循环指令后,就可以创建更有弹性的节目菜单了,在网址栏链接的部分,我们使用了{% url 'tv-url' 0 %}
#  可以在urls.py中的设置样式,给定参数(在这里是0~1)会编出符合该格式的网址蓝,非常方便

#  6.1.5   在template中使用static文件
#  基于性能的考虑,Django对于静态文件有不同的处理方式,这些我们在前面的章节也提过,在此复习一下,开发模式中间的问题比较简单,注意以下几点:
#  1. 在settings.py中,设置STATIC_URL使用的网站,例如STATIC_URL='/static/',也就是在指定在网址中以/static/开头的网址就视为要对静态文件进行读取
#  2. 在settings.py中,设置STATICFILES_DIRS,这是设置静态文件真正要存放的文件位置,一般而言都会放在网站目录下的static文件夹中,所以都会以os.path.join(BASE_DIR,'static')进行设置
#  3. 在template文件中使用静态文件的专用加载方式

#  其中第2点非常重要,也就是在传统的PHP网站中,如果要使用图片文件,只要把该文件放在任意目录中,然后使用路径作为链接即可.
#　例如，放在/images文件夹下的logo.jpg中，在链接时只要写成<img src='/images.logo.jpg'>就可以了，但是这种方法在Django中是行不通的
#　在Django中要使用如下方式：

#　　　｛％　load staticfiles　％｝
#   <img src="{% static " images/logo.png" % }" width =60>

# 其中，{% load staticfiles %}在整个文件中只要使用过一次即可．到目前为止，

# 我们把logo.png放在static/images文件夹内，接着在index.html把logo.png加入Bootstrap菜单栏的navbar-brand中，语句如下

#  在网站的左上角就可以看到此网站的图形logo了．