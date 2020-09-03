#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
# print "Reg code"
import cgi,cgitb
data=cgi.FieldStorage()
n=data.getvalue('name')
# print n
fn=data.getvalue('fname')
# print fn
ge=data.getvalue('a')
# print ge
mob=data.getvalue('mob')
# print mob
em=data.getvalue('email')
# print em
pwd=data.getvalue('psd')
# print pwd
import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","school",3306)
cursor=db.cursor()
ins="insert into tbl_stu(Name,Fname,Gender,Mobile_no,Email,Password) values('%s','%s','%s','%s','%s','%s')"%(n,fn,ge,mob,em,pwd)
# query="insert into tbl_stu(Name,Fname,Gender,Mobile_no,Email,Password) values ('"+n+"','"+fn+"','"+ge+"','"+mob+"','"+em+"','"+pwd+"')"
res=cursor.execute(ins)
db.commit()
if res:
  ins1="insert into login(logmail,logpass) values('%s','%s')"%(em,pwd)
  cursor.execute(ins1)
  db.commit()
  print """<script>alert('Registration successfully');</script>"""
  print """<script>window.location.href="login.py"</script>"""
else:
  print "Data Not inserted" 