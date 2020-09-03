#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
# print "Login Wala Page"
print """
<!DOCTYPE html>
<html>
<head>
	<title>Login  |   Student</title>
		<link rel="icon" type="images/gif" href="login.gif">

</head>
<body>
<form action="log_code.py" method="post" accept-charset="utf-8">
	<table>
		<tr><td>Email</td><td><input type="email" name="email" required=""></td></tr>
		<tr><td>Password</td><td><input type="password" name="psd" required=""></td></tr>
		<tr><td><input type="submit" value="Submit"></td></tr>
	</table>
</form>
</body>
</html>
"""