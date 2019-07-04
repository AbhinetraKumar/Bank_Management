import pymysql

class Start:
    def enter(self):
        t = True
        while t:
            print("- ₹ BANK MANAGEMENT SYSTEM ₹ -")
            print(' Enter 1 to Registered LOGIN \n Enter 2 to OPEN ACCOUNT and REGSITER \n Enter 3 for Manager LOGIN to check all account holders \nEnter 4 to EXIT \n')
            i = int(input("Enter the choice : "))
            if i == 2:
                r = register()
                r.reg()
            elif i == 1:
                l = login()
                l.log()
            elif i==3:
                l=mlogin()
                l.log()
            else:
                print("Exited")
                t = False


class register:
    def reg(self):
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        accno = int(input("Enter the account no of your choice [min 4 digit] - [max 6 digit]: "))
        name = input("Enter the account holder name : ")
        typee = input("Ente the type of account [C/S] : ")
        deposit = int(input("Enter The Initial amount (zero balance accounts available)"))
        password = input("Enter pin : ")
        cursor = db.cursor()
        try:
            cursor.execute('insert into account values("%d","%s","%s","%d","%s")' % (accno, name, typee, deposit, password))
            print("\nregistered")
        except:
            print("Account number already taken , please select any other account number of your choice\n")
        db.commit()
        
        db.close()


class login:
    def log(self):
        ssn1 = input("Enter the account no of your choice [min 4 digit]: ")
        password1 = input("Enter the pin : ")
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        cursor = db.cursor()
        cursor.execute("select * from account where accno='" + ssn1 + "' and password='" + password1 + "'")
        data = cursor.fetchall()
        if not data:
            print("\n!!!Invlaid details")

        else:
            e = enter1()
            e.ent()
        db.commit()
        db.close()

class mlogin:
    def log(self):
        ssn1 = input("Enter the manger ID : ")
        password1 = input("Enter the pin : ")
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        cursor = db.cursor()
        cursor.execute("select * from man where manid='" + ssn1 + "' and manpin='" + password1 + "'")
        data = cursor.fetchall()
        if not data:
            print("\n!!!Invlaid details")

        else:
            print("ALL ACCOUNT HOLDER'S LIST\n\n")
            d2 = allholder()
            d2.aholder()
        db.commit()
        db.close()


class enter1:
    def ent(self):
        t = True
        while t:
            print("\n\t****MAIN MENU****")
            print("\t1. DEPOSIT AMOUNT")
            print("\t2. WITHDRAW AMOUNT")
            print("\t3. BALANCE ENQUIRY")
            print("\t4. CLOSE AN ACCOUNT")
            print("\t5. MODIFY AN ACCOUNT")
            print("\t6. EXIT")
            i = int(input("Enter your choice : "))
            if i == 1:
                d = deposite()
                d.depo()
            elif i == 2:
                all = withdraw()
                all.withd()
            elif i == 3:
                b = balance()
                b.bal()
            elif i == 4:
                d = delete()
                d.dele()
            elif i == 5:
                u = update()
                u.up()
            elif i == 6:
                print
                "Exited"
                t = False
            else:
                print("!!!INVALID OPTION")


class allholder:
    def aholder(self):
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        cursor = db.cursor()
        cursor.execute("select accno, name from account")
        data = cursor.fetchall()
        if not data:
            print("No Accounts\n")
        else:
            print("->>>Account No  --    Name")
            for row in data:
                print("->>>   %d   --    %s" % (row[0], row[1]))
        print("\n\n\n")
        db.commit()
        db.close()


class deposite:
    def depo(self):
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        cursor = db.cursor()
        num = int(input("Enter The account No. : "))
        cursor.execute("select deposit, accno from account where accno = '%d' " % num)
        data = cursor.fetchall()
        if not data:
            print("!! No RECORD  !!")
        else:
            k = data[0][0]
            i = int(input("Enter the deposite amount : "))
            k += i
            cursor.execute("update account set deposit = '%d' where accno = '%d'" % (k, num))
        db.commit()
        db.close()

class withdraw:
    def withd(self):
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        cursor = db.cursor()
        num = int(input("Enter The account No. : "))
        cursor.execute("select deposit, accno from account where accno = '%d' " % num)
        data = cursor.fetchall()
        if not data:
            print("!! No RECORD  !!")
        else:
            k = data[0][0]
            i = int(input("Enter the withdraw amount : "))
            k -= i
            cursor.execute("update account set deposit = '%d' where accno = '%d'" % (k, num))
            print(" ₹ %d deducted from your account please select 3 to check balance\n"%i)
        db.commit()
        db.close()

class balance:
    def bal(self):
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        cursor = db.cursor()
        num = int(input("Enter The account No. : "))
        cursor.execute("select deposit from account where accno = '%d' " % num)
        data = cursor.fetchall()
        if not data:
            print("!! No RECORD  !!")
        else:
            k = data[0][0]
            print("Your current balance is : Rs %d Only\n" % k)
        db.commit()
        db.close()


class delete:
    def dele(self):
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        cursor = db.cursor()
        try:
            acno = int(input("\nEnter Account No : "))
            cursor.execute("delete from account where accno = '%d'" % acno)
            db.commit()
            print("\nAccount CLOSED !!")
        except:
            print("\n!!!Cannot CLOSE, Enter valid details !!")
            db.rollback()
        db.close()


class update:
    def up(self):
        db = pymysql.connect(user='root', password='', host='localhost', database='bank')
        cursor = db.cursor()
        try:
            acc = int(input("\nEnter Account No : "))
            cursor.execute("select * from account where accno ='%d'" % acc)
            data = cursor.fetchall()
            if not data:
                print("Wrong DETAILS !! \n")

            else:
                nam = input("Enter the NAME : ")
                typ = input("Enter the Account TYPE : ")
                dep = int(input("Enter the Current DEPOSIT :"))
                passw = input("Enter the PASSWORD : ")
                cursor.execute("update account set name ='%s',type ='%s',deposit = '%d',password ='%s' where accno ='%d'" % (
                        nam, typ, dep, passw, acc))
                db.commit()
                print("\nACCOUNT MODIFIED !!")

                cursor.execute("select * from account where accno = '%d'" % acc)
                data = cursor.fetchall()
                for row in data:
                    print("\nAccount No = %d" % row[0])
                    print("Name = %s" % row[1])
                    print("Account Type = %s" % row[2])
                    print("Current Balance = %d" % row[3])
        except:
            print("\n!!!INVALID \n")
            db.rollback()
        db.close()

s = Start()
s.enter()
