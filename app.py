from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.render_template('indexNoAI.html')


if __name__ == '__main__':
   app.run("127.0.0.1",5050,debug=True)
