# 功能简介

这是一个四川大学图书馆自动预约的软件，并采用pywebio部署到网页端

# 使用说明

* 安装必要的包
```bash
conda install lxml requests pandas
pip3 install pywebio
```
* 运行web_init.py即可搭建一个四川大学图书馆自动预约的网站(默认端口是5001)
* 运行autoReserve.py即可自动为csv文件里面的用户进行预约
* 然后将autoReserve.py放在crontab里，将info.csv文件的路径改成绝对路径即可自动预约，我部署的服务器是每小时的第15分钟自动预约

# 现成网站

我已经搭建了一个网站，但是不会时时刻刻开放，如果您感兴趣可以自己搭建

http://119.3.162.117:5001/

# 存在问题

* 密码是明文存储的，因为只开发了一天，如果不想存储在我的服务器上，请您自行搭建环境
* 还有许多功能没有添加
  * 修改密码
  * 添加查重
  * 修改预定的图书馆
* 如果您有兴趣欢迎进行pull request或者在issue区讨论，我会及时浏览
# 特别鸣谢
https://www.bilibili.com/video/BV1vZ4y1X7j5
我是从这个B站视频看见的，然后自己扩充了一下，感谢学长

