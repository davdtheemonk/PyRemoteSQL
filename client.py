
import socket
import time
import sys

try:
    import pymysql
    pymysql.install_as_MySQLdb()
    db = pymysql.connect()

except ImportError:
    pass
s = socket.socket()



print(" ------------SQL PITTY CLIENT LITE ------------ \
      \n          write SQL code on the go \
      \n            /Code cheza kiwewe/ \
        \n ------- Connect only to your SQL server ------- \
            \n HELP :\
            \n 1.Username and Password required for login to database \
            \n 2.'root' is default username for most databases \
            \n 3.Leave password blank if database has no password \
            \n 4.Bug or Errors parishniclaus@gmail.com\
            \n 5.Make sure Your phpmyAdmin allows remote conections \
            \n     ***Happy Querying***")


class sock:

    def hostPort(self):
        self.host = str(input("REMOTE/LOCAL SERVER IP : "))
        self.port = [int(input("PORT TO CONNECT : "))]

    # Establishing connection to remote address,checks if the address can recieve a connection

    def connect(self):

        sec = 0
        if(self.host != 0) and (self.port != 0):
            while sec < 10:
                try:
                    s.connect((self.host, self.port))
                    print("Connected successfully to", self.host)
                    s.close()
                    sock.checkSQL(self)
                    break
    # 10 reconnection attempts before program terminates
                except:
                    sec += 1
                    print("an ERROR occured find relatable info : ", sys.exc_info()[
                          0], "\n Can't connect to remote address \n Reconnecting...")
                    sock.reconnect(self)
        else:
            print("ERROR : Transmit failed. Write a valid address \n")
            option = input("Press 'y' to exit ")
            if (option == 'y'):
                exit(-1)
            else:
                print("restart program please")

    def reconnect(self):
        time.sleep(5)
        try:
            s.connect((self.host, self.port))
            print("connected successfully to", self.host)
            s.close()
        except:
            print("ERROR : Cant connect to server")

    # Random check if phpMyAdmin is installed on remote address
    def checkSQL(self):
        host = self.host
        print("Making sure phpMyAdmin is installed in server\
                  \n Program will terminate if its not correctly installed.")
        try:
            c = open("host/phpMyAdmin/config.inc.php", 'r', encoding='utf-8')
            s = open("host/phpMyAdmin/sql.php", 'r', encoding='utf-8')
            v = open("host/phpMyAdmin/version_check.php",
                     'r', encoding='utf-8')
            i = open("host/phpMyAdmin/index.php", 'r', encoding='utf-8')
            if (c.seekable()) and (s.seekable()) and (v.seekable) and (i.seekable()):
                print("phpMyAdmin installed")
            else:
                print("phpMyAdmin not installed")
                exit(-1)
            sock.database(self)
        finally:
            c.close()
            s.close()
            v.close()
            i.close()

    # establishng connection to database
    def database(self):
        time.sleep(5)
        user = str(input("Enter user name :"))
        pwsd = str(input("enter password : "))
        db_name = input("Enter database name")
        try:
            db(self.host, user, pwsd, db_name)
            cursor = db.cursor()
            cursor.execute("SELECT VERSION();")
            data = cursor.fetchone()
            print("Connected Succesfully to ", db_name, " via host ", self.host, "\
                  \n       ---WELCOME---\
                  \n Your Database Version is %s : " % data)
            sql = raw_input("DB|", db_name, "|#> ")
            # check this part
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
                print("oops! this ", MySQLdb.exc_info()[
                      0], " occurred find relatable info")
        except:
            print("an ERROR occured find relatable info",
                  MySQLdb.exc_info()[0], "\n Terminating")
            exit(-1)
        db.close()


newConnection = sock()
newConnection.hostPort()
newConnection.connect()
