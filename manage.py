import time
from flask import Flask, request, make_response, url_for, session
from flask_script import Manager
from flask import redirect
#创建app
from werkzeug.exceptions import abort

from lala import user

app=Flask(__name__)
app.register_blueprint(user)
# 对APP 进行配置
app.config['myname']='bill'
app.config['SECRET_KEY']='1234543434 '

manage=Manager(app)

#配置路由及处理函数
@app.route('/')
def index():
    print(1/0)
    return 'helollo  miss huang'

@app.route('/nestedobj')
def nestefobj():
    myname=app.config['myname']='bill'
    return request.base_url + '.myname='+myname

@app.route('/user/<username>')
def welcome(username):
    print('welcome %s to register'%username)
    return 'hello lulululu'


@app.route('/user')
def reeee():
    abort(500)
    return 'cloris:;;just be perserved to make you quality fit your ambitious'

@app.route('/index')
def redir():
    abort(404)
    return redirect(url_for('reeee'))

@app.errorhandler(404)
def error(error):
    return 'fighting to create a light future'

@app.errorhandler(500)
def error(error):
    return 'everything is possible,,fighting to create a light future'

@app.route('/setcookie')
def setCookie():
    resp=make_response('cookie设置成功')
    resp.set_cookie('name','bill',expires=time.time()+30)
    return resp

@app.route('/getcookie')
def getCookie():
    cook=request.cookies.get('name','time is up')
    return cook

@app.route('/setsession')
def setSession():
    session['name'] = 'huang'
    return 'session shezhichenggong'

@app.route('/getsession')
def getSession():
    cook=session.get('name','zoudiule')
    return cook

@app.route('/error')
def error():
    a=4/0
    return a

@app.before_first_request
def bre():
    print('hrllosdjh')

@app.before_request
def reb():
    print('before request;',request)

@app.after_request
def ares(resp):
    print('after request rerrgggggg',request,resp)
    return resp

@app.teardown_request
def te(resp):
    print('tear_request')
    return resp


%HOMEDRIVE%%HOMEPATH%
%HOMEDRIVE%%HOMEPATH%

if __name__ == '__main__':
    # app.run(port=8003,debug = False)
    manage.run()
