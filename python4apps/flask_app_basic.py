from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/hello')
def say_hello():
  return 'Hello from Server'
  
@app.route('/number/<int:num>')
def say_number(num):
  return 'You are looking for this number :' + str(num)  
  
@app.route('/add_number/<int:num1>/<int:num2>')
def add_number(num1,num2):
  return str(num1) + ' + ' + str(num2) + ' = ' + str(num1 + num2)   