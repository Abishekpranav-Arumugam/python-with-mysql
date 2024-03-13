import mysql.connector as m
from tabulate import tabulate

d_obj = m.connect(host='localhost', database='database3', user='root', password='44-abcdef')

def All_det():
    print("\n")
    print("Faculty Personal Details")
    res = d_obj.cursor()
    sql = "SELECT * FROM faculty_p"
    res.execute(sql)
    t_view = res.fetchall()
    print("\n")
    print(tabulate(t_view, headers=["Name of the Faculty ","Gender ", "Year of Joining", "Experience in (Years) ", "Research Scholar ", "Address"]))
    
    print("\n")
    print("Faculty Academic Details")
    res = d_obj.cursor()
    sql = "SELECT * FROM faculty_a"
    res.execute(sql)
    t_view = res.fetchall()
    print("\n")
    print(tabulate(t_view, headers=["Name of the Faculty","Department", "Domain", "Training started","Training Ended","Training Period","Company Name","Company Sector","Type of Training","Workshop Attended"]))
    print("\n")
    
    print("\n")
    print("Faculty Publication Details")
    res = d_obj.cursor()
    sql = "SELECT * FROM faculty_pub"
    res.execute(sql)
    t_view = res.fetchall()
    print("\n")
    print(tabulate(t_view, headers=["Name of the Faculty ","Paper Published", "Journal Published", "Book Published ", "Conference Attended ", "Project Published"]))
    print("\n")
    
def fac_det():
    res = d_obj.cursor()
    sql = "SELECT * FROM faculty_p"
    res.execute(sql)
    t_view = res.fetchall()
    print("\n")
    print(tabulate(t_view, headers=["Name of the Faculty ","Gender ", "Year of Joining", "Experience in (Years) ", "Research Scholar ", "Address"]))
    print("\n")
    print("1. View all")
    print("2. Back")
    print("\n")
    option=int(input("Enter the choice :"))
    if(option==1):
        All_det()
    elif(option>=3):
        print("\nInvalid Input.")
    else:
        pass

def fac_acad():
    res = d_obj.cursor()
    sql = "SELECT * FROM faculty_a"
    res.execute(sql)
    t_view = res.fetchall()
    print("\n")
    print(tabulate(t_view, headers=["Name of the Faculty","Department", "Domain", "Training started","Training Ended","Training Period","Company Name","Company Sector","Type of Training","Workshop Attended"]))
    print("\n")
    print("1. View all")
    print("2. Back")
    print("\n")
    option=int(input("Enter the choice :"))
    if(option==1):
        All_det()
    elif(option>=3):
        print("\nInvalid Input.")
    else:
        pass

def fac_pub():
    res = d_obj.cursor()
    sql = "SELECT * FROM faculty_pub"
    res.execute(sql)
    t_view = res.fetchall()
    print("\n")
    print(tabulate(t_view, headers=["Name of the Faculty ","Paper Published", "Journal Published", "Book Published ", "Conference Attended ", "Project Published"]))
    print("\n")
    print("1. View all")
    print("2. Back")
    print("\n")
    option=int(input("Enter the choice :"))
    if(option==1):
        All_det()
    elif(option>=3):
        print("\nInvalid Input.")
    else:
        pass
        


def insert():
    print("1. Insert Personal Details.")
    print("2. Insert Academic Details.")
    print("3. Insert Publications.")
    print("\n")
    option=int(input("Which field do you want to insert: "))
    if(option==1):
        name = input("Enter the Faculty Name: ")
        gender = input("Enter the Gender: ")
        year_of_joining = input("Enter the Year of join: ")
        exp_in_years = input("Enter the experience(in years):")
        research_scholar = input("Enter your degree: ")
        address = input("Enter your address : ")
        ph_no= input("Enter your mobile number : ")
        res = d_obj.cursor()
        sql = "INSERT INTO faculty_p (name, gender, year_of_joining, exp_in_years, research_scholar,address) VALUES (%s, %s, %s, %s, %s, %s)"
        res.execute(sql, (name, gender, year_of_joining, exp_in_years, research_scholar,address))
        d_obj.commit()
        print("\nRecord Inserted successfully")

    elif(option==2):
        name = input("Enter the Faculty Name: ")
        dep = input("Enter the Department: ")
        area_o_spec = input("Enter area of specialisation: ")
        Tra_st = input("Enter training start date:")
        Tra_en = input("Enter training end date: ")
        Tra_per = input("Enter total number of training days: ")
        company_na= input("Enter company/industry name: ")
        company_se= input("Enter type of sector: ")
        ty_of_train= input("Enter type of training undergone:")
        wor_att= input("Enter number of workshop attended: ")
        res = d_obj.cursor()
        sql = "INSERT INTO faculty_a (name, dep, area_o_spec, Tra_st, Tra_en,Tra_per,company_na,company_se,ty_of_train,wor_att) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        res.execute(sql, (name, dep, area_o_spec, Tra_st, Tra_en,Tra_per,company_na,company_se,ty_of_train,wor_att))
        d_obj.commit()
        print("\nRecord Inserted successfully")

    elif(option==3):
        name = input("Enter the Faculty Name: ")
        pap_pub = input("Enter the Paper Publications: ")
        jur_pub = input("Enter the Journal Publications: ")
        book_pub = input("Enter the Book Publications: ")
        conf_att = input("Enter Conference Attended: ")
        pro_pub = input("Enter Project Publications: ")
        res = d_obj.cursor()
        sql = "INSERT INTO faculty_pub (name, pap_pub,jur_pub, book_pub, conf_att, pro_pub) VALUES (%s, %s, %s, %s, %s, %s)"
        res.execute(sql, (name, pap_pub,jur_pub, book_pub, conf_att, pro_pub))
        d_obj.commit()
        print("\nRecord Inserted successfully")
        
    else:
        print("Invalid Input.")

def delete():
    print("1. Faculty Personl Details")
    print("2. Faculty Academic Details")
    print("3. Faculty Publications Details")
    print("\n")
    option=int(input("Which field do you want to delete :"))
    if(option==1):
        name = input("Enter Faculty name:")
        res = d_obj.cursor() 
        sql = "DELETE FROM faculty_p WHERE name=%s"
        res.execute(sql, (name,))
        d_obj.commit()
        fac_det()
        print("\nRecord Deleted Successfully...!!!")
        print("\n")
        
    elif(option==2):
        name = input("Enter Faculty name:")
        res = d_obj.cursor() 
        sql = "DELETE FROM faculty_a WHERE name=%s"
        res.execute(sql, (name,))
        d_obj.commit()
        fac_acad()
        print("\nRecord Deleted Successfully...!!!")
        print("\n")
        
    elif(option==3):
        name = input("Enter Faculty name:")
        res = d_obj.cursor() 
        sql = "DELETE FROM faculty_pub WHERE name=%s"
        res.execute(sql, (name,))
        d_obj.commit()
        fac_pub()
        print("\nRecord Deleted Successfully...!!!")
        print("\n")
        
    else:
        print("Invalid Input.")

def update():
    print("1. Update Faculty Personal Details.")
    print("2. Update Academic Details.")
    print("3. Update Publications.")
    print("\n ")
    option=int(input("Which field do you want to update: "))
    
    if(option==1):
        print("1. Name of the Faculty")
        print("2. Gender ")
        print("3. Year of Joining")
        print("4. Experience in (Years) ")
        print("5. Research Scholar ")
        print("6. Address")

        option = int(input("\nWhich field do you want to update: "))

        if option == 1:
            cur_name = input("Enter Faculty Name:")
            new_name = input("Enter new Name:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_p SET name=%s WHERE name=%s"
            cur.execute(sql, (new_name, cur_name))
            d_obj.commit()
            fac_det()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 2:
            name = input("Enter the Name:")
            gender = input("Enter the Gender:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_p SET gender=%s WHERE name=%s"
            cur.execute(sql, (gender, name))
            d_obj.commit()
            fac_det()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 3:
            name = input("Enter Faculty Name:")
            year_of_joining = input("Enter Year of Joining:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_p SET year_of_joining=%s WHERE name=%s"
            cur.execute(sql, (year_of_joining, name))
            d_obj.commit()
            fac_det()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 4:
            name = input("Enter Faculty Name:")
            exp_in_years = input("Enter Years in Experience:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_p SET exp_in_years=%s WHERE name=%s"
            cur.execute(sql, (exp_in_years, name))
            d_obj.commit()
            fac_det()
            print("\nUpdate Successful")
            print("\n")
            
        elif option ==5:
            name = input("Enter Faculty Name:")
            address = input("Enter the Address:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_p SET address=%s WHERE name=%s"
            cur.execute(sql,(address, name))
            d_obj.commit()
            fac_det()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 6:
            name = input("Enter the Faculty Name:")
            ph_no = input("Enter the Phone no:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_p SET ph_no=%s WHERE name=%s"
            cur.execute(sql, (ph_no, name))
            d_obj.commit()
            fac_det()
            print("\nUpdate Successful")
            print("\n")
        else:
            print("Invalid option")
            print("\n")

    if(option==2):
        print("1. Name of the Faculty")
        print("2. Department ")
        print("3. Area of Specialisation")
        print("4. Training Started ")
        print("5. Training Ended")
        print("6. Training Period")
        print("7. Company Name")
        print("8. Company Sector")
        print("9. Type of Training")
        print("10. Workshop Attended")

        option = int(input("\nWhich field do you want to update: "))

        if option == 1:
            cur_name = input("Enter Faculty Name:")
            new_name = input("Enter new Faculty Name:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET name=%s WHERE name=%s"
            cur.execute(sql, (new_name, cur_name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 2:
            name = input("Enter the Faculty Name:")
            dep = input("Enter the Department:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET dep=%s WHERE name=%s"
            cur.execute(sql, (dep, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 3:
            name = input("Enter Faculty Name:")
            area_o_spec = input("Enter the Area of Specialisation:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET area_o_spec=%s WHERE name=%s"
            cur.execute(sql, (area_o_spec, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 4:
            name = input("Enter Faculty Name:")
            Tra_st = input("Enter the Training Started:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET Tra_st=%s WHERE name=%s"
            cur.execute(sql, (Tra_st, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 5:
            name = input("Enter Faculty Name:")
            Tra_en= input("Enter the Training Ended:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET Tra_en=%s WHERE name=%s"
            cur.execute(sql,(Tra_en, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 6:
            name = input("Enter the Faculty Name:")
            Tra_per = input("Enter the Training Period:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET Tra_per=%s WHERE name=%s"
            cur.execute(sql, (Tra_per, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 7:
            name = input("Enter the Faculty Name:")
            company_na = input("Enter the Company Name:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET company_na=%s WHERE name=%s"
            cur.execute(sql, (company_na, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 8:
            name = input("Enter the Faculty Name:")
            company_se = input("Enter the Company Sector:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET company_se=%s WHERE name=%s"
            cur.execute(sql, (company_se, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 9:
            name = input("Enter the Faculty Name:")
            ty_of_train = input("Enter the Type of Training:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET ty_of_train=%s WHERE name=%s"
            cur.execute(sql, (ty_of_train, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 10:
            name = input("Enter the Faculty Name:")
            wor_att = input("Enter the Workshop Attended:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_a SET wor_att=%s WHERE name=%s"
            cur.execute(sql, (wor_att, name))
            d_obj.commit()
            fac_acad()
            print("\nUpdate Successful")
            print("\n")
            
        else:
            print("Invalid option")
            print("\n")
    
    if(option==3):
        print("1. Name of the Faculty")
        print("2. Paper Publications ")
        print("3. Journals Published")
        print("4. Book Published")
        print("5. Conference Attended ")
        print("6. Project Publications")

        option = int(input("\nWhich field do you want to update: "))

        if option == 1:
            cur_name = input("Enter Faculty Name:")
            new_name = input("Enter new Faculty Name:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_pub SET name=%s WHERE name=%s"
            cur.execute(sql, (new_name, cur_name))
            d_obj.commit()
            fac_pub()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 2:
            name = input("Enter the Name:")
            pap_pub = input("Enter the Paper Published:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_pub SET pap_pub=%s WHERE name=%s"
            cur.execute(sql, (pap_pub, name))
            d_obj.commit()
            fac_pub()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 3:
            name = input("Enter Faculty Name:")
            jur_pub = input("Enter Journal Published:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_pub SET jur_pub=%s WHERE name=%s"
            cur.execute(sql, (jur_pub, name))
            d_obj.commit()
            fac_pub()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 4:
            name = input("Enter Faculty Name:")
            book_pub = input("Enter the Book Published:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_pub SET book_pub=%s WHERE name=%s"
            cur.execute(sql, (book_pub, name))
            d_obj.commit()
            fac_pub()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 5:
            name = input("Enter Faculty Name:")
            conf_att = input("Enter the Conference Attended:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_pub SET conf_att=%s WHERE name=%s"
            cur.execute(sql,(conf_att, name))
            d_obj.commit()
            fac_pub()
            print("\nUpdate Successful")
            print("\n")
            
        elif option == 6:
            name = input("Enter the Faculty Name:")
            pro_pub = input("Enter the Project Published:")
            cur = d_obj.cursor()
            sql = "UPDATE faculty_pub SET pro_pub=%s WHERE name=%s"
            cur.execute(sql, (pro_pub, name))
            d_obj.commit()
            fac_pub()
            print("\nUpdate Successful")
            print("\n")
            
        else:
            print("Invalid option")
            print("\n")
            
    else:
        print("\nInvalid Input.")


while True:
    print(" \n ")
    print("1. Faculty Personal Details.")
    print("2. Faculty Academic Details.")
    print("3. Faculty Publications.")
    print("4. Update.")
    print("5. Insert.")
    print("6. Delete.")
    print("\n")
    s = int(input("Enter the choice: "))
    if s == 1:
        fac_det()
    elif s == 2:
        fac_acad()
    elif s == 3:
        fac_pub()
    elif s == 4:
        update()
    elif s == 5:
        insert()
    elif s == 6:
        delete()
    else:
        print("Invalid Input.")
        