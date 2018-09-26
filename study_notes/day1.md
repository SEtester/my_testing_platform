#### django目录说明
- manage.py：一个命令行工具，可以使你用多种方式对Django项目进行交互
- 内层的目录：项目的真正的Python包
- _init _.py：一个空文件，它告诉Python这个目录应该被看做一个Python包
- settings.py：项目的配置
- urls.py：项目的URL声明
- wsgi.py：项目与WSGI兼容的Web服务器入口


#### 创建项目
- 命令 ： django-admin startproject 项目名
举例说明 ： 创建要给名为 testting_platform的项目
django-admin startproject testting_platform


#### 查看django支持的python版本
- 查看django包里的setup.py文件
```
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
```

#### 创建应用
- 命令 ： python manage.py startapp 应用名  
举例说明 ： 需求：开发一个登陆功能  
创建一个业务模块 python manage.py startapp login_action  
 


#### 目录介绍
- _init.py_是一个空文件，表示当前目录login_action可以当作一个python包使用。
- tests.py文件用于开发测试用例，在实际开发中会有专门的测试人员，这个事情不需要我们来做。
- models.py文件跟数据库操作相关。
- views.py文件跟接收浏览器请求，进行处理，返回页面相关。
- admin.py文件跟网站的后台管理相关。

#### 安装应用
应用创建成功后，需要安装才可以使用，也就是建立应用和项目之间的关联，
在learning/settings.py中INSTALLED_APPS下添加应用的名称就可以完成安装。

#### 开发服务器
在开发阶段，为了能够快速预览到开发的效果，  
django提供了一个纯python编写的轻量级web服务器，仅在开发阶段使用。  
- 运行服务器命令 python manage.py runserver ip:端口  
举例说明：python manage.py runserver  

#### 模型设计 ORM框架
O是object，也就类对象的意思，R是relation，翻译成中文是关系，
也就是关系数据库中数据表的意思，M是mapping，是映射的意思。在ORM框架中，
它帮我们把类和数据表进行了一个映射，可以让我们通过类和类对象就能操作它所对应的表格中的数据。
ORM框架还有一个功能，它可以根据我们设计的类自动帮我们生成数据库中的表格，省去了我们自己建表的过程。

django中内嵌了ORM框架，不需要直接面向数据库编程，而是定义模型类，通过模型类和对象完成数据表的增删改查操作。

使用django进行数据库开发的步骤如下：

1. 在models.py中定义模型类
2. 迁移
3. 通过类和对象完成数据增删改查操作