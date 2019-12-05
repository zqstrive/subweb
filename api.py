# coding=utf-8
import sys
import flask_restful
from flask import redirect, url_for
import  base64
import  re
import  requests
import urllib3
import urllib
import urllib.parse
import json
import time
import codecs
import api.subconverter
import api.aff
import api.getini

from flask import Flask,render_template,request
urllib3.disable_warnings()


def safe_base64_decode(s): # 解码
    try:
        if len(s) % 4 != 0:
            s = s + '=' * (4 - len(s) % 4)
        base64_str = base64.urlsafe_b64decode(s)
        return bytes.decode(base64_str)
    except Exception as e:
        print('解码错误')   

def safe_base64_encode(s): # 加密
    try:
        return base64.urlsafe_b64encode(bytes(s, encoding='utf8'))
    except Exception as e:
        print('解码错误',e)

app = Flask(__name__)

ip = 'http://'+api.aff.apiip+'/'
@app.route('/',methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if request.form['submit'] == '基础使用版':
            return redirect(ip+'basic')
        if request.form['submit'] == '节点分组版':
            return redirect(ip+'customgroup')
        if request.form['submit'] == '配置文件版':
            return redirect(ip+'ini')
    return render_template('login.html')

@app.route('/basic', methods=['GET', 'POST'])
def basic():
    try:
        if request.method == "POST":
            s = request.form['left']
            s = s.replace('\n','|').replace('\r','')
            if s.split('|')[-1]== '':
                s = s[:-1]        
            if '://' in s:
                sub = urllib.parse.quote(s)
                try:
                    tool=str(request.values.get('tool'))
                except :
                    pass
                if tool == 'clash':
                        CustomGroupvmess = 'http://{ip}/sub?target=clash&url={sub}'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=clash&url={sub}'.format(sub=str(sub)) 
                        return render_template('clash.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)
                if tool == 'clashr':
                        CustomGroupvmess = 'http://{ip}/sub?target=clashr&url={sub}'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=clashr&url={sub}'.format(sub=str(sub)) 
                        return render_template('clashr.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)                       
                if tool == 'surge':
                        CustomGroupvmess = 'http://{ip}/sub?target=surge&url={sub}'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}'.format(sub=str(sub)) 
                        return render_template('surge.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)
                if tool == 'mellow':
                        CustomGroupvmess = 'http://{ip}/sub?target=mellow&url={sub}'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=mellow&url={sub}'.format(sub=str(sub)) 
                        return render_template('mellow.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)
                if tool == 'surfboard':
                        CustomGroupvmess = 'http://{ip}/sub?target=surfboard&url={sub}'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=surfboard&url={sub}'.format(sub=str(sub)) 
                        return render_template('surfboard.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)
                if tool == 'qxnode':
                        CustomGroupvmess = 'http://{ip}/sub?target=quanx&url={sub}'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=quanx&url={sub}'.format(sub=str(sub))
                        return render_template('qxnode.html',sub = s,custom="未填写",api=CustomGroupvmess,api2=api2)            
                if tool == 'surnode':
                        CustomGroupvmess = 'http://{ip}/sub?target=surge&url={sub}&ver=4&udp=true&tfo=true'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}&ver=4&list=true&udp=true&tfo=true'.format(sub=str(sub))
                        return render_template('surgenode.html',sub = s,custom="默认为surge4，参数为为ver=4。默认udp=true,tfo=true",api=CustomGroupvmess,api2=api2)                                 
                else:
                    return render_template('basic.html')    
            else:
                return '订阅不规范'
        return render_template('basic.html')
    except Exception as e:
        return e

@app.route('/customgroup', methods=['GET', 'POST'])
def customgroup():
    try:
        if request.method == "POST":
            if request.form['submit'] == '点击添加节点分组':            
                ori1 = request.form['custom1']
                ori2 = request.form['custom2']
                ori3 = request.form['custom3']
                add1 = '@'+ request.form['firstname'].replace('@','')
                add2 = '@'+request.form['lastname'].replace('@','')
                add3='@'+  request.values.get('method').replace('@','')
                if add1 == '@':
                    return '未填写名称'                
                if add2 == '@':
                    return '未填写节点'
                return render_template('index.html',custom1=ori1+add1,custom2=ori2+add2,custom3=ori3+add3)    
            s = request.form['left']
            s = s.replace('\n','|').replace('\r','')
            if s.split('|')[-1]== '':
                s = s[:-1]        
            if '://' in s:
                n=request.form['custom1']           
                c=request.form['custom2']
                method = request.form['custom3']
                len1 = len(str(n).split('@'))
                len2 = len(str(c).split('@'))
                len3 = len(str(method).split('@'))
                if len1 != len2 or len1 != len3 or len2 != len3:
                    return('检查分组是否一一对应')
                groups = str(safe_base64_encode(api.subconverter.getgroups(n,c,method))).split('\'')[1]
                sub = urllib.parse.quote(s)
                try:
                    tool=str(request.values.get('tool'))
                except :
                    pass
               
                if tool == 'clash':
                        CustomGroupvmess = 'http://{ip}/sub?target=clash&url={sub}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups)
                        api2 = 'https://gfwsb.114514.best/sub?target=clash&url={sub}'.format(sub=str(sub)) 
                        return render_template('clash.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)
                if tool == 'clashr':
                        CustomGroupvmess = 'http://{ip}/sub?target=clashr&url={sub}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups)
                        api2 = 'https://gfwsb.114514.best/sub?target=clashr&url={sub}'.format(sub=str(sub)) 
                        return render_template('clashr.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)                       
                if tool == 'surge':
                        CustomGroupvmess = 'http://{ip}/sub?target=surge&url={sub}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups)
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}'.format(sub=str(sub)) 
                        return render_template('surge.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)
                if tool == 'mellow':
                        CustomGroupvmess = 'http://{ip}/sub?target=mellow&url={sub}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups)
                        api2 = 'https://gfwsb.114514.best/sub?target=mellow&url={sub}'.format(sub=str(sub)) 
                        return render_template('mellow.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)
                if tool == 'surfboard':
                        CustomGroupvmess = 'http://{ip}/sub?target=surfboard&url={sub}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups)
                        api2 = 'https://gfwsb.114514.best/sub?target=surfboard&url={sub}'.format(sub=str(sub)) 
                        return render_template('surfboard.html',sub = s,custom=n+c+method+'  备用暂时不支持',api=CustomGroupvmess,api2=api2)
                if tool == 'qxnode':
                        CustomGroupvmess = 'http://{ip}/sub?target=quanx&url={sub}'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=quanx&url={sub}'.format(sub=str(sub))
                        return render_template('qxnode.html',sub = s,custom="qx-node 暂不支持客制化",api=CustomGroupvmess,api2=api2)            
                if tool == 'surnode':
                        CustomGroupvmess = 'http://{ip}/sub?target=surge&url={sub}&ver=4&udp=true&tfo=true'.format(ip=api.aff.subip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}&ver=4&list=true&udp=true&tfo=true'.format(sub=str(sub))
                        return render_template('surgenode.html',sub = s,custom="默认为surge4，参数为为ver=4。默认udp=true,tfo=true",api=CustomGroupvmess,api2=api2)                                  
                else:
                    return render_template('index.html')    
            else:
                return '订阅不规范'
        return render_template('index.html')
    except Exception as e:
        return e

@app.route('/ini', methods=['GET', 'POST'])
def inigroup():
    try:
        if request.method == "POST":
            s = request.form['left']
            s = s.replace('\n','|').replace('\r','')
            if s.split('|')[-1]== '':
                s = s[:-1]        
            if '://' in s:
                ini=request.form['ini']                            
                sub = urllib.parse.quote(s)
                try:
                    tool=str(request.values.get('tool'))
                except :
                    pass
                ini1 = api.subconverter.getini(ini).split('&')
                rulesets = str(safe_base64_encode(ini1[0])).split('\'')[1]
                groups = str(safe_base64_encode(ini1[1])).split('\'')[1]               
                if tool == 'clash':
                        CustomGroupvmess = 'http://{ip}/sub?target=clash&url={sub}&ruleset={rulesets}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,rulesets=rulesets)
                        api2 = 'https://gfwsb.114514.best/sub?target=clash&url={sub}&ruleset={rulesets}&groups={groups}'.format(sub=str(sub),groups=groups,rulesets=rulesets) 
                        return render_template('clash.html',sub = s,custom=ini,api=CustomGroupvmess,api2=api2)
                if tool == 'clashr':
                        CustomGroupvmess = 'http://{ip}/sub?target=clashr&url={sub}&ruleset={rulesets}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,rulesets=rulesets)
                        api2 = 'https://gfwsb.114514.best/sub?target=clashr&url={sub}&ruleset={rulesets}&groups={groups}'.format(sub=str(sub),groups=groups,rulesets=rulesets) 
                        return render_template('clashr.html',sub = s,custom=ini,api=CustomGroupvmess,api2=api2)
                if tool == 'surge':
                        CustomGroupvmess = 'http://{ip}/sub?target=surge&url={sub}&ruleset={rulesets}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,rulesets=rulesets)
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}&ruleset={rulesets}&groups={groups}'.format(sub=str(sub),groups=groups,rulesets=rulesets) 
                        return render_template('surge.html',sub = s,custom=ini,api=CustomGroupvmess,api2=api2)
                if tool == 'mellow':
                        CustomGroupvmess = 'http://{ip}/sub?target=mellow&url={sub}&ruleset={rulesets}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,rulesets=rulesets)
                        api2 = 'https://gfwsb.114514.best/sub?target=mellow&url={sub}&ruleset={rulesets}&groups={groups}'.format(sub=str(sub),groups=groups,rulesets=rulesets) 
                        return render_template('mellow.html',sub = s,custom=ini,api=CustomGroupvmess,api2=api2)
                if tool == 'surfboard':
                        CustomGroupvmess = 'http://{ip}/sub?target=surfboard&url={sub}&ruleset={rulesets}&groups={groups}'.format(ip=api.aff.subip,sub=str(sub),groups=groups,rulesets=rulesets)
                        api2 = 'https://gfwsb.114514.best/sub?target=surfboard&url={sub}&ruleset={rulesets}&groups={groups}'.format(sub=str(sub),groups=groups,rulesets=rulesets) 
                        return render_template('surfboard.html',sub = s,custom=ini,api=CustomGroupvmess,api2=api2)
                if tool == 'qxnode':
                        CustomGroupvmess = 'http://{ip}/api/qxnode?sublink={sub}'.format(ip=api.aff.apiip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=quanx&url={sub}'.format(sub=str(sub))
                        return render_template('qxnode.html',sub = s,custom="QuanX Node List 不支持客制化 ",api=CustomGroupvmess,api2=api2)            
                if tool == 'surnode':
                        CustomGroupvmess = 'http://{ip}/api/surnode?sublink={sub}&ver=4&udp=true&tfo=true'.format(ip=api.aff.apiip,sub=str(sub))
                        api2 = 'https://gfwsb.114514.best/sub?target=surge&url={sub}&ver=4&list=true&udp=true&tfo=true'.format(sub=str(sub))
                        return render_template('surgenode.html',sub = s,custom="默认为surge4，参数为为ver=4。默认udp=true,tfo=true",api=CustomGroupvmess,api2=api2)                                  
                else:
                    return render_template('ini.html')    
            else:
                return '订阅不规范'
        return render_template('ini.html')
        
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=10086)            #自定义端口