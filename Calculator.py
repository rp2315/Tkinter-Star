from tkinter import *
#import tkMessageBox

class calculator:

        count=0
        flag=0
        n1=0
        n2=0
        ans=0
        temp=""
        
        
        def __init__(self):
                top = Tk()
                top.title('Calculator')
                top.geometry("375x390")

                self.e1 = Entry(top,font=("cambria",12))
                self.e1.place(x="20",y="20",width="335",height="40")

                self.b1=Button(top,text="MC",command=lambda:self.put(1))
                self.b1.place(x="25",y="70",width="60",height="40")

                self.b2=Button(top,text="MR",command=lambda:self.put(2))
                self.b2.place(x="90",y="70",width="60",height="40")

                self.b3=Button(top,text="MS",command=lambda:self.put(3))
                self.b3.place(x="155",y="70",width="60",height="40")

                self.b4=Button(top,text="M+",command=lambda:self.put(4))
                self.b4.place(x="220",y="70",width="60",height="40")

                self.b5=Button(top,text="M-",command=lambda:self.put(5))
                self.b5.place(x="285",y="70",width="60",height="40")

                self.b6=Button(top,text="←",command=lambda:self.put(6))
                self.b6.place(x="25",y="120",width="60",height="40")

                self.b7=Button(top,text="CE",command=lambda:self.put(7))
                self.b7.place(x="90",y="120",width="60",height="40")

                self.b8=Button(top,text="C",command=lambda:self.put(8))
                self.b8.place(x="155",y="120",width="60",height="40")

                self.b9=Button(top,text="±",command=lambda:self.put(9))
                self.b9.place(x="220",y="120",width="60",height="40")

                self.b10=Button(top,text="√ ",command=lambda:self.put(10))
                self.b10.place(x="285",y="120",width="60",height="40")

                self.b11=Button(top,text="7",command=lambda:self.put(11))
                self.b11.place(x="25",y="170",width="60",height="40")

                self.b12=Button(top,text="8",command=lambda:self.put(12))
                self.b12.place(x="90",y="170",width="60",height="40")

                self.b13=Button(top,text="9",command=lambda:self.put(13))
                self.b13.place(x="155",y="170",width="60",height="40")

                self.b14=Button(top,text="/",command=lambda:self.put(14))
                self.b14.place(x="220",y="170",width="60",height="40")

                self.b15=Button(top,text="%",command=lambda:self.put(15))
                self.b15.place(x="285",y="170",width="60",height="40")

                self.b16=Button(top,text="4",command=lambda:self.put(16))
                self.b16.place(x="25",y="220",width="60",height="40")

                self.b17=Button(top,text="5",command=lambda:self.put(17))
                self.b17.place(x="90",y="220",width="60",height="40")

                self.b18=Button(top,text="6",command=lambda:self.put(18))
                self.b18.place(x="155",y="220",width="60",height="40")

                self.b19=Button(top,text="x",command=lambda:self.put(19))
                self.b19.place(x="220",y="220",width="60",height="40")

                self.b20=Button(top,text="1/x",command=lambda:self.put(20))
                self.b20.place(x="285",y="220",width="60",height="40")

                self.b21=Button(top,text="1",command=lambda:self.put(21))
                self.b21.place(x="25",y="270",width="60",height="40")

                self.b22=Button(top,text="2",command=lambda:self.put(22))
                self.b22.place(x="90",y="270",width="60",height="40")

                self.b23=Button(top,text="3",command=lambda:self.put(23))
                self.b23.place(x="155",y="270",width="60",height="40")

                self.b24=Button(top,text="-",command=lambda:self.put(24))
                self.b24.place(x="220",y="270",width="60",height="40")

                self.b25=Button(top,text="=",command=lambda:self.put(25))
                self.b25.place(x="285",y="270",width="60",height="90")

                self.b26=Button(top,text="0",command=lambda:self.put(26))
                self.b26.place(x="25",y="320",width="125",height="40")

                self.b27=Button(top,text=".",command=lambda:self.put(27))
                self.b27.place(x="155",y="320",width="60",height="40")

                self.b28=Button(top, text="+", command=lambda:self.put(28))
                self.b28.place(x="220",y="320",width="60",height="40")

                top.mainloop()

        def put(self,b_id):

                st = ""
                
                if(b_id==1):
                        self.e1.insert(0,str(1))
                if(b_id==2):
                        self.e1.insert(0,str(1))                        
                if(b_id==3):
                        self.e1.insert(0,str(1))                        
                if(b_id==4):
                        self.e1.insert(0,str(1))
                if(b_id==5):
                        self.e1.insert(0,str(1))
                        
                if(b_id==6):
                        st=self.e1.get()
                        n = int(st)
                        n=n/10
                        self.e1.delete(0,'end')
                        self.e1.insert(0,n)
                        
                if(b_id==7):
                        self.e1.delete(0,'end')
                        
                if(b_id==8):
                        self.e1.delete(0,'end')
                        
                if(b_id==9):
                        self.n1=int(self.e1.get())
                        self.flag=9
                        self.e1.delete(0,'end')
                        
                if(b_id==10):
                        self.n1=int(self.e1.get())
                        self.flag=10
                        self.e1.delete(0,'end')
                        
                if(b_id==11):
                        st=self.e1.get()
                        st=st+"7"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==12):
                        st=self.e1.get()
                        st=st+"8"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==13):
                        st=self.e1.get()
                        st=st+"9"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==14):
                        self.n1=int(self.e1.get())
                        self.flag=14
                        self.e1.delete(0,'end')
                        
                if(b_id==15):
                        self.n1=int(self.e1.get())
                        self.flag=15
                        self.e1.delete(0,'end')
                        
                if(b_id==16):
                        st=self.e1.get()
                        st=st+"4"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==17):
                        st=self.e1.get()
                        st=st+"5"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==18):
                        st=self.e1.get()
                        st=st+"6"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==19):
                        self.n1=int(self.e1.get())
                        self.flag=19
                        self.e1.delete(0,'end')
                        
                if(b_id==20):
                        self.n1=int(self.e1.get())
                        self.flag=20
                        self.e1.delete(0,'end')
                        
                if(b_id==21):
                        st=self.e1.get()
                        st=st+"1"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==22):
                        st=self.e1.get()
                        st=st+"2"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==23):
                        st=self.e1.get()
                        st=st+"3"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==24):
                        self.n1=int(self.e1.get())
                        self.flag=24
                        self.e1.delete(0,'end')
                        
                if(b_id==25):

                        self.n2=int(self.e1.get())


                        if(self.flag==9):
                                ans=self.n1+self.n2
                        '''if(self.flag==10):
                                ans=self.n1+self.n2'''
                        if(self.flag==14):
                                ans=self.n1/self.n2
                        if(self.flag==15):
                                ans=self.n1%self.n2
                        if(self.flag==19):
                                ans=self.n1*self.n2
                        '''if(self.flag==20):
                                ans=self.n1+self.n2'''
                        if(self.flag==24):
                                ans=self.n1-self.n2
                        if(self.flag==28):
                                ans=self.n1+self.n2

                        self.e1.delete(0,'end')
                        self.e1.insert(0,str(ans))
                        
                if(b_id==26):
                        st=self.e1.get()
                        st=st+"0"
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""
                        
                if(b_id==27):
                        
                        if(self.count==0):
                                st=self.e1.get()
                                self.count=self.count+1
                                st=st+"."
                                self.e1.delete(0,'end')
                                self.e1.insert(0,st)
                                st=""    
                        else:
                                self.e1.delete(0,'end')
                                st = " Invalid Input "
                                self.e1.insert(0,st)
                                self.count=0
                   
                if(b_id==28):
                        self.n1=int(self.e1.get())
                        stself.e1.get()
                        self.flag=28
                        st=st+"+"
                        self.temp=st
                        self.e1.delete(0,'end')
                        self.e1.insert(0,st)
                        st=""

obj = calculator()
                        
