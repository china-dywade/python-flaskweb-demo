
from flask import Flask, redirect, url_for, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("./login.html")


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


@app.route('/post/<int:post_id>')
def postId(post_id):
    return 'Hello %s!' % post_id


@app.route('/post/<path:pathUrl>')
def pathUrl(pathUrl):
    return 'Hello %s!' % pathUrl


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # 获取post(表单)参数
        user = request.form['nm']
        print(request)
        return redirect(url_for('success', name=user))
    else:
        # 获取get参数
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("chenshifeng", "shifengboy", max_age=3600)
    return resp


@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("chenshifeng")  # 获取名字为Itcast_1对应cookie的值
    return cookie_1


@app.route("/delete_cookies")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("chenshifeng")

    return resp


# Web 应用使用不同的 HTTP 方法处理 URL 。
# 当你使用 Flask 时，应当熟悉 HTTP 方法。
# 缺省情况下，一个路由只回应 GET 请求。
# 可以使用 route() 装饰器的 methods 参数来处理不同的 HTTP 方法:
# 方法	描述
# GET	以未加密的形式将数据发送到服务器，最常见的方法。
# HEAD	和GET方法相同，但没有响应体。
# POST	用于将HTML表单数据发送到服务器，POST方法接收的数据不由服务器缓存。
# PUT	用上传的内容替换目标资源的所有当前表示。
# DELETE	删除由URL给出的目标资源的所有当前表示。

# 设置静态文件地址
# url_for('static', filename='style.css')
if __name__ == '__main__':
    app.run(debug=True)
