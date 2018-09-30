#### 数据库配置
- 在settings.py文件中，通过DATABASES项进行数据库设置
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
- django支持的数据库包括：sqlite、mysql等主流数据库
- Django默认使用SQLite数据库

#### 使用django进行数据库开发的步骤如下：
1. 在models.py中定义模型类
2. 迁移   
- 生成迁移文件：根据模型类生成sql语句
```
python manage.py makemigrations
```
- 迁移文件被生成到应用的migrations目录
```
迁移文件被生成到应用的migrations目录
```
- 执行迁移：执行sql语句生成数据表
````
python manage.py migrate
````
3. 通过类和对象完成数据增删改查操作


#### Django管理操作 (管理数据表数据)
- 创建一个管理员用户
```
python manage.py createsuperuser,按提示输入用户名、邮箱、密码
```
- 启动服务器，通过“127.0.0.1:8000/admin”访问，输入上面创建的用户名、密码完成登录
- 进入管理站点，默认可以对groups、users进行管理

#### 管理界面本地化
- 编辑settings.py文件，设置编码、时区
```
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
```