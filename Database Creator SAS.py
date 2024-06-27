import mysql.connector as s
mc=s.connect(host='localhost',user='root',passwd='')
if mc.is_connected()==False:
    print("error")
else:
    print("ok")
cr=mc.cursor()
a="create database if not exists SAS;"
d="use SAS"

b="""create table if not exists result_hashes
(
 hashes             varchar(65)   NOT NULL  PRIMARY KEY );"""
try:
    cr.execute(a)
    mc.commit()
    print("1 ok")
except:
    print("error")
    mc.rollback()
#---------------------------------
try:
    cr.execute(d)
    mc.commit()
    print("2 ok")
except:
    print("error")
    mc.rollback()
#------------------------------------
try:
    cr.execute(b)
    mc.commit()
    print("3 ok")
except:
    print("error")
    mc.commit
#-----------------------------------

print("continue next step..............")
