# coding=utf-8
import sys
import flask_restful
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

from flask import Flask,render_template,request
urllib3.disable_warnings()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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
                    
                sub = urllib.parse.quote(s)
                name = urllib.parse.quote(n)
                custom = urllib.parse.quote(c)
                custommethod = urllib.parse.quote(method) 
                try:
                    tool=str(request.values.get('tool'))
                except :
                    pass
                if tool == 'clash':
                        CustomGroupvmess = 'http://{ip}/api/clash?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                        return render_template('clash.html',sub = s,custom=n+c+method,api=CustomGroupvmess)

                if tool == 'clashr':
                        CustomGroupvmess = 'http://{ip}/api/clashr?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                        return render_template('clashr.html',sub = s,custom=n+c+method,api=CustomGroupvmess)
                if tool == 'surge':
                        CustomGroupvmess = 'http://{ip}/api/surge?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                        return render_template('surge.html',sub = s,custom=n+c+method,api=CustomGroupvmess)

                if tool == 'mellow':
                        CustomGroupvmess = 'http://{ip}/api/mellow?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                        return render_template('mellow.html',sub = s,custom=n+c+method,api=CustomGroupvmess)
                if tool == 'surfboard':
                        CustomGroupvmess = 'http://{ip}/api/surfboard?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                        return render_template('surfboard.html',sub = s,custom=n+c+method,api=CustomGroupvmess)
                if tool == 'qxnode':
                        CustomGroupvmess = 'http://{ip}/api/qxnode?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                        return render_template('qxnode.html',sub = s,custom="QuanX Node List 不支持客制化 ",api=CustomGroupvmess)            
                if tool == 'surnode':
                        CustomGroupvmess = 'http://{ip}/api/surnode?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}&type=v2'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                        return render_template('surgenode.html',sub = s,custom="Surge Node List 不支持客制化 ",api=CustomGroupvmess)                   
                if tool == 'surnodess':
                        CustomGroupvmess = 'http://{ip}/api/surnode?sublink={sub}&name={name}&gp={custom}&gpm={custommethod}&type=ss'.format(ip=api.aff.apiip,sub=str(sub),name=str(name),custom=str(custom),custommethod=str(custommethod))
                        return render_template('surgenode.html',sub = s,custom="Surge Node List 不支持客制化 ",api=CustomGroupvmess)                  
                else:
                    return render_template('index.html')    
            else:
                return '订阅不规范'
        return render_template('index.html')
    except Exception as e:
        return e

@app.route('/api/clash', methods=['GET', 'POST'])
def clashapigroup():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        return api.subconverter.Retry_request('http://127.0.0.1:10010/sub?target=clash&url='+sub)        
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

@app.route('/api/clashr', methods=['GET', 'POST'])
def clashr():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        return api.subconverter.Retry_request('http://127.0.0.1:10010/sub?target=clashr&url='+sub)        
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

@app.route('/api/surge', methods=['GET', 'POST'])
def surge():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        #return api.subconverter.Retry_request('http://127.0.0.1:10010/surge?url='+sub+'&ver=4')     
        return api.subconverter.Retry_request('http://127.0.0.1:10010/sub?target=surge&url='+sub+'&ver=4')        
   
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

@app.route('/api/qxnode', methods=['GET', 'POST'])
def qxnode():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        return api.subconverter.Retry_request('http://127.0.0.1:10010/sub?target=quanx&url='+sub)        
     
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

@app.route('/api/mellow', methods=['GET', 'POST'])
def mellow():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        return api.subconverter.Retry_request('http://127.0.0.1:10010/mellow?url='+sub)        
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

@app.route('/api/surfboard', methods=['GET', 'POST'])
def surfboard():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''

        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''

        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        api.subconverter.writeini(name,custom,custommethod)
        return api.subconverter.Retry_request('http://127.0.0.1:10010/sub?target=surfboard&url='+sub)        
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

@app.route('/api/surnode', methods=['GET', 'POST'])
def surnode():
    try:
        sub = request.args.get('sublink')
        try:
            name = request.args.get('name')
        except Exception as e:
            name = ''
        try:
            custom = request.args.get('gp')
        except Exception as e:
            custom = ''
        try:
            custommethod = request.args.get('gpm')
        except Exception as e:
            custommethod = ''
        try:
            surgetype = request.args.get('type')
        except Exception as e:
            surgetype = 'ss'         
        
        return api.subconverter.Retry_request('https://dove.589669.xyz/Mix2Surge?type={surgetype}&sub='.format(surgetype=surgetype)+sub) 
      
    except Exception as e:
        return '检测调用格式是否正确'+ api.aff.aff

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=10086)            #自定义端口