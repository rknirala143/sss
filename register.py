#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
# print "Register page"
print """
<!DOCTYPE html>
<html>
<head>
	<title>Register  |   Student</title>
	<link rel="icon" type="images/gif" href="login.gif">
</head>
<body>
<form action="reg_code.py" method="post" accept-charset="utf-8">
	<table>
		<tr><td>Name</td><td><input type="text" name="name" required=""></td></tr>
		<tr><td>Father's name</td><td><input type="text" name="fname" required=""></td></tr>
		<tr><td>Gender</td><td><input type="radio" name="a" value="Male" required="">Male<input type="radio" name="a" value="Female" required="">Female</td></tr>
		<tr><td>Mobile No</td><td><input type="number" name="mob" required=""></td></tr>
		<tr><td>Email</td><td><input type="email" name="email" required=""></td></tr>
		<tr><td>Password</td><td><input type="password" name="psd" required=""></td></tr>
		<!-- <tr><td>Image</td><td><input type="file" name="img"></td></tr> -->
		<tr><td><input type="submit" value="Submit"></td></tr>
	</table>
</form>
</body>
</html>
"""