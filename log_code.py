#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "code wala page"
import cgi,cgitb

form=cgi.FieldStorage()
em=form.getvalue('email')
# print em
pwd=form.getvalue('psd')
# print pwd

import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","school",3306)
cursor=con.cursor()

query="select * from tbl_stu where Email='%s'"%(em)
cursor.execute(query)
data=cursor.fetchone()

if data[1]==em:
	if data[2]==pwd:
		print """<script>window.location.href='dashboard.py?id=%s';</script>"""%data[1]
	else:
		print """<script>alert('Email or Password does not matched');</script>"""
else:
	print """<script>alert('email does not match');</script>"""	
# 	print "<script>window.location.href='dashboard.py?id="+em+"'</script>"
# else:
# 	print """
# 	<script>window.location.href="register.py"</script>
# 	"""