from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! 기말 우뜨콰라고'

@app.route('/soccer')
def soccer():
    return 'Hello, soccer!'

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/youtube', methods=['GET', 'POST'])
def youtube():
    linklist = ["https://www.youtube.com/embed/FhLD58QnRM4?si=XFUJjxIy2k3__1KV","https://www.youtube.com/embed/GnSmlzpiHVE?si=p4jt7jLs_Lfl-39R"]
    keyword = request.form["keyword"]
    print(keyword)
    linknum = 0 # 0은 호피폴라, 1은 하현상
    if keyword == '호피폴라':
        linknum = 0
    elif keyword == '하현상':
        linknum = 1
    else:
        print('잘못된 입력')

    return render_template('youtube.html', name=keyword, link=linklist[linknum])

@app.route('/ytpage')
def ytpage():
    return render_template('ytpage.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        keyword = request.form["keyword"]
        print(keyword)
        return f"POST로 전달된 당신이 입력한 검색어: {keyword}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")