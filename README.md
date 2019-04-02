# weibo_reboot

发一条微博，内容为windows关机命令，如shutdown -s -t 60，即可远程关闭计算机，同时添加一条评论“正在关机......”

sinaweibopy3适用于python3。

weibo_reboot1.py登录验证微博账号、密码，在授权页面跳转后的页面的地址栏获取code，输入到控制台，获取用户access_token，即可访问新浪微博API。
通过获取微博内容，从第一条微博内容中提取出text，即关机命令，subprocess模块创建子进程执行关机。

weibo_reboot2.py将weibo_reboot1.py中的access_token保存下来，直接使用，不必每次再打开浏览器授权。
