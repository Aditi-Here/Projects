from flask import Flask,render_template,request
import pickle
from database import adi_col_name
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("login.html")

@app.route('/createaccount')
def create():
    return render_template("createaccount.html")

@app.route('/reteivepassword')
def reteivePassword():
    return render_template("reterivePassword.html")


database=adi_col_name.find()
print("database: ",database)
database_list=[]
for item in database:
    print(item)
    database_list.append(item)

# adi_col_name.delete_many({})
#
# print('list:',database_list[1]['username'])
#
database_username_aditi_list=[]
database_username_aditi=adi_col_name.find({'username':'aditi'})
print("database username aditi: ",database_username_aditi)
for items in database_username_aditi:
    database_username_aditi_list.append(items)

print('database_username_aditi_list',database_username_aditi_list)



@app.route('/create',methods=['POST'])
def addNewUser():
    # adi_col_name.insert_one(Student2)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        adi_col_name.insert_one({'username':username,'password':password})
        return render_template('home.html', name=username)

#@app.route('/create',methods=['POST'])
# def login():
#      if request.method=='POST':
#         username=request.form['username']
#         password=request.form['password']
#         print(username,password)
#
#         if adi_col_name.find({'$and': [{'username':username},{'password':password}]}):
#             print('first')
#             return render_template('home.html', name=username)
#         else:
#             return render_template('login.html',info='invalid username or password')
#
#
#
#

if __name__ == '__main__':
    app.run(debug=False)

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