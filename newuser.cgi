#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb

#mysql database connectivity

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dbuser",
  passwd="Resi*123",
  database="users"
)

mycursor = mydb.cursor()
mycursor.execute("select * from login")
myresult = mycursor.fetchall() # it gives the list

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('uname')
password  = form.getvalue('passwd')
repassword = form.getvalue('repasswd')

#fname = form.getvalue('fname')
#lname = form.getvalue('lname')

username = "'"+username+"'"
password1 = "'"+password+"'"




fname = "'"+'nullkk'+"'"
lname = "'"+'nullkk'+"'"

print("Content-type:text/html\r\n\r\n")

wrongbtn = '''
<h1> New password and Confirm password doesn't match </h1>
<button id="myButton" class="float-leftsubmit-button" >Go Back</button>

<style>
.float-leftsubmit-button {
  background-color: #4CAF50;
    border: none;
      color: white;
        padding: 5px 20px;
          text-align: center;
            text-decoration: none;
              display: inline-block;
                font-size: 16px;
                  margin: 4px 2px;
                    cursor: pointer;
                    }
</style>



<script type="text/javascript">
    document.getElementById("myButton").onclick = function () {
            location.href = "http://13.233.94.154/index.html";
                };
                </script>

'''



if password == repassword:
    query = 'INSERT INTO `login` VALUES ('+username+','+password1+','+fname+','+lname+')'
    result  = mycursor.execute(query)
    mydb.commit()
    print('<script>window.location.href="http://13.233.94.154/index.html";</script>')

else:
    print(wrongbtn)
