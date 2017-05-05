## 安装步骤
* git clone git@github.com:ShawnLeee/awesome_proj.git
* cd awesome_proj
* virtualenv -p /usr/bin/python2.7 venv
* source venv/bin/activate
* python fake_qiubai/manage.py runserver
* cd qiubai_front
* npm install
* npm run dev    
前端页面暂时只适配了移动端，pc端页面在django static中    
项目中的数据是从糗事百科网站爬取下来存储在本地mysql数据库中，对一些数据采用redis进行了缓存 
 
![效果展示](http://ww1.sinaimg.cn/large/6c3951c4ly1ffab6jbrwyg20d90jihdt.gif)    
pc页面展示图
[Tap Me](http://ww1.sinaimg.cn/large/6c3951c4ly1ffac3hskppg20u60lc7wr.gif).