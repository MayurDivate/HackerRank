from flask import Flask

app = Flask('Mayur')

@app.route('/')
def index_html():
    welocome_msg =  'This is a Welcome page of my First Flask app.  <a href="/about"> Click here to know more </a>'

    return welocome_msg

@app.route('/about')
def hello_word():
    return 'Hi I am FLASK!'

if __name__ == '__main__':
    app.run()