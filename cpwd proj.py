import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='1234',database='CPWD')
con.autocommit=True
if con.is_connected():
    print('connected sucessfully')
else:
    print('not connected')
C1=con.cursor()
def main():
    print(70*'*')
    print('****WELCOME TO Complaint management SERVICE****')
    print('1.REGISTER COMPLAINT')
    print('2.SEARCH RECORDS')
    print('3.CHECK STATUS (URGENT) ')
    print('4.UPDATE RECORD')
    print('5.DELETE RECORD')
    print('6.ENTER FEEDBACK')
    print('7.DISPLAY ALL RECORDS')
    print('8.EXIT')
    print(70*'*')
    
def register():
        print('THANK YOU FOR CHOOSING OUR SERVICES!')
        print('Kindly fill in your complaint details: ')
        print(60*'#')
        a=    input('Enter Name: ')
        b=int(input('Enter mobile number: '))
        c=   (input('Enter address: '))
        d=   input('Enter complaint details: ')
        e=   (input('Enter if complaint is urgent: (y/n):  '))
        print(60*'#')
        g='N'
        data=(a,b,c,d,e)
        SQL="insert into info(name,mobile,address,complaints,urgency,resolved) values('{}',{},'{}','{}','{}','{}')".format(a,b,c,d,e,g)
        C1.execute(SQL)
        con.commit()
        print('your complaint has been registered.')
def searchrecords():
        print('to display all the details of the person on the basis of name')
        str1=input('enter name of person whose record you want to see:  ')
        SQL=("select * from info where name='{}'".format(str1))
        C1.execute(SQL)
        rows=C1.fetchall()
        for i in rows:
            print(i)
def checkstatus():
        print('To display all the details of the urgent records')
        SQL=('select * from info where urgency="y"')
        C1.execute(SQL)
        rows=C1.fetchall()
        for i in rows:
            print(i)
def updatedetails():
        up=input('enter Sno of the person whose record you want to update:  ')
        r=input('has the issue been resolved(y/n): ')
        SQL="update info set resolved=('{}') where sno=('{}')".format(r,up)
        C1.execute(SQL)
        con.commit()
        print('record succesfully updated.')
def deleterecord():
        a=input('enter name of the person whose record you want to delete:  ')
        SQL="delete from info where name ='{}'".format(a)
        C1.execute(SQL)
        con.commit()
        print('succesfully deleted record')
def feedback():
        a=input('enter your name: ')
        f=input('enter feedback: ')
        SQL="update info set feedback='{}' where name='{}'".format(f,a)
        C1.execute(SQL)
        con.commit()
        print('thankyou for your feedback')
def displayallrecord():
        SQL=('select * from info')
        C1.execute(SQL)
        rows=C1.fetchall()
        for i in rows:
            print(i)
while True:
    main()
    ch=int(input('ENTER CHOICE ***1/2/3/4/5/6***: '))
    if ch==1:
        register()
    elif ch==2:
        searchrecords()
    elif ch==3:
        checkstatus()
    elif ch==4:
        updatedetails()
    elif ch==5:
        deleterecord()
    elif ch==6:
        feedback()
    elif ch==7:
        displayallrecord()
    elif ch==8:
        break
    print('****DO YOU WANT TO ENTER MORE****')
    ANS=input('ENTER ANS Y/N:  ')
    if ANS=="N" or ANS=='n':
        break
