# 脚本功能
[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)
  - 项目基于Flask框架
  - 项目基于subconverter：https://github.com/tindy2013/subconverter
  - 配置文件版示例： https://github.com/lzdnico/subconverteriniexample
  - 项目示例站点： https://subweb.niconewbeee.tk
  - 更新频道：https://t.me/niconewbeeeapi
  - 打赏地址:https://t.me/niconewbeeeapi/134
  - 托管地址生成页面示意图
  ![image](https://github.com/lzdnico/subweb/blob/test/images/index.png) 
# 环境搭建及运行
  - 1.安装python3 依赖： 
  ```bash
  apt install -y python3-pip  git python3
  ```
  - 2.下载源码：
  ```bash
  cd 
  git clone https://github.com/lzdnico/subweb.git 
  ```
  - 3.安装库： 
  ```bash
  cd subweb
  pip3 install -I -r requirements.txt 
  ```
  - 4.开始运行：
  ```bash
  chmod 777 /root//subweb/subweb.sh
  cd /root/subweb 
  ./subweb.sh http:127.0.0.1:10086 http:127.0.0.1:10010
  ```
  ```bash
  http:127.0.0.1:10086 为web前端地址
  http:127.0.0.1:10010 为sub后端地址
  想要修改web端口，需修改api.py的main函数
  想要修改sub端口，需修改config/perf.ini中的配置
  ```
# Docker 运行 By NicoNewBeee 
- 1.拉取镜像： 
```bash
docker pull niconewbeee/subweb:latest
```
- 2.运行docker 
WEB_HOST、CORE_HOST：参数修改为服务器的ip以及端口号，或者是域名搭配反代
-p 参数：WEB_HOST的端口Web_Port映射到10086，CORE_HOST的端口Core_Port映射到10010
```bash
docker run -d --restart=always --name=subweb -e WEB_HOST=http://serverip:Web_Port -e CORE_HOST=http://serverip:Core_Port -p Web_Port:10086 -p Core_Port:10010 niconewbeee/subweb
```
- 3.查看日志 
```bash
docker logs -f -t --tail 10 subweb
```
- 4.停止 
```bash
docker stop subweb
```
- 5.重启 
```bash
docker restart subweb
```
- 6.删除 
```bash
docker rm -f subweb
```

# Docker 运行 By NicoNewBeee 自编译版
- 1.下载源码： 
```bash
git clone https://github.com/lzdnico/subweb.git 
cd subweb
```
- 2.客制化（可选）：
```bash
修改 config/pref.ini（可选，用于自定义默认规则）
修改 docker.sh (可选，启动后执行的命令，默认5分钟进行自检)
修改 templates(可选)下html网页显示内容
```
- 3.生成docker
```bash
docker build -t subweb .
```
- 4.运行docker
```bash
docker run -d --restart=always --name=subweb -e WEB_HOST=http://serverip:Web_Port -e CORE_HOST=http://serverip:Core_Port -p Web_Port:10086 -p Core_Port:10010 subweb
```
- 5.查看日志 
```bash
docker logs -f -t --tail 10 subweb
```
# Docker 运行 By du5
> https://docker.io/gtary/subweb build by [@du5](https://t.me/Gtary)
1. 拉取镜像
```bash
docker pull gtary/subweb
```
2. 运行 
```bash
docker run -d --restart=always --name=subweb -e WEB_HOST=http://127.0.0.1:Web_Port -e CORE_HOST=http://127.0.0.1:Core_Port -p Web_Port:10086 -p Core_Port:10010 gtary/subweb
```
3. 停止
```bash
docker stop subweb
```
4. 重启
```bash
docker restart subweb
```
4. 删除
```bash
docker rm -f subweb
```
5. 查看日志
```bash
docker exec subweb tail /var/log/core.log -f
docker exec subweb tail /var/log/web.log -f
```


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
