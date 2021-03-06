#  第２章　django网站快速入门


#  ２．１　　个人博客网站规划

#  ２．１．１　　博客网站的需求与规划


#  项目名称mblog
#  通过admin管理界面张贴(发帖)，编辑以及删除帖文，且此界面支持Markdown语句
#  使用Bootstrap网页框架
#  在主页中显示每篇文章的标题，简短摘要以及发帖日期
#  在主页中加入侧边栏，可以加入自定义的HTML,Javascript网页代码
#  在输出文章时，可以解析Markdown语句并正确显示排版后的样子


#  由于是简单的入门示例网站，因此在设置上只有管理员一人可以张贴以及管理文章，不需要有用户的注册，登录等权限管理．此外，在数据库中仅存储文章的
#  原始数据，但此数据支持Markdown语句，可以在文章显示时作为排版的依据，不提供所见即所得的文章编辑界面．另外，所有图像文件采用第三方网站存储的方式
#  ．本博客要显示的图像需要以外部的链接的方式通过Markdown语句设置在文章中，并在显示该篇文章时显示在指定的位置

#  ２．１．２　产生第一个网站框架

#2.1.3  django文件夹与文件解析

# 配置文件中,包括settigns.py,urls.py以及wsgi.py,其中   wsgi.py是和虚拟主机中的网页服务器(如apahce)沟通的接口,中间的设置要等到网站上线才会用到


# urls.py 用来设置每一个url的网址要对应的函数以及对应的方式,通常是创建新的网页时要先编辑的文件.
#　settings.py是此网站的系统设计所在的位置，新创建的网站都要先打开这个文件，进行编辑设置的操作．真正网站所有运行的逻辑都在使用startapp mainsite
#　　创建出来的APP文件夹中．使用这样的方式是让网站的每一个主要功能都成为一个单独的模块，方便网站的开发者在不同的网站中重复使用，这也是python
#　程序设计应用中reuse(复用)概念的应用
#　

#　先要在编辑settngs.py的两个地方．首先，把我们创建的APP模块mainsite加进去(在settings.py的INSTALL_APPS列表中)
