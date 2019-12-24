#! /bin/sh 
echo "-----------------------------------Start-------------------------------------"
cd /root/subweb
git reset --hard HEAD
sleep 1s
git pull
echo "----------------------------------Update-------------------------------------"
sleep 1s
\cp /root/nico/aff.py /root/subweb/api/aff.py                    #前端后端地址定义
\cp /root/nico/pref.ini /root/subweb/config/pref.ini             #后端基础配置定义
\cp /root/nico/docker.sh /root/subweb/docker.sh                  #docker运行脚本
\cp /root/nico/tg.py /root/subweb/api/tg.py                      #进程报警脚本
chmod 777 /root/subweb/config/subconverter
chmod 777 /root/subweb/docker.sh
echo "------------------------------------DONE---------------------------------------"