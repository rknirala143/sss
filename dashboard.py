#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "Dashboard"
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","school",3306)
cur=con.cursor()
query="select * from tbl_stu where Email=''%s"%(pid)
cur.execute(query)
res=cur.fetchone()
print """
<!DOCTYPE html>
<html>
<head>
	<title>Dashboard    |  Home    |    Index</title>
	
</head>
<body>
<div class="main">
	<pre>
<span>Name   	:-   </span><span>%s</span></br>
<span>Email	:-   </span><span>%s</span></br>
<span>Password:-   </span><span>%s</span></br>
<span>Dob     :-   </span><span>%s</span></br>
<span>Mobile	:-   </span><span>%s</span></br>
<span>Mobile	:-   </span><span>%s</span>
</pre>

<!-- # <table border="1" align="center" style="background-color:red;color:white;height:200px;width:80%;border-radius:20px 20px 20px 20px;">
# 	<tr>
# 		<th>Name</th>
# 		<th>Fname</th>
# 		<th>Mobile</th>
# 		<th>Gender</th>
# 		<th>Email</th>
# 		<th>Password</th>
# 	</tr>
# """ -->
# for r in res:
# 	print "<tr>"
# 	print "<td>",r[0],"</td>"
# 	print "<td>",r[1],"</td>"
# 	print "<td>",r[3],"</td>"
# 	print "<td>",r[2],"</td>"
# 	print "<td>",r[4],"</td>"
# 	print "<td>",r[5],"</td>"
# 	print "</tr>"
# print """

# </table>
</div>	
</body>
</html>
"""%(data[1],data[2],data[3],data[4],data[5],data[6]pid)