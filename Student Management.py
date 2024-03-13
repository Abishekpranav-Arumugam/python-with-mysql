import mysql.connector as m
from tabulate import tabulate

d_obj = m.connect(host='localhost', database='database2', user='root', password='44-abcdef')

def view_all(s):
    res = d_obj.cursor()
    sql1 = "SELECT * FROM stud"
    res.execute(sql1)
    t_view1 = res.fetchall()
    print("\nStudent Details: \n")
    print(tabulate(t_view1, headers=["Name", "Roll_no", "Mail", "Phone_no"]))
    
    print("\n")
    
    sql2 = "SELECT * FROM acad"
    res.execute(sql2)
    t_view2 = res.fetchall()
    print("\nAcademics Table: \n")
    print(tabulate(t_view2, headers=["Roll_no", "Sem_1", "Sem_2", "Sem_3"]))
    
  
def stud_det(s):
    res = d_obj.cursor()
    sql1 = "SELECT * FROM stud"
    res.execute(sql1)
    t_view1 = res.fetchall()
    print("\nStudent Details: \n")
    print(tabulate(t_view1, headers=["Name", "Roll_no", "Mail", "Phone_no"]))
    print("\n")
    print("1. View ")
    print("2. Back ")
    print("\n")
    ch=int(input())
    if ch==1 :
        view_all(s)
    elif ch== 2:
        pass
    else:
        print("Invalid")

def stud_acad(s):
    res = d_obj.cursor()
    sql2 = "SELECT * FROM acad"
    res.execute(sql2)
    t_view2 = res.fetchall()
    print("\nAcademics Table: \n")
    print(tabulate(t_view2, headers=["Roll_no", "Sem_1", "Sem_2", "Sem_3"]))
    print("\n")
    print("1. View ")
    print("2. Back ")
    print("\n")
    ch=int(input())
    if(ch==1):
        view_all(s)
    elif ch== 2:
        pass
    else:
        print("Invalid")

def delete(s):
    print("1. Student Details ")
    print("2. Student Academics ")
    print("\n")
    ch=int(input("Enter field you want to delete : "))
    print("\n")
    
    if ch == 1:
        sid = input("Enter Student Roll no:")
        res = d_obj.cursor()
        sql = "DELETE FROM stud WHERE Roll_no=%s"
        res.execute(sql, (sid,))
        d_obj.commit()
        print("\nRecord Deleted Successfully...!!!") 
        
    elif ch == 2:
        sid = input("Enter Student Roll no:")
        res = d_obj.cursor()
        sql = "DELETE FROM acad WHERE Roll_no=%s"
        res.execute(sql, (sid,))
        d_obj.commit()
        print("\nRecord Deleted Successfully...!!!")
        
    else:
        print("Invalid ")
    
def stud_in(s):
    print("1. Student Details ")
    print("2. Academics Details ")
    print("\n")
    ch=int(input("Enter the field to insert : "))
    print("\n")
    if(ch==1):
        Name = input("Enter the student Name: ")
        Roll_no = input("Enter the Roll number: ")
        Mail = input("Enter the Mail ID: ")
        Phone_no = input("Enter the Phone number: ") 
    
        try:
            res = d_obj.cursor()
            sql = "INSERT INTO stud (Name, Roll_no, Mail, Phone_no) VALUES (%s, %s, %s, %s)"
            res.execute(sql, (Name, Roll_no, Mail, Phone_no))
            d_obj.commit()
            print("\nRecord Inserted successfully")
        except m.Error as e:
            print(f"Error: {e}")
            
    elif ch == 2:
        Roll_no = input("Enter the Roll no: ")
        sem_1 = float(input("Enter the semester1 CGPA: ")) 
        sem_2 = float(input("Enter the semester2 CGPA: "))
        sem_3 = float(input("Enter the semester3 CGPA: "))
    
        try:
            res = d_obj.cursor()
            sql = "INSERT INTO acad (Roll_no, sem_1, sem_2, sem_3) VALUES (%s, %s, %s, %s)"
            res.execute(sql, (Roll_no, sem_1, sem_2, sem_3))
            d_obj.commit()
            print("\nRecord Inserted successfully")
        except m.Error as e:
            print(f"Error: {e}")
        
    else:
        print("Invalid")
        
def stud_up(s):
    print("1. Student Details ")
    print("2. Student Academics Details ")
    print("\n")
    ch=int(input("Enter the field to be updated : "))
    if ch==1:
        print("\n")
        print("1. Name")
        print("2. Roll No")
        print("3. Mail ID")
        print("4. Phone No")
        print("\n")

        option = int(input("\nWhich field do you want to update : "))

        if option == 1:
            Roll_no = input("Enter Roll no:")
            Name = input("Enter new Name:")
            cur = d_obj.cursor()
            sql = "UPDATE stud SET Name=%s WHERE Roll_no=%s"
            cur.execute(sql, (Name, Roll_no))
            d_obj.commit()
            stud_det(s)
            print("\nUpdate Successful")
        elif option == 2:
            current_roll_no = input("Enter Roll no:")
            new_roll_no = input("Enter new Roll no:")
            cur = d_obj.cursor()
            sql = "UPDATE stud SET Roll_no=%s WHERE Roll_no=%s"
            cur.execute(sql, (new_roll_no, current_roll_no))
            d_obj.commit()
            stud_det(s)
            print("\nUpdate Successful")
        elif option == 3:
            Roll_no = input("Enter Roll no :")
            Mail = input("Enter new Mail ID : ")
            cur = d_obj.cursor()
            sql = "UPDATE stud SET Mail=%s WHERE Roll_no=%s"
            cur.execute(sql, (Mail, Roll_no))
            d_obj.commit()
            stud_det(s)
            print("\nUpdate Successful")
        elif option == 4:
            Roll_no = input("Enter Roll no :")
            phone_no = input("Enter new Phone No :")
            cur = d_obj.cursor()
            sql = "UPDATE patients SET Reason_for_Admission=%s WHERE Patient_id=%s"
            cur.execute(sql, (phone_no, Roll_no))
            d_obj.commit()
            stud_det(s)
            print("\nUpdate Successful")
        else:
            print("Invalid option")
            
    elif ch==2:
            print("\n")
            print("1. Roll no")
            print("2. Sem 1")
            print("3. Sem 2")
            print("4. Sem 3")
            print("\n")

            option = int(input("\nWhich field do you want to update : "))

            if option == 1:
                Roll_no = input("Enter Roll no:")
                Name = input("Enter new Roll no:")
                cur = d_obj.cursor()
                sql = "UPDATE acad SET Roll_no=%s WHERE Roll_no=%s"
                cur.execute(sql, (Name, Roll_no))
                d_obj.commit()
                stud_acad(s)
                print("\nUpdate Successful")
            elif option == 2:
                current_roll_no = input("Enter Roll no:")
                new_sem_1 = input("Enter new Sem 1 mark:")
                cur = d_obj.cursor()
                sql = "UPDATE acad SET Sem_1=%s WHERE Roll_no=%s"
                cur.execute(sql, (new_sem_1, current_roll_no))
                d_obj.commit()
                stud_acad(s)
                print("\nUpdate Successful")
            elif option == 3:
                current_roll_no = input("Enter Roll no:")
                new_sem_2 = input("Enter new Sem 1 mark:")
                cur = d_obj.cursor()
                sql = "UPDATE acad SET Sem_2=%s WHERE Roll_no=%s"
                cur.execute(sql, (new_sem_2, current_roll_no))
                d_obj.commit()
                stud_acad(s)
                print("\nUpdate Successful")
            elif option == 4:
                current_roll_no = input("Enter Roll no:")
                new_sem_3 = input("Enter new Sem 1 mark:")
                cur = d_obj.cursor()
                sql = "UPDATE acad SET Sem_3=%s WHERE Roll_no=%s"
                cur.execute(sql, (new_sem_3, current_roll_no))
                d_obj.commit()
                stud_acad(s)
                print("\nUpdate Successful")
            else:
                print("Invalid option")
    else:
        print("Invalid ")    

while True:
    print("\n1. Student details ")
    print("2. Academics details ")
    print("3. Insert ")
    print("4. Update")
    print("5. Delete ")
    print("\n")
    s = int(input("Enter the choice: "))
    if s == 1:
        stud_det(s)
    elif s == 2:
        stud_acad(s)
    elif s == 3:
        stud_in(s)
    elif s == 4:
        stud_up(s)
    elif s == 5:
        delete(s)
    else:
        print("\nInvalid")