#! /bin/sh 
echo "-----------------------------------Start-------------------------------------"
echo "-----------------------------------$WEB_HOST,$CORE_HOST------------------------"
filename="/subweb/api/aff.py"
cat>"${filename}"<<EOF
aff = '不限制机场，规则生成失败，请检测调用格式。STC测试可用，注册地址：bilibili.stchk.cloud/auth/register?code=gzI5'   
subip = '$CORE_HOST'     
apiip = '$WEB_HOST'          
EOF
cat /subweb/api/aff.py
echo "-----------------------------------写文件完成----------------------------------------"
echo "------------------------------------While循环----------------------------------------"
while true
do
    proc_name="subconverter"        #进程名
    proc_num()                      #查询进程数量
    {
        num=`ps -ef | grep $proc_name | grep -v grep | wc -l`
        return $num
    }
    proc_num  
    number=$?                       #获取进程数量
    if [ $number -eq 0 ]            #如果进程数量为0
    then                            #重新启动服务器，或者扩展其它内容。
        cd /subweb/config
        ./subconverter &
        pkill python3
        python3 /subweb/api.py &   #运行web服务
echo "------------------------------------Restart----------------------------------------"
    fi
    sleep 300s
echo "------------------------------------Sucess----------------------------------------"
done
echo "------------------------------------WEB----------------------------------------"
tail -f /dev/null