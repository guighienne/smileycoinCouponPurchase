from Tkinter import *
import ttk
import hashlib
import string
import createTX
import jeeq

class tools_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()


    def initialize(self):
        self.grid()

        ### logo ###

        self.image = PhotoImage(file="C:\Users\guigh\Documents\BlockchainProject\CodePython\PurchaseInBlockchain\logo.gif",master=self)
        self.display = Canvas(self, highlightthickness=0,height=120,width=400)
        self.display.create_image(0,0,image=self.image, anchor='nw',tags="IMGp")
        self.display.grid(columnspan=2,padx=20,pady=20)

        ### txid + pubKey###

        self.entry2 = Entry(self)
        self.entry2.grid(columnspan=4,sticky='EW',padx=10,ipadx=1,ipady=1)
        self.entry2.insert(0,' publicKey')
        self.entry2.bind('<FocusIn>', self.on_entry2_click)
        self.entry2.bind('<FocusOut>', self.on_focus2out)
        self.entry2.config(fg = 'grey')

        self.entry3 = Entry(self)
        self.entry3.grid(sticky='EW',padx=10,pady=20,ipadx=1,ipady=1)
        self.entry3.insert(0,' txid')
        self.entry3.bind('<FocusIn>', self.on_entry3_click)
        self.entry3.bind('<FocusOut>', self.on_focus3out)
        self.entry3.config(fg = 'grey')

        self.entry4 = Entry(self)
        self.entry4.grid(row=2,column=1,sticky='W',padx=0,ipadx=1,ipady=1)
        self.entry4.insert(0,' vout')
        self.entry4.bind('<FocusIn>', self.on_entry4_click)
        self.entry4.bind('<FocusOut>', self.on_focus4out)
        self.entry4.config(fg = 'grey')

        self.entry5 = Entry(self)
        self.entry5.grid(row=2,column=2,sticky='W',padx=10,ipadx=1,ipady=1)
        self.entry5.insert(0,' total amount')
        self.entry5.bind('<FocusIn>', self.on_entry5_click)
        self.entry5.bind('<FocusOut>', self.on_focus5out)
        self.entry5.config(fg = 'grey')

        ### notebook ###

        self.tools=ttk.Notebook(self)
        self.tools.grid(sticky='EW',columnspan=3,padx=10,ipady=5)

        ### transaction1 ###

        self.transaction1=ttk.Frame(self.tools)
        self.tools.add(self.transaction1,text='Transaction1')

        self.entry7 = Entry(self.transaction1)
        self.entry7.grid(columnspan=4,sticky='EW',padx=10,pady=15,ipadx=1,ipady=1)
        self.entry7.insert(0,' text to attach')
        self.entry7.bind('<FocusIn>', self.on_entry7_click)
        self.entry7.bind('<FocusOut>', self.on_focus7out)
        self.entry7.config(fg = 'grey')

        self.entry11 = Entry(self.transaction1)
        self.entry11.grid(sticky='EW',padx=10,ipadx=1,ipady=1)
        self.entry11.insert(0,' seller address')
        self.entry11.bind('<FocusIn>', self.on_entry11_click)
        self.entry11.bind('<FocusOut>', self.on_focus11out)
        self.entry11.config(fg = 'grey')

        self.button_confirm1 = Button(self.transaction1,text=u"Confirm",
                                command=self.OnButtonConfirm1Click)
        self.button_confirm1.grid(row=1,column=3,sticky='E',padx=10)

        self.result1 = Text(self.transaction1,wrap='word',height=8)
        self.result1.grid(row=2,columnspan=4,sticky='EW',padx=10,pady=15)

        self.label1 = Label(self.transaction1, text = "You can sign and send this transaction !")
        self.label1.grid(sticky='E',column=2,columnspan=2,padx=10)

        ### transaction2 ###

        self.transaction2=ttk.Frame(self.tools)
        self.tools.add(self.transaction2,text='Transaction2')

        self.entry8 = Entry(self.transaction2)
        self.entry8.grid(columnspan=4,sticky='EW',padx=10,pady=15,ipadx=1,ipady=1)
        self.entry8.insert(0,' full transaction1')
        self.entry8.bind('<FocusIn>', self.on_entry8_click)
        self.entry8.bind('<FocusOut>', self.on_focus8out)
        self.entry8.config(fg = 'grey')

        self.entry9 = Entry(self.transaction2)
        self.entry9.grid(columnspan=2,sticky='W',padx=10,ipadx=1,ipady=1)
        self.entry9.insert(0,' coupon')
        self.entry9.bind('<FocusIn>', self.on_entry9_click)
        self.entry9.bind('<FocusOut>', self.on_focus9out)
        self.entry9.config(fg = 'grey')

        self.button_confirm2 = Button(self.transaction2,text=u"Confirm",
                                command=self.OnButtonConfirm2Click)
        self.button_confirm2.grid(row=1,column=3,sticky='E',padx=10)

        self.result2_= Text(self.transaction2,wrap='word',height=3)
        self.result2_.grid(columnspan=4,sticky='EW',padx=10,pady=15)

        self.label2_ = Label(self.transaction2, text = "Keep track of this encrypted coupon !",fg='red')
        self.label2_.grid(sticky='E',column=2,columnspan=2,padx=10)

        self.result2 = Text(self.transaction2,wrap='word',height=4)
        self.result2.grid(row=4,columnspan=4,sticky='EW',padx=10,pady=15)

        self.label2 = Label(self.transaction2, text = "You can sign and send this transaction !")
        self.label2.grid(sticky='E',column=2,columnspan=2,padx=10)

        ### transaction3 ###

        self.transaction3=ttk.Frame(self.tools)
        self.tools.add(self.transaction3,text='Transaction3')

        self.entry1 = Entry(self.transaction3)
        self.entry1.grid(columnspan=4,sticky='EW',padx=10,pady=15,ipadx=1,ipady=1)
        self.entry1.insert(0,' full transaction2')
        self.entry1.bind('<FocusIn>', self.on_entry1_click)
        self.entry1.bind('<FocusOut>', self.on_focus1out)
        self.entry1.config(fg = 'grey')

        self.entry6 = Entry(self.transaction3)
        self.entry6.grid(sticky='W',padx=10,ipadx=1,ipady=1)
        self.entry6.insert(0,' price in smly')
        self.entry6.bind('<FocusIn>', self.on_entry6_click)
        self.entry6.bind('<FocusOut>', self.on_focus6out)
        self.entry6.config(fg = 'grey')

        self.button_confirm = Button(self.transaction3,text=u"Confirm",
                                command=self.OnButtonConfirmClick)
        self.button_confirm.grid(row=1,column=3,sticky='E',padx=10)

        self.result = Text(self.transaction3,wrap='word',height=8)
        self.result.grid(row=2,columnspan=4,sticky='EW',padx=10,pady=15)

        self.label = Label(self.transaction3, text = "You can sign and send this transaction !")
        self.label.grid(sticky='E',column=2,columnspan=2,padx=10)

        ### redeem transaction###

        self.redeem=ttk.Frame(self.tools)
        self.tools.add(self.redeem,text='Redeem')

        self.entry12=Entry(self.redeem)
        self.entry12.grid(columnspan=4,sticky='EW',padx=10,pady=15,ipadx=1,ipady=1)
        self.entry12.insert(0,' full transaction3')
        self.entry12.bind('<FocusIn>', self.on_entry12_click)
        self.entry12.bind('<FocusOut>', self.on_focus12out)
        self.entry12.config(fg = 'grey')

        self.entry13=Entry(self.redeem)
        self.entry13.grid(columnspan=4,sticky='EW',padx=10,ipadx=1,ipady=1)
        self.entry13.insert(0,' privateKey')
        self.entry13.bind('<FocusIn>', self.on_entry13_click)
        self.entry13.bind('<FocusOut>', self.on_focus13out)
        self.entry13.config(fg = 'grey')

        self.entry14=Entry(self.redeem)
        self.entry14.grid(columnspan=2,sticky='EW',padx=10,ipadx=1,ipady=1)
        self.entry14.insert(0,' encrypted coupon (for seller only)')
        self.entry14.bind('<FocusIn>', self.on_entry14_click)
        self.entry14.bind('<FocusOut>', self.on_focus14out)
        self.entry14.config(fg = 'grey')

        self.button_confirm4 = Button(self.redeem,text=u"Confirm",
                                command=self.OnButtonConfirm4Click)
        self.button_confirm4.grid(row=2,column=3,sticky='E',padx=10,pady=15)

        self.result4 = Text(self.redeem,wrap='word',height=7)
        self.result4.grid(row=3,columnspan=4,sticky='EW',padx=10)

        self.label = Label(self.redeem, text = "This transaction is already signed !",fg='red')
        self.label.grid(sticky='E',column=2,columnspan=2,padx=10,pady=15)

        ### grid ###

        self.grid_columnconfigure(0,weight=1)
        #self.grid_rowconfigure(1,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry('690x580')

    def on_entry1_click(self,event):
        if self.entry1.get() == ' full transaction2':
            self.entry1.delete(0, "end")
            self.entry1.insert(0, '')
            self.entry1.config(fg = 'black')

    def on_focus1out(self,event):
        if self.entry1.get() == '':
            self.entry1.insert(0, ' full transaction2')
            self.entry1.config(fg = 'grey')

    def on_entry2_click(self,event):
        if self.entry2.get() == ' publicKey':
            self.entry2.delete(0, "end")
            self.entry2.insert(0, '')
            self.entry2.config(fg = 'black')

    def on_focus2out(self,event):
        if self.entry2.get() == '':
            self.entry2.insert(0, ' publicKey')
            self.entry2.config(fg = 'grey')

    def on_entry3_click(self,event):
        if self.entry3.get() == ' txid':
            self.entry3.delete(0, "end")
            self.entry3.insert(0, '')
            self.entry3.config(fg = 'black')

    def on_focus3out(self,event):
        if self.entry3.get() == '':
            self.entry3.insert(0, ' txid')
            self.entry3.config(fg = 'grey')

    def on_entry4_click(self,event):
        if self.entry4.get() == ' vout':
            self.entry4.delete(0, "end")
            self.entry4.insert(0, '')
            self.entry4.config(fg = 'black')

    def on_focus4out(self,event):
        if self.entry4.get() == '':
            self.entry4.insert(0, ' vout')
            self.entry4.config(fg = 'grey')

    def on_entry5_click(self,event):
        if self.entry5.get() == ' total amount':
            self.entry5.delete(0, "end")
            self.entry5.insert(0, '')
            self.entry5.config(fg = 'black')

    def on_focus5out(self,event):
        if self.entry5.get() == '':
            self.entry5.insert(0, ' total amount')
            self.entry5.config(fg = 'grey')

    def on_entry6_click(self,event):
        if self.entry6.get() == ' price in smly':
            self.entry6.delete(0, "end")
            self.entry6.insert(0, '')
            self.entry6.config(fg = 'black')

    def on_focus6out(self,event):
        if self.entry6.get() == '':
            self.entry6.insert(0, ' price in smly')
            self.entry6.config(fg = 'grey')

    def on_entry7_click(self,event):
        if self.entry7.get() == ' text to attach':
            self.entry7.delete(0, "end")
            self.entry7.insert(0, '')
            self.entry7.config(fg = 'black')

    def on_focus7out(self,event):
        if self.entry7.get() == '':
            self.entry7.insert(0, ' text to attach')
            self.entry7.config(fg = 'grey')

    def on_entry8_click(self,event):
        if self.entry8.get() == ' full transaction1':
            self.entry8.delete(0, "end")
            self.entry8.insert(0, '')
            self.entry8.config(fg = 'black')

    def on_focus8out(self,event):
        if self.entry8.get() == '':
            self.entry8.insert(0, ' full transaction1')
            self.entry8.config(fg = 'grey')

    def on_entry9_click(self,event):
        if self.entry9.get() == ' coupon':
            self.entry9.delete(0, "end")
            self.entry9.insert(0, '')
            self.entry9.config(fg = 'black')

    def on_focus9out(self,event):
        if self.entry9.get() == '':
            self.entry9.insert(0, ' coupon')
            self.entry9.config(fg = 'grey')

    def on_entry11_click(self,event):
        if self.entry11.get() == ' seller address':
            self.entry11.delete(0, "end")
            self.entry11.insert(0, '')
            self.entry11.config(fg = 'black')

    def on_focus11out(self,event):
        if self.entry11.get() == '':
            self.entry11.insert(0, ' seller address')
            self.entry11.config(fg = 'grey')

    def on_entry12_click(self,event):
        if self.entry12.get() == ' full transaction3':
            self.entry12.delete(0, "end")
            self.entry12.insert(0, '')
            self.entry12.config(fg = 'black')

    def on_focus12out(self,event):
        if self.entry12.get() == '':
            self.entry12.insert(0, ' full transaction3')
            self.entry12.config(fg = 'grey')

    def on_entry13_click(self,event):
        if self.entry13.get() == ' privateKey':
            self.entry13.delete(0, "end")
            self.entry13.insert(0, '')
            self.entry13.config(fg = 'black')

    def on_focus13out(self,event):
        if self.entry13.get() == '':
            self.entry13.insert(0, ' privateKey')
            self.entry13.config(fg = 'grey')

    def on_entry14_click(self,event):
        if self.entry14.get() == ' encrypted coupon (for seller only)':
            self.entry14.delete(0, "end")
            self.entry14.insert(0, '')
            self.entry14.config(fg = 'black')

    def on_focus14out(self,event):
        if self.entry14.get() == '':
            self.entry14.insert(0, ' encrypted coupon (for seller only)')
            self.entry14.config(fg = 'grey')

    def OnButtonConfirmClick(self):
        self.result.delete('0.0', END)
        md=hashlib.new('ripemd160')
        md.update(hashlib.sha256(self.entry2.get().decode('hex')).digest())
        self.script1='76a914'+md.hexdigest()+'88ac'
        md=hashlib.new('ripemd160')
        md.update(hashlib.sha256(createTX.transaction2_getPubKey(self.entry1.get()).decode('hex')).digest())
        self.script3='76a914'+md.hexdigest()+'88ac'
        self.scriptPubKey=createTX.transaction3_scriptPubKey(self.entry1.get(),self.entry2.get())
        self.script2=self.scriptPubKey
        self.outputs=[[(int(self.entry5.get())-2-int(self.entry6.get()))*100000000,self.script1],[100000000,self.script3],[(int(self.entry6.get()))*100000000,self.script2]]

        ### for P2SH
        # md=hashlib.new('ripemd160')
        # md.update(hashlib.sha256(self.scriptPubKey.decode('hex')).digest())
        # self.script2="a914"+md.hexdigest()+"87"
        #self.script4='6a'+'%02x'%len(self.scriptPubKey.decode('hex'))+self.scriptPubKey
        #self.outputs=[[(int(self.entry5.get())-2-int(self.entry6.get()))*100000000,self.script1],[100000000,self.script3],[(int(self.entry6.get()))*100000000,self.script2],[0,self.script4]]
        self.result.insert('1.0',createTX.makeRawTransaction(self.entry3.get(),int(self.entry4.get()),'',self.outputs))

    def OnButtonConfirm1Click(self):
        self.result1.delete('0.0', END)
        md=hashlib.new('ripemd160')
        md.update(hashlib.sha256(self.entry2.get().decode('hex')).digest())
        self.script1='76a914'+md.hexdigest()+'88ac'
        self.script3='76a914'+createTX.address_to_script(self.entry11.get())+'88ac'
        self.hextext=self.entry7.get().encode('hex')
        self.script2='6a'+'%02x'%len(self.hextext.decode('hex'))+self.hextext
        self.outputs=[[(int(self.entry5.get())-2)*100000000,self.script1],[100000000,self.script3],[0,self.script2]]
        self.result1.insert('1.0',createTX.makeRawTransaction(self.entry3.get(),int(self.entry4.get()),'',self.outputs))

    def OnButtonConfirm2Click(self):
        self.result2.delete('0.0', END)
        self.result2_.delete('0.0', END)
        self.pubKey=createTX.transaction2_getPubKey(self.entry8.get())
        self.EncMessage=jeeq.encrypt_message(self.pubKey.decode('hex'),self.entry9.get()).encode('hex')
        md=hashlib.new('ripemd160')
        md.update(hashlib.sha256(self.entry2.get().decode('hex')).digest())
        self.script1='76a914'+md.hexdigest()+'88ac'
        md=hashlib.new('ripemd160')
        md.update(hashlib.sha256(self.pubKey.decode('hex')).digest())
        self.script3='76a914'+md.hexdigest()+'88ac'
        md=hashlib.new('ripemd160')
        md.update(hashlib.sha256(self.EncMessage.decode('hex')).digest())
        self.script2='6a14'+md.hexdigest()
        self.outputs=[[(int(self.entry5.get())-2)*100000000,self.script1],[100000000,self.script3],[0,self.script2]]
        self.result2.insert('1.0',createTX.makeRawTransaction(self.entry3.get(),int(self.entry4.get()),'',self.outputs))
        self.result2_.insert('1.0',self.EncMessage)


    def OnButtonConfirm4Click(self):
        self.result4.delete('0.0', END)
        md=hashlib.new('ripemd160')
        md.update(hashlib.sha256(self.entry2.get().decode('hex')).digest())
        self.outputs=[[createTX.redeem_data(self.entry12.get())[2],'76a914'+md.hexdigest()+'88ac']]
        self.result4.insert('1.0',createTX.makeSignedTransaction(self.entry13.get(), hashlib.sha256(self.entry12.get().decode('hex')).hexdigest(), 3, createTX.redeem_data(self.entry12.get())[1], createTX.redeem_data(self.entry12.get())[0],self.entry14.get(), self.outputs))

if __name__ == "__main__":
    app = tools_tk(None)
    app.title('SmileyCoin Tools')
    app.mainloop()