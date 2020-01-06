#! /bin/sh 
function start()
{
echo "-----------------------------------Start-------------------------------------"
python3 /subweb/api/tg.py API测试版开始启动
}

function client()
{  
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
        python3 /subweb/api/tg.py API测试版后端掉线了，又自动重启了
    fi
    
    proc_name="python3"        #进程名
    proc_num()                      #查询进程数量
    {
        num=`ps -ef | grep $proc_name | grep -v grep | wc -l`
        return $num
    }
    proc_num  
    number=$?                       #获取进程数量
    if [ $number -eq 0 ]            #如果进程数量为0
    then                            #重新启动服务器，或者扩展其它内容。
        python3 /subweb/api/tg.py API测试版前端掉线了，又自动重启了
        python3 /subweb/api.py &   #运行web服务
    fi
}


function main()
{
    start
    while true
    do   
    client    
    sleep 60s
    done
}

main

