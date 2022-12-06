import pymongo

USER_NAME='dbAditi'
PASSWORD='dbAditi'
client = pymongo.MongoClient(f"mongodb+srv://{USER_NAME}:{PASSWORD}@cluster0.wecdstw.mongodb.net/?retryWrites=true&w=majority")

DB='Record'
COLLECTION_NAME='Student'
adi_db=client[DB]
adi_col_name=adi_db[COLLECTION_NAME]
# Student1={'aditi':'1234',"sam":'5678'}
Student1={'username':'aditi','password':1234}
Student2={'username':'sam','password':5678}
# adi_col_name.insert_one(Student1)
# adi_col_name.insert_one(Student2)
# print(adi_col_name)

