# Contact-Information
### Libraries required :
  * flask
  * flask_wtf
  * wtforms
  * wtforms_validators
  * pymysql
  * flask_wtf.csrf
  * smtplib
  * pymysql
### How to run(Ubuntu Terminal) ?
* create folder with any name.
* Move to newly created folder using cd command.
* Create folder named as templates and static.
* Download contactinfo.py from repository and store it in current directory.
* Download config.py from repository and store it in current directory.
* Now move to templates directory
* Download contactinfo.html from repository and save it in templates.
* Download contactinfo.sql from repository and store it in templates.
* Using below command dump the contactinfo.sql in your mysql database.
        sudo mysqldump contactinfo < contactinfo.sql
* Move to the directory where contactinfo.py is present
* Run contactinfo.py in terminal(Ubuntu) using command :
        python contactinfo.py

### Note : In contactinfo.py at line no. 43 and 44, Enter your email id and password. so that mail will be sent from your email id.

