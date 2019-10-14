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
username = form.getvalue('Username')
password  = form.getvalue('Password')


button1 ='''
<button id="myButton" class="float-leftsubmit-button" >CLICK TO TRY AGAIN</button>

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



for row in myresult:
        if (username == row[0]) and (password == row[1]):
                print("Content-type:text/html\n")
                print('<script>window.location.href="http://13.233.94.154/TravelGuide/main.html";</script>')

else:
	print("Content-type:text/html\n")
	print("<h2>Username and Password Incorrect</h2>")
	print(button1)


mycursor.close()



