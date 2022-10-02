from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("login.html")

database = {'aditi':'1234',"sam":'5678'}

@app.route('/login',methods=['POST'])
def login():
     if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        print(username,password)
        if username not in database:
            print('first')
            return render_template('login.html',info='invalid user')
        else:
            print('sec')
            if database[username]!=password:
                return render_template('login.html',info='invalid user')
            else:
                return render_template('home.html',name=username)



if __name__ == '__main__':
    app.run()

# from flask import Flask,request,render_template
# import pickle
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return render_template("login.html")
# database={'aditi':'1234','sam':'aditi','samiti':'987'}
#
# @app.route('/form_login',methods=['POST','GET'])
# def login():
#     username=request.form['username']
#     pwd=request.form['password']
#     if username not in database:
# 	    return render_template('login.html',info='Invalid User')
#     else:
#         if database[username]!=pwd:
#             return render_template('login.html',info='Invalid Password')
#         else:
# 	         return 'Welcome'+"  "+ str(username.upper())
#
# if __name__ == '__main__':
#     app.run()