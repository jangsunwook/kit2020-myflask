from flask import Flask, request, render_template , redirect, url_for, abort
app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hellovar(name):
    return 'Hello, {}!'.format(name)

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "도라에몽"
    elif num == 2:
        return "진구"
    elif num == 3:
        return "퉁퉁이"    
    else:
        return "없어요"

    #return 'Hello, {}!'.format(name)

@app.route('/naver')
def naver():
    return redirect ("http://naver.com/")
    #return render_template("naver.html")

@app.route('/kakao')
def daum():
    return redirect ("http://daum.net/")

@app.route('/urltest')
def url_test():
    return redirect (url_for('naver'))

@app.route('/move/<site>')
def move_site(site):
    if site == 'naver':
        return redirect(url_for('naver'))
    elif site == 'naver':
        return redirect(url_for('daum'))    
    else:
        abort(404)

        #redirect '없는 페이지입니다'  

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.route('/img')
def img():
    return render_template("image.html")

  

#로그인

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']   
        pw = request.form['pw'] 
        print(id,type(id))
        print(pw,type(pw))
        #id와pw가 임의로 정한 값이랑 비교해서 맞으면 맞다 틀리면 틀리다.
        if id == 'abc' and pw == '1234':
            return "안녕하세요~ {} 님" .format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요."    

        

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        return 'POST 이다.학번은: {} 이름은: {}'.format(num, name)   
    return 'Hello, World!'    

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)   