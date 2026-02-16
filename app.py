from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Cloud Computing - Flask App</h1>
        <p>Welcome! Jay Jaiswal .</p>
        <p>Subject: Cloud Computing | Week 2</p>
    '''

@app.route('/about')
def about():
    return '<h2>About</h2><p>Simple Flask application for cloud deployment.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

