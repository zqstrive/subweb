#全局变量定义
aff = '不限制机场，规则生成失败，请检测调用格式。STC测试可用，注册地址：bilibili.stchk.cloud/auth/register?code=gzI5'

#subip = 'https://stcapi.stcnat.com' 
#apiip = 'http://stcapi.stcnat.com:10086'       

#subip = 'https://api.niconewbeee.tk'    
#apiip = 'http://185.238.248.145:10086'    

subip = 'http://127.0.0.1:10010'      #默认apiip 是web的端口，在api.py的main函数指定。  默认subip是 subconverter 的端口，在config/perf.ini 中指定
apiip = 'http://127.0.0.1:10086'          #套CDN后，可以在服务器上整反代，将域名反代到本地运行的端口：http://127.0.0.1:10010 