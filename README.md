# seiya

# step1:
set mysql/my.cnf:
[client]
default-character-set = utf8
[mysqld]
character-set-server = utf8
[mysql]
default-character-set = utf8
# 设置完成后启动mysql并创建名为“seiya”的database

# step2:
# 进入项目根目录seiya
linux: export FLASK_APP=seiya/web/app.py
win: set FLASK_APP=seiya\web\app.py

# step3:
# 在项目根目录下用migrate初始化数据库
flask db init
flask db migrate
flask db upgrade

# step4:
# 往数据库中写入必要数据
# 项目根目录下flask shell
from seiya.db.base import create_data
create_data()

# step5:
# 项目根目录下运行爬虫，三个爬虫所爬的网站的反爬都比较严格，默认爬虫delay为30，可自行在settings.py文件中修改
# 点评网的css字典映射已自动解读，解读文件为woffdict.py
# woffdict.py需要在实例化时接收字典映射css的url，调用实例化方法decrypt时需要接收未解读的网页源代码，运行后返回解读后的网页源代码
# 爬点评网时最好先手动浏览并验证成功一次后再爬会比较顺利
# 由于网站改动频繁，爬虫有时效性
scrapy crawl jobs
scrapy crawl houses
scrapy crawl restaurant
# 运行web
flask run
