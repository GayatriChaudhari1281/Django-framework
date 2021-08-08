from flask import Flask
app=Flask(__name__)
@app.route('/demo')
def welcome():
	return '<h1>Shree Ganesh welcome to flask<h1/>'

app.run(port=7788)