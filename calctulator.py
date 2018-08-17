'''
Nathanael Sumpter

8/17/2018

tkinter gui calculator

'''
##################################################
##################################################
###### Not the most effeciant calculator... ######
################ But it works ####################
##################################################


from tkinter import *
from tkinter import ttk


#pop-up box for different messages
def popupmsg(msg):
    f = Tk()
    f.iconbitmap("favicon.ico")
    frame = Frame(f)
    frame.pack()
   
    lbl = Label(frame,text = msg,font=12)
    lbl.pack()

    btn = Button(frame,text = "okay",command = f.destroy)
    btn.pack()

    f.mainloop()



class Calc_app():
    def __init__(self,master):
        self.arr = []
        self.operation = ''
        self.fnum = ''
        self.lnum = ''

        frame = Frame(master)
        frame.pack()

        ###output box###
        self.entry = Entry(frame, text="",font=12)

        ###number buttons###
        self.btn1 = ttk.Button(frame,text="1",command=lambda:self.on_click(1))
        self.btn2 = ttk.Button(frame,text="2",command=lambda:self.on_click(2))
        self.btn3 = ttk.Button(frame,text="3",command=lambda:self.on_click(3))
        self.btn4 = ttk.Button(frame,text="4",command=lambda:self.on_click(4))
        self.btn5 = ttk.Button(frame,text="5",command=lambda:self.on_click(5))
        self.btn6 = ttk.Button(frame,text="6",command=lambda:self.on_click(6))
        self.btn7 = ttk.Button(frame,text="7",command=lambda:self.on_click(7))
        self.btn8 = ttk.Button(frame,text="8",command=lambda:self.on_click(8))
        self.btn9 = ttk.Button(frame,text="9",command=lambda:self.on_click(9))
        self.btn0 = ttk.Button(frame,text="0",command=lambda:self.on_click(0))
        self.btnf = ttk.Button(frame,text=".",command=lambda:popupmsg("Floats not accepted yet!"))
        self.btnQuit = ttk.Button(frame,text="Quit",command=quit)


        

        ###clear button###
        self.btn_clr = ttk.Button(frame,text="clear",command=lambda: self.clear(0))

        ###math buttons###
        
        self.btnx = ttk.Button(frame,text="X",command=lambda:self.math('x'))
        self.btnd = ttk.Button(frame,text="/",command=lambda:self.math('/'))
        self.btna = ttk.Button(frame,text="+",command=lambda:self.math('+'))
        self.btns = ttk.Button(frame,text="-",command=lambda:self.math('-'))
        self.btne = ttk.Button(frame,text="=",command=lambda:self.math('='))

        ###grid alignment###
        self.btnf.grid(row=5,column=2,ipady=10,ipadx=3)
        self.btnQuit.grid(row=5,column=0,ipady=10,ipadx=3)
        self.btn_clr.grid(row = 0, column = 4,ipady=10,ipadx=3)
        self.btnx.grid(row=1,column=4,ipady=10,ipadx=3)
        self.btnd.grid(row=2,column=4,ipady=10,ipadx=3)
        self.btna.grid(row=3,column=4,ipady=10,ipadx=3)
        self.btns.grid(row=4,column=4,ipady=10,ipadx=3)
        self.btne.grid(row=5,column=4,ipady=10,ipadx=3)


        self.entry.grid(row=0,column=0,columnspan=3)
        self.btn1.grid(row = 1, column = 0,ipady=10,ipadx=3)
        self.btn2.grid(row = 1, column = 1,ipady=10,ipadx=3)
        self.btn3.grid(row = 1, column = 2,ipady=10,ipadx=3)
        self.btn4.grid(row = 2, column = 0,ipady=10,ipadx=3)
        self.btn5.grid(row = 2, column = 1,ipady=10,ipadx=3)
        self.btn6.grid(row = 2, column = 2,ipady=10,ipadx=3)
        self.btn7.grid(row = 3, column = 0,ipady=10,ipadx=3) 
        self.btn8.grid(row = 3, column = 1,ipady=10,ipadx=3)
        self.btn9.grid(row = 3, column = 2,ipady=10,ipadx=3)
        self.btn0.grid(row = 4, column = 1,ipady=10,ipadx=3)

    #clear output screen
    def clear(self,n):
        self.arr = []
        self.on_click(None)
        if n == 0:

            self.math('0')
        
    def make_num(self,numList):
        s = ''.join(map(str, numList))
        return float(s)

        print(new_arr)
     #### MAX LENGTH FOR ARRAY SHOULD BE 20 ####
     # on click function
    def on_click(self,num):
        self.entry.delete(0,END)
        if num != None:

            self.arr.append(num)
        print(self.arr)
        if len(self.arr) > 1 and num != None:
            for num in reversed(self.arr):
                #print(num)
                self.entry.insert(0,num)
        elif num == None:
            pass
        else:
            self.entry.insert(0,str(num))

    def math(self, s):  
        run = False
        if s == 'x':
            x = self.make_num(self.arr)
            if self.fnum == '':

                self.fnum = x
            else:
                self.lnum = x
            self.operation = 'x'
            print("multiply")
            self.clear(1)
        elif s == '/':
            x = self.make_num(self.arr)
            if self.fnum == '':

                self.fnum = x
            else:
                self.lnum = x
            self.operation = '/'
            print("divide")
            self.clear(1)
        elif s == '+':
            x = self.make_num(self.arr)
            if self.fnum == '':

                self.fnum = x
            else:
                self.lnum = x
            self.operation = '+'
            print("add")
            self.clear(1)
        elif s == '-':
            x = self.make_num(self.arr)
            if self.fnum == '':

                self.fnum = x
            else:
                self.lnum = x
            self.operation = '-'
            print("subtract")
            self.clear(1)
        elif s == '0':
            self.operation = ''
            self.fnum = ''
            self.lnum = ''
        else:
            x = self.make_num(self.arr)
            self.lnum = x
            run = True
            print("equals")

        if run == True:
            if self.operation == 'x':
                print('x')
                answer = int(self.fnum) * int(self.lnum)
                self.clear(1)
                self.entry.insert(0,answer)
            elif self.operation == '/':
                print('/')
                answer = int(self.fnum) / int(self.lnum)
                self.clear(1)
                self.entry.insert(0,answer)

            elif self.operation == '+':
                print('+')
                answer = int(self.fnum) + int(self.lnum)
                self.clear(1)
                self.entry.insert(0,answer)

            elif self.operation == '-':
                print('-')
                answer = int(self.fnum) - int(self.lnum)
                self.clear(1)
                self.entry.insert(0,answer)
            self.fnum = ''
            self.arr.append(answer)
        print(self.fnum,self.lnum)








#main loop
root = Tk()
root.title("Calculator")
root.iconbitmap("favicon.ico")
app = Calc_app(root)
root.mainloop()
