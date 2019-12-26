# Docker运行
  - 1.安装python3 依赖： 
  ```bash
  docker pull niconewbeee/subweb:basic
  ```
  - 2.下载源码：
  ```bash
  cd 
  git clone https://github.com/lzdnico/subweb.git 
  ```
  - 3.客制化：
  ```bash 
  修改api/aff.py  中的subip 和 apiip 分别为前端和后端地址   端口号为docker -p参数的宿主机端口
  修改config/perf.ini 中的默认配置                         端口10010不用修改，可以通过docker映射自定义访问端口
  修改templates 文件下的网页显示
  \cp /root/subweb/docker/mydocker.sh /root/subweb/docker.sh  修改启动脚本
  chmod 777 /root/subweb/docker.sh                          修改启动脚本权限

  ```
  - 4.开始运行：
  -p 前端端口号：10086 -p 后端端口号：10010                 这个前/后端端口需要与api/aff.py中的一致
  ```bash 
  docker run  -d --restart=always -v /root/subweb:/subweb -p 10086:10086 -p 10010:10010  niconewbeee/subweb:basic
  ```