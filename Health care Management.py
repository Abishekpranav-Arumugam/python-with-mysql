import mysql.connector as m
from tabulate import tabulate

d_obj = m.connect(host='localhost', database='database1', user='root', password='44-abcdef')

def Pat_Det():   # select
    res = d_obj.cursor()
    sql = "SELECT * FROM patients"
    res.execute(sql)
    t_view = res.fetchall()
    print("\n")
    print(tabulate(t_view, headers=["Name", "Patient Id", "Blood Group", "Reason for admission", "Date of admitted", "Date of discharged", "Total Amount"]))

def Doc_Appt():
    print("1. Doctor Appointment")
    print("2. View")
    print("3. Back")
    print("\n")
    opt=int(input("Enter the Field: "))
    print("\n")
    if opt==1:
        res = d_obj.cursor()
        op1 = " 09:00 - 12:00 am"
        op2 = " 01:00 - 04:00 pm"
        op3 = " 05:00 - 08:00 pm"
        Doc_name = input("Enter the Doctor Name: ")
        Specialist = input("Specialist: ")
        print("Timing: \n", op1, "\n", op2, "\n", op3)
        print("\n")
        ch = int(input("Enter the timing to visit the doctor : ")) 

        if ch == 1:
            sql = "INSERT INTO Doc_App (Doc_name, Specialist, Timing) VALUES (%s, %s, %s)"
            res.execute(sql, (Doc_name, Specialist, op1))
            d_obj.commit()
            print("\nAppointment booked successfully")
        elif ch == 2:
            sql = "INSERT INTO Doc_App (Doc_name, Specialist, Timing) VALUES (%s, %s, %s)"
            res.execute(sql, (Doc_name, Specialist, op2))
            d_obj.commit()
            print("\nAppointment booked successfully")
        elif ch == 3:
            sql = "INSERT INTO Doc_App (Doc_name, Specialist, Timing) VALUES (%s, %s, %s)"
            res.execute(sql, (Doc_name, Specialist, op3))
            d_obj.commit()
            print("\nAppointment booked successfully")
        else:
            print("Invalid")
    elif opt==2:
        res = d_obj.cursor()
        sql = "SELECT * FROM Doc_App"
        res.execute(sql)
        t_view = res.fetchall()
        print("\n")
        print(tabulate(t_view, headers=["Doc_name", "Specialist", "Timing"]))
    else:
        print("Invalid")

def delete():
    print("\n")
    print("1. Patient Details")
    print("2. Doctor Appointment")
    print("\n")
    ch=int(input("Enter the field to Delete: "))
    print("\n")
    if ch==1:
        pid = input("Enter Patient ID:")
        res = d_obj.cursor()
        sql = "DELETE FROM patients WHERE patient_id=%s"
        res.execute(sql, (pid,))
        d_obj.commit()
        print("\nRecord Deleted Successfully...!!!")
    else:
        pid = input("Enter Doctor Name:")
        res = d_obj.cursor()
        sql = "DELETE FROM Doc_App WHERE Doc_name=%s"
        res.execute(sql, (pid,))
        d_obj.commit()
        print("\nRecord Deleted Successfully...!!!")
        print("\n")
        sql = "SELECT * FROM Doc_App"
        res.execute(sql)
        t_view = res.fetchall()
        print("\n")
        print(tabulate(t_view, headers=["Doc_name", "Specialist", "Timing"]))
        
def insert():
    print("1. Patient Details")
    print("2. Doctor Appointment")
    print("\n")
    ch=int(input("Enter the field to insert : "))
    print("\n")
    if(ch==1):
        name = input("Enter the  Name: ")
        Patient_id = input("Enter the Patient_id: ")
        Blood_grp = input("Enter the Blood_grp: ")
        Reason_for_Admission = input("Enter the Reason_for_Admission: ") 
        Date_of_admitted = input("Enter the Date_of_Admitted: ") 
        Date_of_discharged = input("Enter the Date_of_discharged: ")
        Total_amount=input("Enter the fee: ")
        try:
            res = d_obj.cursor()
            sql = "INSERT INTO patients (name, Patient_id, Blood_grp, Reason_for_Admission, Date_of_admitted,Date_of_discharged, Total_amount) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            res.execute(sql, (name, Patient_id, Blood_grp, Reason_for_Admission, Date_of_admitted,Date_of_discharged, Total_amount))
            d_obj.commit()
            print("\nRecord Inserted successfully")
        except m.Error as e:
            print(f"Error: {e}")
            
    elif ch == 2:
        print("1. Doctor name")
        print("2. Specialist")
        print("3. Timing")
        try:
            res = d_obj.cursor()
            sql = "INSERT INTO Doc_App (Doc_name, Specialist, Timing) VALUES (%s, %s, %s)"
            res.execute(sql, (Doc_name, Specialist, Timing))
            d_obj.commit()
            print("\nRecord Inserted successfully")
        except m.Error as e:
            print(f"Error: {e}")
        print("\n")
        res = d_obj.cursor()
        sql = "SELECT * FROM Doc_App"
        res.execute(sql)
        t_view = res.fetchall()
        print("\n")
        print(tabulate(t_view, headers=["Doc_name", "Specialist", "Timing"]))
    else:
        print("Invalid")

def update_1():
    print("\n")
    print("1. Update the Patients Details")
    print("2. Update the Doctor Appointment")
    print("\n")
    ch=int(input("Enter the field to be updated: "))
    print("\n")
    if ch==1:
        print("1. Name")
        print("2. Patient ID")
        print("3. Blood Group")
        print("4. Reason for Admission")
        print("5. Date of Admitted")
        print("6. Date of Discharged")
        print("7. Total Amount")

        option = int(input("\nWhich field do you want to update: "))

        if option == 1:
            Patient_id = input("Enter Patient ID:")
            name = input("Enter new Name:")
            cur = d_obj.cursor()
            sql = "UPDATE patients SET name=%s WHERE Patient_id=%s"
            cur.execute(sql, (name, Patient_id))
            d_obj.commit()
            Pat_Det()
            print("\nUpdate Successful")
        elif option == 2:
            current_patient_id = input("Enter current Patient ID:")
            new_patient_id = input("Enter new Patient ID:")
            cur = d_obj.cursor()
            sql = "UPDATE patients SET Patient_id=%s WHERE Patient_id=%s"
            cur.execute(sql, (new_patient_id, current_patient_id))
            d_obj.commit()
            Pat_Det()
            print("\nUpdate Successful")
        elif option == 3:
            Patient_id = input("Enter Patient ID:")
            blood_grp = input("Enter new Blood Group:")
            cur = d_obj.cursor()
            sql = "UPDATE patients SET Blood_group=%s WHERE Patient_id=%s"
            cur.execute(sql, (blood_grp, Patient_id))
            d_obj.commit()
            Pat_Det()
            print("\nUpdate Successful")
        elif option == 4:
            Patient_id = input("Enter Patient ID:")
            reason_for_admission = input("Enter new Reason for Admission:")
            cur = d_obj.cursor()
            sql = "UPDATE patients SET Reason_for_Admission=%s WHERE Patient_id=%s"
            cur.execute(sql, (reason_for_admission, Patient_id))
            d_obj.commit()
            Pat_Det()
            print("\nUpdate Successful")
        elif option == 5:
            Patient_id = input("Enter Patient ID:")
            date_of_admitted = input("Enter new Date of Admitted (YYYY-MM-DD):")
            cur = d_obj.cursor()
            sql = "UPDATE patients SET Date_of_admitted=%s WHERE Patient_id=%s"
            cur.execute(sql, (date_of_admitted, Patient_id))
            d_obj.commit()
            Pat_Det()
            print("\nUpdate Successful")
        elif option == 6:
            Patient_id = input("Enter Patient ID:")
            date_of_discharged = input("Enter new Date of Discharged (YYYY-MM-DD):")
            cur = d_obj.cursor()
            sql = "UPDATE patients SET Date_of_discharged=%s WHERE Patient_id=%s"
            cur.execute(sql, (date_of_discharged, Patient_id))
            d_obj.commit()
            Pat_Det()
            print("\nUpdate Successful")
        elif option == 7:
            Patient_id = input("Enter Patient ID:")
            total_amount = input("Enter new fee:")
            cur = d_obj.cursor()
            sql = "UPDATE patients SET Total_amount=%s WHERE Patient_id=%s"
            cur.execute(sql, (total_amount, Patient_id))
            d_obj.commit()
            Pat_Det()
            print("\nUpdate Successful")
        else:
            print("Invalid option")
    elif ch==2:
        print("1. Doctor name")
        print("2. Specialist")
        print("\n")
        ch=int(input("Enter the field to be updated: "))
        print("\n")
        if ch==1:
            Doc_name = input("Enter Doctor name:")
            name = input("Enter new Name:")
            cur = d_obj.cursor()
            sql = "UPDATE Doc_App SET Doc_name=%s WHERE Doc_name=%s"
            cur.execute(sql, (name, Doc_name))
            d_obj.commit()
            print("\nUpdate Successful")
            print("\n")
            res = d_obj.cursor()
            sql = "SELECT * FROM Doc_App"
            res.execute(sql)
            t_view = res.fetchall()
            print("\n")
            print(tabulate(t_view, headers=["Doc_name", "Specialist", "Timing"]))
        elif ch==2:
            Doc_name = input("Enter Doctor name:")
            Specialist = input("Enter new Specialist:")
            cur = d_obj.cursor()
            sql = "UPDATE Doc_App SET Specialist=%s WHERE Doc_name=%s"
            cur.execute(sql, (Specialist, Doc_name))
            d_obj.commit()
            print("\nUpdate Successful")
            print("\n")
            res = d_obj.cursor()
            sql = "SELECT * FROM Doc_App"
            res.execute(sql)
            t_view = res.fetchall()
            print("\n")
            print(tabulate(t_view, headers=["Doc_name", "Specialist", "Timing"]))
        else:
            print("Invalid")
    else:
        print("Invalid")

while True:
    print("\n1. Patients Details")
    print("2. Doctor Appointment")
    print("3. Insert")
    print("4. Update")
    print("5. Delete")
    print("\n")
    s = int(input("Enter the choice: "))
    if s == 1:
        Pat_Det()
    elif s == 2:
        Doc_Appt()
    elif s==3:
        insert()
    elif s == 4:
        update_1()
    elif s == 5:
        delete()