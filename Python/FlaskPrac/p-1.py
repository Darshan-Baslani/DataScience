from flask import Flask

app = Flask(__name__)

@app.route('/')
def fun():
	return '<h1>Hello</h1>'

@app.route('/Darshan')
def darshan():
	return 'Hello, Darshan!'

@app.route('/<name>')
def name(name):
	return f"Hello, {name}"

if __name__ == '__main__':
	app.run()