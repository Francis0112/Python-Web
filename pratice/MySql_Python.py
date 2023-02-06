

# day 7 Database Exercise
# i will do it java style with classes and objects, returned method and parameterized crud methods
# Crud Operation
# Recap 

import mysql.connector
from mysql.connector import Error

class Connect():

    def connection(self):
        try:
            con = mysql.connector.connect(host='localhost',database='onegai',user='root',password='')
            if con.is_connected():
                db_info = con.get_server_info()
                print("Connected to Mysql Server version: ",db_info)
                cursor = con.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("you are connected to: ", record)
        except Error as e:
                print("Error while connecting to mysql ",e)
        return con
    
class tables():

    def table_hospital(self):
        query = """create table hospital(
        Hospital_id int primary key not null auto_increment,
        Hospital_name varchar(100) not null,
        Bed_count int null
        );"""
        try:
            con1 = Connect().connection()
            cursor = con1.cursor()
            cursor.execute(query)    
            print("Hospital Table Created!")
        except Error as e:
            print(e)
        cursor.close()
        con1.close()

    def table_doctor(self):
        query = """create table doctor(
        Doctor_Id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        Doctor_Name VARCHAR(100) NOT NULL, 
        Hospital_Id INT NOT NULL, 
        Joining_Date DATE NOT NULL, 
        Speciality VARCHAR(100) NULL, 
        Salary INT NULL, 
        Experience INT NULL
        );"""
        try:
            con1 = Connect().connection()
            cursor = con1.cursor()
            cursor.execute(query)
            print("Doctor Table Created!")
        except Error as e:
            print(e)
        cursor.close()
        con1.close()

class crud():

    con1 = Connect().connection()
    cur = con1.cursor()

    def insert_hospital(self,name,bed):
        data = [name,bed]
        cmd = """insert into hospital (hospital_name, bed_count) values (%s,%s);"""
        self.cur.execute(cmd,data)
        self.con1.commit()
        print("Data Inserted!")
        self.con1.close()
        self.cur.close()

    def update_hospital(self,nid, name, bed):
        data = [name,bed,nid]
        cmd = """update hospital set hospital_name=%s, bed_count=%s where hospital_id=%s"""
        self.cur.execute(cmd,data)
        self.con1.commit()
        print("Data Updated!")
        self.cur.close()
        self.con1.close()

    def delete_hospital(self,Nid):
        data = [Nid]
        cmd = """delete from hospital where hospital_id=%s"""
        self.cur.execute(cmd, data)
        self.con1.commit()
        print("Data Deleted!")
        self.cur.close()
        self.con1.close()

    def display_hospital(self):
        cmd = """select * from hospital"""
        self.cur.execute(cmd)
        records = self.cur.fetchall()
        for i in records:
            print(i)
    
    def insert_doctor(self,name,hospital_id, speciality, salary, experience):
        data = [name, hospital_id, speciality, salary, experience]
        cmd = """insert into doctor (Doctor_name, hospital_id, Joining_Date, Speciality, Salary, Experience) values (%s,%s,CURDATE(),%s,%s,%s)"""
        self.cur.execute(cmd,data)
        self.con1.commit()
        print("Data Inserted!")
        self.cur.close()
        self.con1.close()

    def update_doctor(self, Nid, name,hospital_id, speciality, salary, experience):
        data = [name,hospital_id,speciality,salary,experience,Nid]
        cmd = """update doctor set Doctor_name=%s,Hospital_id=%s,Speciality=%s,Salary=%s,Experience=%s where Doctor_id=%s"""
        self.cur.execute(cmd, data)
        self.con1.commit()
        print("Data Updated!")
        self.cur.close()
        self.con1.close()

    def delete_doctor(self, Nid):
        data = [Nid]
        cmd="""delete from doctor where Doctor_id=%s"""
        self.cur.execute(cmd, data)
        self.con1.commit()
        print("Data Deleted!")
        self.cur.close()
        self.con1.close()

    def display_doctor(self):
        query = """select * from doctor"""
        self.cur.execute(query)
        records = self.cur.fetchall()
        for i in records:
            print(i)

        
# naruto = tables()
# naruto.table_hospital()
# naruto.table_doctor()

# sam = crud()
# sam.insert_hospital("ASIAN Hospital and Medical Center", 820)
# sam.update_hospital(nid=2,bed=123,name="umbrella hospital")
# sam.display_hospital()
# sam.delete_hospital(7)

# sam.insert_doctor(name="Ed Caluag",hospital_id=4,speciality="Spirit Healing",salary=44124,experience=13)
# sam.update_doctor(Nid=3,name="doc willi Ong",hospital_id=23,speciality="Online Diagnosis",salary=123456789,experience=12)
# sam.display_doctor()
# sam.delete_doctor(1)
# sam.delete_doctor(2)
# sam.display_doctor()
# sam.display_hospital()

# Question 2: Fetch Hospital and Doctor Information using hospital Id and doctor Id
def get_doctor_id(Nid):
    a = Connect().connection()
    c = a.cursor()
    data = [Nid]
    cmd = """select * from doctor where Doctor_id=%s"""
    c.execute(cmd, data)
    res = c.fetchone()
    for i in res:
        print(i, end=" ")


def get_hospital_id(Nid):
    a = Connect().connection()
    c = a.cursor()
    data = [Nid]
    cmd = """select * from hospital where Hospital_id=%s"""
    c.execute(cmd, data)
    res = c.fetchone()
    for i in res:
        print(i, end=" ")

# get_doctor_id(1)
# get_hospital_id(2)


# Exercise 3: Get a list of doctors from a given hospital
def list_doctors(hos_id):
    a = Connect().connection()
    c = a.cursor()
    data = [hos_id]
    cmd = """select * from doctor where Hospital_id=%s"""
    c.execute(cmd, data)
    res = c.fetchall()
    for i in res:
        print(i)
# list_doctors(1)


# Exercise 3: Get the list Of doctors as per the given specialty
def undiscover(spec):
    data = [spec]
    a = Connect().connection()
    c = a.cursor()
    cmd = """select * from doctor where speciality=%s"""
    c.execute(cmd,data)
    res = c.fetchall()
    for i in res:
        print(i)
# undiscover("undiscover")

