# coding=utf-8
import  sys
import  base64
import  re
import  requests
import  urllib3
import  urllib
import  json
import  time
import codecs
#import  api.aff
urllib3.disable_warnings()
def Retry_request(url): #远程下载
    i = 0
    for i in range(2):
        try:
            res = requests.get(url) # verify =false 防止请求时因为代理导致证书不安全
            return res.text
        except Exception as e:
            i = i+1
            print('重新下载：'+url)

def writeini(name,custom,method,ini):             # 自定义规则
    
    try:
        if ini == '' or ini == None:
            if custom == '' or custom == None:   #不分组的情况
                with open("./config/prefserver.ini", "r",encoding = 'utf-8') as f:
                    rule = f.read() 
                with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
                    f.writelines(rule)            
            else:
                with open("./config/prefserver.ini", "r",encoding = 'utf-8') as f:
                    rule = f.read()

                names = str(name).split('@')                
                groups = str(custom).split('@')
                methods = str(method).split('@')

                if len(groups) == len(names):  #分组填写正常的的情况
                        inicustom = str(rule).split(';NicoNewBeee')
                        inigroup = ''
                        groupname = '`'
                        for i in range(1,len(groups)):
                            if methods[i] == 'sl':
                                inigroup += 'custom_proxy_group='+str(names[i])+'手动选择`select`('+str(groups[i])+')\n'
                                groupname += '[]'+str(names[i])+'手动选择`'
                            if methods[i] == 'ut':
                                inigroup += 'custom_proxy_group='+str(names[i])+'延迟最低`url-test`('+str(groups[i])+')`http://www.gstatic.com/generate_204`500\n'
                                groupname += '[]'+str(names[i])+'延迟最低`'
                            if methods[i] == 'fb':
                                inigroup += 'custom_proxy_group='+str(names[i])+'故障切换`fallback`('+str(groups[i])+')`http://www.gstatic.com/generate_204`500\n'
                                groupname += '[]'+str(names[i])+'故障切换`'
                            if methods[i] == 'lb':
                                inigroup += 'custom_proxy_group='+str(names[i])+'负载均衡`load-balance`('+str(groups[i])+')`http://www.gstatic.com/generate_204`500\n'
                                groupname += '[]'+str(names[i])+'负载均衡`'

                        proxygroup =   'custom_proxy_group=🔰 节点选择`select'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=📲 电报吹水`select`[]🔰 节点选择`'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=📹 YouTube`select`[]🔰 节点选择`'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=🎥 NETFLIX`select`[]🔰 节点选择`'+groupname+'`(NF|解锁)`[]DIRECT\n\
                                        custom_proxy_group=📺 巴哈姆特`select`[]🔰 节点选择`'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=🌍 国外媒体`select`[]🔰 节点选择`'+groupname+'[]DIRECT\n\
                                        custom_proxy_group=🌏 国内媒体`select`[]DIRECT`[]🔰 节点选择\n\
                                        custom_proxy_group=🍎 苹果服务`select`[]DIRECT`[]🔰 节点选择`\n\
                                        custom_proxy_group=🛑 全球拦截`select`[]REJECT`[]DIRECT\n\
                                        custom_proxy_group=🐟 漏网之鱼`select`[]🔰 节点选择`[]DIRECT`'+groupname+'\n'

                        inicustom[1] = proxygroup+inigroup                
                        with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
                            f.writelines(str(inicustom[0])+str(inicustom[1])+str(inicustom[2])) 
                else:                           #分组填写不正常的的情况
                    with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
                        f.writelines(rule)  
        else:
            with open("./config/inibase.ini", "r",encoding = 'utf-8') as f:
                    rule = f.read()
            ini = Retry_request(ini)
            if '[common]' in ini or '[server]' in ini or '[advanced]' in ini or '[managed_config]' in ini:
                return 'ini'
            ini = ini.split(';NicoNewBeee')[1]
            rule =  rule + '\n;ini客制化\n'+ini
            with codecs.open("./config/pref.ini", "w",encoding = 'utf-8') as f:
                    f.writelines(rule)                             
    except Exception as e:
        print(e)

#print(Retry_request('http://127.0.0.1:10010/clash?url=https%3A//stc-dns.com/link/jSkLx7LgGRRfgSFw%3Fmu%3D2'))
#custom_proxy_group=UrlTest`url-test`.*`http://www.gstatic.com/generate_204`300
#custom_proxy_group=FallBack`fallback`.*`http://www.gstatic.com/generate_204`300
#custom_proxy_group=LoadBalance`load-balance`.*`http://www.gstatic.com/generate_204`300

