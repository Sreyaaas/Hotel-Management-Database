#===========================Hotelmanagement system=========================
import random
from tkinter import*
import requests
import webbrowser
# import mysql.connector as con

root=Tk()
root.geometry("660x540")
root.title("LEXUS HOTEL")
root.resizable(width=False, height=False)


          
#================messegeAPI======================

def website():
     webbrowser.open("https://801088.wixsite.com/website")

def sms():
              #message sent after 9pm will be scheduled to be sent at 9am the next day
              url = "https://www.fast2sms.com/dev/bulk"

##              t="Dear customer\nThank you for choosing Lexus Hotel.This sms is to confirm that your booking has been succesfully completed.Glad to welcome you soon\nThankyou:)"

              querystring = {"authorization":"AmY7fJrtTxF52n3sSQMzwE4B8OpkVoPWUebyKX0dRjH9Cl1qZc8n4xqwBrEQWOgTuve3dZNV9DGAsJSL",
               "sender_id":"FSTSMS",
               "message":"Dear customer\nThank you for choosing Lexus Hotel.This sms is to confirm that your booking has been succesfully completed.Glad to welcome you soon\nThankyou:)",
               "language":"english",
               "route":"p",
               "numbers":e3.get()}

              headers = {
              'cache-control': "no-cache"
              }

              response = requests.request("GET", url, headers=headers, params=querystring)

              print(response.text)     

#==================BOOKING================== 

def booking() :
    root=Tk()
    root.geometry("700x500")
    root.title('BOOKING MENU')
    
    root.configure(bg="lavender") 
    
    #=============Label======================
    title=Label(root,text="BOOKING",fg="White",bg="steel blue", font = ("Comic sans MS",30,"bold"))
    title.place(x=240,y=5)
    lb1=Label(root,text="ENTER NAME",fg="Black",bg="lavender")
    lb2=Label(root,text="ENTER ADDRESS",bg="lavender")
    lb3=Label(root,text="ENTER PHONENO",bg="lavender")
    lb4=Label(root,text="ENTER IDP",bg="lavender")
    lb5=Label(root,text="ENTER CHECKIN DATE",bg="lavender")
    lb6=Label(root,text="ENTER NO: OF DAYS",bg="lavender")
    lb7=Label(root,text="SELECT YOUR ROOM",bg="lightblue",fg="snow",font=("arial",16,"bold"))
    a=str(random.randint(100,200))

    

    def roomno():
        b7=Label(root,text=a,bg="lavender",font=("arial",12))
        b7.place(x=260,y=345)
    bt=Button(root,text="ROOM NUMBER :",command=roomno,bd="6",bg="powder blue")
    bt.place(x=67,y=340)
   
    

    lb1.place(x=50,y=90)
    lb2.place(x=50,y=130)
    lb3.place(x=50,y=170)
    lb4.place(x=50,y=210)
    lb5.place(x=50,y=290)
    lb6.place(x=50,y=250)
    lb7.place(x=396,y=90)


         
         
        
    bt=Button(root,text="CONFIRMATION",command=sms,bd="6",bg="powder blue")
    bt.place(x=67,y=380)

    

    #================Entry===================
    global e3
##    global e1
##  global e6
    global ttt
##    ttt=("Good day",e1.get(),"We confirm your reservation at lexus hotel on",e5.get()," has been succesfully completed.Glad to welcome you soon")
    e1=Entry(root,width=30,bd="6",bg="Powder Blue")
    e2=Entry(root,width=30,bd="6",bg="Powder Blue")
    e3=Entry(root,width=30,bd="6",bg="Powder Blue")
    e4=Entry(root,width=30,bd="6",bg="lightblue")
    e5=Entry(root,width=30,bd="6",bg="Powder Blue")
    e6=Entry(root,width=30,bd="6",bg="Powder Blue")
    e1.place(x=180,y=90)
    e2.place(x=180,y=130)
    e3.place(x=180,y=170)
    e4.place(x=180,y=210)
    e5.place(x=180,y=290)
    e6.place(x=180,y=250)
    
    
 #================RoomsLabel=================
          
            
#===============RECORD INSERTION ACCORDING TO ROOM SELECTION=====================


    h="YOUR PAYMENT AMOUNT : 1500"
    def lab1():
##        lb=Label(root,text=h,font="10",bg="lavender")
##        lb.place(x=200,y=380)
        b=1500
        m=e1.get()
        n=e2.get()
        o=e3.get()
        p=e4.get()
        q=e5.get()
        r=e6.get()
        jj=1500*int(r)
        Tamount="YOUR PAYMENT AMOUNT IS :RS"+str(jj)
        lbl=Label(root,text=Tamount,font="10",bg="lavender")
        lbl.place(x=200,y=380)
        import mysql.connector as con
        mycon=con.connect(host='localhost',user='root',password='vishal1234',database='htms')
        mycursor=mycon.cursor()
        qry="INSERT INTO hts(Name,Address,Phone,Idp,Date,Days,Roomno,TotalBill) VALUES('{0}','{1}',{2},{3},{4},{5},{6},{7})".format(m,n,o,p,q,r,int(a),jj)
        mycursor.execute(qry)
        mycon.commit()
        
        
       
    g="YOUR PAYMENT AMOUNT : 2500"
    def lab2():
##        lb2=Label(root,text=g,font="10")
        lb2.place(x=200,y=380)
        c=2500
        m=e1.get()
        n=e2.get()
        o=e3.get()
        p=e4.get()
        q=e5.get()
        r=e6.get()
        jj=2500*int(r)
        Tamount="YOUR PAYMENT AMOUNT IS :RS"+str(jj)
        lbl=Label(root,text=Tamount,font="10",bg="lavender")
        lbl.place(x=220,y=380)
        import mysql.connector as con
        mycon=con.connect(host='localhost',user='root',password='vishal1234',database='htms')
        mycursor=mycon.cursor()
        qry="INSERT INTO hts(Name,Address,Phone,Idp,Date,Days,Roomno,TotalBill) VALUES('{0}','{1}',{2},{3},{4},{5},{6},{7})".format(m,n,o,p,q,r,int(a),jj)
        mycursor.execute(qry)
        mycon.commit()
        jj=2500*int(r)
        
    i="YOUR PAYMENT AMOUNT : 3500"
    def lab3():
##        lb3=Label(root,text=i,font="10")
##        lb3.place(x=200,y=380)
        d=3500
        m=e1.get()
        n=e2.get()
        o=e3.get()
        p=e4.get()
        q=e5.get()
        r=e6.get()
        jj=3500*int(r)
        Tamount="YOUR PAYMENT AMOUNT IS :RS"+str(jj)
        lbl=Label(root,text=Tamount,font="10",bg="lavender")
        lbl.place(x=200,y=380)
        import mysql.connector as con
        mycon=con.connect(host='localhost',user='root',password='vishal1234',database='htms')
        mycursor=mycon.cursor()
        qry="INSERT INTO hts(Name,Address,Phone,Idp,Date,Days,Roomno,TotalBill) VALUES('{0}','{1}',{2},{3},{4},{5},{6},{7})".format(m,n,o,p,q,r,int(a),jj)
        mycursor.execute(qry)
        mycon.commit()
        jj=3500*int(r)
        
        
    l="YOUR PAYMENT AMOUNT : 4500"
    def lab4():
##        lb4=Label(root,text=l,font="10")
##        lb4.place(x=200,y=380)
        e=4500
        m=e1.get()
        n=e2.get()
        o=e3.get()
        p=e4.get()
        q=e5.get()
        r=e6.get()
        jj=4500*int(r)
        Tamount="YOUR PAYMENT AMOUNT IS :RS"+str(jj)
        lbl=Label(root,text=Tamount,font="10",bg="lavender")
        lbl.place(x=200,y=380)
        import mysql.connector as con
        mycon=con.connect(host='localhost',user='root',password='vishal1234',database='htms')
        mycursor=mycon.cursor()
        qry="INSERT INTO hts(Name,Address,Phone,Idp,Date,Days,Roomno,TotalBill) VALUES('{0}','{1}',{2},{3},{4},{5},{6},{7})".format(m,n,o,p,q,r,int(a),jj)
        mycursor.execute(qry)
        mycon.commit()
        jj=4500*int(r)
        
       

    #============================RoomsButtons=============================
    b1=Button(root,text="STANDARD NON AC ",bd="9",padx="10",pady="6",fg="Black",bg="powder blue",command=lab1)
    b2=Button(root,text="STANDARD  -  AC ",padx="18",pady="6",bd="9",fg="Black",bg="powder blue",command=lab2) 
    b3=Button(root,text="DELUXE SINGLE BED ",bd="9",padx="11",pady="6",fg="Black",bg="powder blue",command=lab3)
    b4=Button(root,text="DELUXE DOUBLE BED ",bd="9",padx="8",pady="6",fg="Black",bg="powder blue",command=lab4)
    b1.place(x=435,y=125)
    b2.place(x=435,y=175)
    b3.place(x=435,y=225)
    b4.place(x=435,y=275)

#NO USE JUST IGNORE
    def get():
        m=e1.get()
        n=e2.get()
        o=e3.get()
        p=e4.get()
        q=e5.get()
        r=e6.get()
        import mysql.connector as con
        mycon=con.connect(host='localhost',user='root',password='vishal1234',database='htms')
        mycursor=mycon.cursor()
        qry="INSERT INTO hts(Name,Address,Phone,Idp,Date,Days,Roomno) VALUES('{0}','{1}',{2},{3},{4},{5},{6})".format(m,n,o,p,q,r,int(a))
        mycursor.execute(qry)
        mycon.commit()
    

    


#===================GUEST FUNCTION========================

def guest():
    root=Tk()
    root.geometry("350x400")
    root.configure(bg="plum2")
    root.title('guests')

#SEARCHING A PARTICULAR RECORD    

    def search():
        root=Tk()
        root.geometry("900x450")
        root.configure(bg="ghostwhite")
        lb2=Label(root,text="SEARCH",bg="ghostwhite",font=("Cosmic Sans MS", 30,"bold"))
        lb2.place(x=347,y=50)
        lb1=Label(root,text="ENTER NAME",bg="ghostwhite",font=("Corbel", 14,"bold"))
        lb1.place(x=200,y=150)
        e1=Entry(root,width=25,bd="6",bg="ghostwhite")
        e1.place(x=340,y=150)
        
        
        def gt():
            
            import mysql.connector as con
            mycon=con.connect(host='localhost',user="root",password="vishal1234",database="htms")
            mycursor=mycon.cursor()
            x=e1.get()
            qry="SELECT * FROM hts WHERE Name='{}'".format(x)
            mycursor.execute(qry)
            m=mycursor.fetchone()
            lbn=Label(root,text="NAME   : "+e1.get())
            lbr=Label(root,text="TOTAL BILL AMOUNT :    ")

            c=len(m)
            h=120
            for i in range(0,c) :
                        l=Label(root,text=m[i],bg="lightblue",pady="8",width=9)
                        l.place(x=h,y=240)
                        h+=73
            lab=Label(root,text="TOTAL BILL AMOUNT ")
            lname=Label(root,text="NAME",width="5",pady="8",padx="15",bg="white")
            ladd=Label(root,text="ADDRESS",width="9",pady="8",bg="white")
            lphno=Label(root,text="PHONE",width="9",pady="8",bg="white")
            lidp=Label(root,text="IDP",width="9",pady="8",bg="white")
            ldate=Label(root,text="DATE",width="9",pady="8",bg="white")
            lroom=Label(root,text="DAYS",width="9",pady="8",bg="white")
            ltt=Label(root,text="TOTAL BILL",width="9",pady="8",bg="white")
            lda=Label(root,text="ROOMNO",width="7",pady="8",padx="7",bg="white")
            lrst=Label(root,text="RESTAURANT",width="9",pady="8",padx="7",bg="white")
            lname.place(x=120,y=200)
            ladd.place(x=192,y=200)
            lphno.place(x=266,y=200)
            lidp.place(x=340,y=200)
            ldate.place(x=412,y=200)
            lroom.place(x=557,y=200)
            ltt.place(x=630,y=200)
            lda.place(x=486,y=200)
            lrst.place(x=704,y=200)
        bt=Button(root,text="SUBMIT",command= gt,bd="6")
        bt.place(x=520,y=146)
            
        
        

#================================VIEW ALL GUEST DETAILS============================

    def guest_info():
        root=Tk()
        root.geometry("920x500")
        root.configure(bg="azure")
        ltitle=Label(root,text="GUEST DETAILS",bg="coral",fg="burlywood1",font=("arial",30,"bold") )
        ltitle.place(x=300,y=30)

        import mysql.connector as con
        mycon=con.connect(host="localhost",user="root",password="vishal1234",database="htms")
        mycursor=mycon.cursor()
        mycursor.execute("select * from hts")
        m=mycursor.fetchall()
        #l7=Label(root,text=m)
        # l7.place(x=120,y=200)
        z=127
        lname=Label(root,text="NAME",width="10",pady="8")
        ladd=Label(root,text="ADDRESS",width="10",pady="8")
        lphno=Label(root,text="PHONE",width="10",pady="8")
        lidp=Label(root,text="IDP",width="10",pady="8")
        ldate=Label(root,text="DATE",width="10",pady="8")
        lroom=Label(root,text="DAYS",width="10",pady="8")
        ltt=Label(root,text="TOTAL BILL",width="10",pady="8")
        lda=Label(root,text="ROOMNO",width="10",pady="8")
        lrst=Label(root,text="RESTAURANT",width="10",pady="8",padx="7")
        lrst.place(x=745,y=90)
        lname.place(x=120,y=90)
        ladd.place(x=199,y=90)
        lphno.place(x=277,y=90)
        lidp.place(x=354,y=90)
        ldate.place(x=432.5,y=90)
        lroom.place(x=511,y=90)
        ltt.place(x=667,y=90)
        lda.place(x=589.5,y=90)
        
        
        
        for w in m :
            l9=Label(root,text=w[0],pady="8",width="10",bg="khaki1",)
            l9.place(x=120,y=z)
            l10=Label(root,text=w[1],pady="8",width="10",bg="tan1")
            l10.place(x=197.5,y=z)
            l11=Label(root,text=w[2],pady="8",width="10",bg="Skyblue3")
            l11.place(x=276,y=z)
            l12=Label(root,text=w[3],pady="8",width="10",bg="Salmon")
            l12.place(x=353.5,y=z)
            l13=Label(root,text=w[4],pady="8",width="10",bg="plum2")
            l14=Label(root,text=w[5],pady="8",width="10",bg="DarkOliveGreen1")
            l15=Label(root,text=w[6],pady="8",width="10",bg="hot pink")
            l16=Label(root,text=w[7],pady="8",width="10",bg="light blue")
            l17=Label(root,text=w[8],pady="8",width="10",bg="mediumpurple")
            l13.place(x=432.,y=z)
            l14.place(x=509.5,y=z)
            l15.place(x=589,y=z)
            l16.place(x=667,y=z)
            l17.place(x=745,y=z)
            
            z+=37
    bt=Button(root,text="SEARCH",command=search,bd="6",pady="13",padx="21",width="18",bg="hot pink")
    bt1=Button(root,text="GUESTS DETAILS",command=guest_info,bd="6",pady="13",padx="21",width="18",bg="hot pink")
    bt.place(x=80,y=120)
    bt1.place(x=80,y=200)
                    
        
    
    
    root.mainloop()
    
    
#NO USE JUST IGNORE  

def rooms_available():
    root=Tk()
    root.title('rooms available')
    import mysql.connector as con
    mycon=con.connect(host='localhost',user="root",password="vishal1234",database="htms")
    mycursor=mycon.cursor()
    mycursor.execute("select*from hts")
    x=mycursor.fetchall()
    l=[101,102,103,104,105,106,107,108,109,110]
    if l in x:
        pass
    else:
        label=Label(root,text=l)
        mycon.close()

#CANCELLATION POLICY

def cancel():
         root=Tk()
         root.title("cancellation policy[important]")
         lll=Label(root,text="Our Policy:\nAny cancellation or reschedule made less than [Time Period] will result in a cancellation fee.\n The amount of the fee will be equal to [Percentage] of the reserved services or [Amount], whichever is more.If you are more than [Time Period] late for your service, we may not be able to accommodate you\n. In this case, the same cancellation fee will apply\n. We will do our very best to reschedule your service for another time that is convenient to you\n.We require a credit card to hold your appointment\n. Cancellation fees will be charged to your card on file.In the event of a true, unavoidable emergency, all or part of your cancellation fee may be applied to future services.",font="Corbel 10 bold")
         lll.pack()
         bt=Button(root,text="CANCELLATION POLICY",command=cancel,bd="7",bg='skyblue',fg='black')
         bt.place(x=200,y=186)
#============================CANCELLATION===============================
         
def checkout():
    root=Tk()
    root.geometry("650x500")
    root.title('CANCELLATION PAGE')
    root.configure(bg='Floral white')
    ltitle=Label(root,text="CANCELLATION PAGE",bg="steel blue",fg="thistle",font=("arial", 28,"bold"))
    ltitle.place(x=140,y=30)
    bt=Button(root,text="CANCELLATION POLICY",command=cancel,bd="6",bg='skyblue')
    bt.place(x=250,y=186)

    lb1=Label(root,text="ENTER NAME",bg="floral white",font=("Corbel", 14,"bold"))
    lb1.place(x=100,y=150)
    e1=Entry(root,width=25,bd="6")
    e1.place(x=240,y=150)
    x=e1.get() 
    
    
    
#DELETING A RECORD    
    def get():
        import mysql.connector as con
        mycon=con.connect(host='localhost',user="root",password="vishal1234",database="htms")
        mycursor=mycon.cursor(buffered=True)        

        x=e1.get()
        qry="DELETE FROM hts WHERE Name='{}'".format(x)
        mycursor.execute(qry)
        mycon.commit()
        lbr=Label(root,text="YOUR BOOKING HAS BEEN CANCELED !",font=("arial",16,"bold"))
        lbr.place(x=200,y=250)
    bt=Button(root,text="CHECKOUT",command= get,bd="6",bg='skyblue',fg='red')
    bt.place(x=420,y=146)

#=======================================RESTAURANT GUI================================================

def rest():
    root=Tk()
    root.geometry("600x600")
    root.title('restaurant')
    root.configure(bg="lightblue")
    ltitle=Label(root,text="RESTAURANT BILL ",width="19",padx="7",font=("Noir", 20,"bold"),bg="azure",fg="black")
    ltitle.place(x=140,y=10)
  
    def sl():       
            if clickedsl.get()=="4":
                et3=Entry(root,bd=6,width=15)
                et3.place(x=100,y=267)
                e2=Entry(root,bd=6,width=10)
                e4=Entry(root,bd=6,width=10)
                e5=Entry(root,bd=6,width=10)
                e4.place(x=355,y=267)
                e5.place(x=280,y=267)
                e2.place(x=205,y=267)
            elif clickedsl.get()=="5":
                et3=Entry(root,bd=6,width=15)
                et3.place(x=100,y=267)
                e2=Entry(root,bd=6,width=10)
                e4=Entry(root,bd=6,width=10)
                e5=Entry(root,bd=6,width=10)
                e4.place(x=355,y=267)
                e5.place(x=280,y=267)
                e2.place(x=205,y=267)
            elif clickedsl.get()=="6":
                et3=Entry(root,bd=6,width=15)
                et3.place(x=100,y=325)
                e2=Entry(root,bd=6,width=10)
                e4=Entry(root,bd=6,width=10)
                e5=Entry(root,bd=6,width=10)
                e4.place(x=355,y=325)
                e5.place(x=280,y=325)
                e2.place(x=205,y=325)



    clicked2=StringVar()
    clicked2.set("QTY")
    drop2=OptionMenu(root,clicked2,"1","2","3","4","5","6","7","8","9","10")
    drop2.place(x=900,y=180)
    clicked3=StringVar()
    clicked3.set("QTY")
    drop3=OptionMenu(root,clicked3,"1","2","3","4","5","6","7","8","9","10")
    drop3.place(x=900,y=180)

    lbs=Label(root,text="SELECT FOOD ITEMS ",bg='skyblue',font=("time", 10,"bold"))
    lb2=Label(root,text="ENTER ROOM NO: ",bg='skyblue',font=("time", 10,"bold"))
    e=Entry(root,width=20)

    lb3=Label(root,text="ITEM NAME",font=("time", 10,"bold"),bg="lightblue")
    lb4=Label(root,text="RATE",font=("time", 10,"bold"),bg="lightblue")
    lb5=Label(root,text="QTY",font=("time", 10,"bold"),bg="lightblue")
    lb6=Label(root,text="AMOUNT",font=("time", 10,"bold"),bg="lightblue")
    lb7=Label(root,text="BILLED BY : VISHAL",font=("time", 10,"bold"),bg="lightblue")
    lb8=Label(root,text="ROOM NO :",font=("time", 11,"bold"),bg="lightblue")
    lb9=Label(root,text="DATE  ",font=("time", 10,"bold"),bg="lightblue")
    lbl1=Label(root,text="SUB TOTAL",font=("time", 10,"bold"),bg="lightblue")
    lbl2=Label(root,text="CGST 9%",font=("time", 10,"bold"),bg="lightblue")
    lbl3=Label(root,text="SGST 9%",font=("time", 10,"bold"),bg="lightblue")
    lbl4=Label(root,text="TOTAL AMOUNT",font=("time", 10,"bold"),bg="lightblue")
    clicked=StringVar()
    clicked.set("FOOD")
    drop=OptionMenu(root,clicked,"PIZZA    350","VEG BURGER  80 ","CHICKEN BURGER  120","SHAWARMA  90","CHICKEN BIRIYANI  130","BEEF BIRIYANI  150","MUTTON BIRYANI  140","FRIED RICE  120","BROASTED CHICKEN  90","MEALS  80","DOSA  60","CHAPPATHI  15","VEG-FRIED RICE  100","NOODLES 200","PORROTA 18","AL FAHAM 360")
    drop.place(x=500,y=180)

    lb3.place(x=110,y=160)
    lb4.place(x=220,y=160)
    lb5.place(x=300,y=160)
    lb6.place(x=363,y=160)

    e1=Entry(root,bd=6,width=15,bg="lavender")
    e2=Entry(root,bd=6,width=10,bg="lavender")
    e3=Entry(root,bd=6,width=10,bg="lavender")
    e4=Entry(root,bd=6,width=10,bg="lavender")
    e5=Entry(root,bd=6,width=10,bg="lavender")
    e6=Entry(root,bd=6,width=15,bg="lavender")
    e7=Entry(root,bd=6,width=10,bg="lavender")
    e8=Entry(root,bd=6,width=10,bg="lavender")
    e9=Entry(root,bd=6,width=15,bg="lavender")
    et=Entry(root,bd=6,width=10,bg="lavender")
    et1=Entry(root,bd=6,width=10,bg="lavender")
    et2=Entry(root,bd=6,width=10,bg="lavender")
    et3=Entry(root,bd=6,width=15,bg="lavender")
    et4=Entry(root,bd=6,width=15,bg="lavender")
    et5=Entry(root,bd=6,width=15,bg="lavender")

    e1.place(x=100,y=180)
    e2.place(x=205,y=180)
    e3.place(x=280,y=180)
    e4.place(x=355,y=180)
    e5.place(x=355,y=209)
    e6.place(x=100,y=209)
    e7.place(x=205,y=209)
    e8.place(x=280,y=209)
    e9.place(x=100,y=238)
    et.place(x=205,y=238)
    et1.place(x=280,y=238)
    et2.place(x=355,y=238)
    er=Entry(root,width=10,bd=4,bg="lavender")
    er.place(x=200,y=111)

    lb7.place(x=100,y=85)
    lb8.place(x=100,y=110)


#BILL CALCULATION AND UPDATING BILL AMOUNT IN THE TABLE

    def sumt():
        v=er.get()
        f=int(e4.get())
        g=int(e5.get())
        h=int(et2.get())
        tot=f+g+h
        tst=22.0+tot
        lbs=Label(root,text=tot,font=("arial",10,"bold"))
        lbs.place(x=380,y=280)
        lb1=Label(root,text="SUB TOTAL  :",font=("arial",10,"bold"),)
        lb1.place(x=270,y=280)
        lbl2=Label(root,text="CGST 9%                     :   12.0",font=("arial", 10,"bold"),bg="lightblue")
        lbl3=Label(root,text="SGST 9%                     :   10.0",font=("arial", 10,"bold"),bg="lightblue")
        lbl4=Label(root,text="TOTAL  AMOUNT         :",font=("arial", 10,"bold"),bg="lightblue")
        lb5=Label(root,text=tst,font=("arial", 10,"bold"),)
        lb5.place(x=400,y=460)

        lbl2.place(x=250,y=400)
        lbl3.place(x=250,y=430)
        lbl4.place(x=250,y=460)
        import mysql.connector as con
        mycon=con.connect(host='localhost',user="root",password="vishal1234",database="htms")
        mycursor=mycon.cursor()
        qry="UPDATE hts SET Rest={0} WHERE Roomno={1}".format(tst,v)
        mycursor.execute(qry)
        mycon.commit()
    btt=Button(root,text="SUBMIT",command=sumt)
    btt.place(x=490,y=240)


   
    

#================================menu======================================================
    
label1=Button(root,text="1. BOOKING",pady=15,command=booking,padx=70,bd=6,bg="skyblue",font=("arial",11,"bold"))
label2=Button(root,text="2. CANCELLATION",pady=15,command=checkout,padx=47,bd=6,bg="skyblue",font=("arial",11,"bold"))
label3=Button(root,text="3. GUEST INFO",pady=15,command=guest,padx=62,bd=6,bg="skyblue",font=("arial",11,"bold"))
label4=Button(root,text="4. RESTAURANT ",command=rest,pady=15,padx=54,bd=6,bg="skyblue",font=("arial",11,"bold"))
label5=Button(root,text="5. WEBSITE",command=website,pady=15,padx=54,bd=6,bg="skyblue",font=("arial",11,"bold"))
label6=Label(root,text="LEXUS HOTEL",width=25,font=("Comic sans MS",24,"bold"),)

#============================button position=================================================

label1.place(x=70,y=290)
label2.place(x=370,y=290)
label3.place(x=70,y=380)
label4.place(x=368,y=380)
label5.place(x=240,y=460)
label6.place(x=100,y=240)


#IMAGE
from PIL import ImageTk,Image
img = Image.open("C:\\Users\\Home\\Videos\\sreyas and vishal\\hoteli.jpeg")     
riz=img.resize((300,200),Image.ANTIALIAS)
np=ImageTk.PhotoImage(riz)
lab=Label(root,image=np)
lab.place(x=190,y=20)
root.mainloop()
