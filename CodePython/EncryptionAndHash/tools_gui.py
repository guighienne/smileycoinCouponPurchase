from Tkinter import *
import ttk
import hashlib
import string
import base58
import jeeq

class tools_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()


    def initialize(self):
        self.grid()
        self.b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

        ### logo ###

        self.image = PhotoImage(file="logo.gif",master=self)
        self.display = Canvas(self, highlightthickness=0,height=120,width=400)
        self.display.create_image(0,0,image=self.image, anchor='nw',tags="IMGp")
        self.display.grid(padx=20,pady=20)

        ### notebook ###

        self.tools=ttk.Notebook(self)
        self.tools.grid(columnspan=20,padx=20)

        ### encryption ###

        self.encryption_tool=ttk.Frame(self.tools)
        self.tools.add(self.encryption_tool,text='Encryption')

        self.entry1 = Entry(self.encryption_tool)
        self.entry1.grid(row=1,columnspan=20,sticky='EW',padx=15,pady=20,ipadx=1,ipady=1)
        self.entry1.insert(0,'Enter a message here...')
        self.entry1.bind('<FocusIn>', self.on_entry1_click)
        self.entry1.bind('<FocusOut>', self.on_focus1out)
        self.entry1.config(fg = 'grey')

        self.entry2 = Entry(self.encryption_tool)
        self.entry2.grid(row=2,columnspan=20,sticky='EW',padx=15,ipadx=1,ipady=1)
        self.entry2.insert(0,'Enter a PublicKey (to encrypt) or a PrivateKey (to decrypt)...')
        self.entry2.bind('<FocusIn>', self.on_entry2_click)
        self.entry2.bind('<FocusOut>', self.on_focus2out)
        self.entry2.config(fg = 'grey')

        self.button_encrypt = Button(self.encryption_tool,text=u"Encrypt",
                                command=self.OnButtonEncryptClick)
        self.button_encrypt.grid(column=18,row=3,sticky='E',padx=0,pady=15)

        self.button_decrypt = Button(self.encryption_tool,text=u"Decrypt",
                                command=self.OnButtonDecryptClick)
        self.button_decrypt.grid(column=19,row=3,sticky='E',padx=15,pady=15)

        self.result = Text(self.encryption_tool,wrap='word',height=8)
        self.result.grid(column=0,row=4,columnspan=20,sticky='EW',padx=15,pady=5)

        self.CheckVar1 = IntVar()
        self.C1 = Checkbutton(self.encryption_tool, text = "Automatically convert to hexadecimal", variable = self.CheckVar1, onvalue = 1, offvalue = 0,command=self.OnButtonConvertClick)
        self.C1.grid(row=5,sticky='W',padx=11)
        #self.C1.select()

        ### hash ###

        self.hash_tool=ttk.Frame(self.tools)
        self.tools.add(self.hash_tool,text='Hash')

        self.entry3 = Entry(self.hash_tool)
        self.entry3.grid(columnspan=20,sticky='EW',padx=15,pady=20,ipadx=1,ipady=1)
        self.entry3.insert(0,'Enter hexadecimal string... ')
        self.entry3.bind('<FocusIn>', self.on_entry3_click)
        self.entry3.bind('<FocusOut>', self.on_focus3out)
        self.entry3.config(fg = 'grey')

        self.labelChoice = Label(self.hash_tool, text = "Choose an algorithm:")
        self.labelChoice.grid(column=17,sticky='e')
        self.listAlgo=["RIPEMD-160", "SHA-1","SHA-256","HASH-160","HASH-256"]

        self.listCombo = ttk.Combobox(self.hash_tool, values=self.listAlgo)
        self.listCombo.current(2)
        self.listCombo.grid(row=1,column=18)

        self.button_hash = Button(self.hash_tool,text=u"Hash",
                                command=self.OnButtonHashClick)
        self.button_hash.grid(row=1,column=19,sticky='e',padx=15)

        self.result_ = Text(self.hash_tool,wrap='word',height=11)
        self.result_.grid(columnspan=20,sticky='EW',padx=15,pady=20)

        ### grid ###

        self.grid_columnconfigure(0,weight=1)
        #self.grid_rowconfigure(1,weight=1)
        self.resizable(True,True)
        self.update()
        self.geometry('800x550')

    def on_entry1_click(self,event):
        if self.entry1.get() == 'Enter a message here...':
            self.entry1.delete(0, "end")
            self.entry1.insert(0, '')
            self.entry1.config(fg = 'black')

    def on_focus1out(self,event):
        if self.entry1.get() == '':
            self.entry1.insert(0, 'Enter a message here...')
            self.entry1.config(fg = 'grey')

    def on_entry2_click(self,event):
        if self.entry2.get() == 'Enter a PublicKey (to encrypt) or a PrivateKey (to decrypt)...':
            self.entry2.delete(0, "end")
            self.entry2.insert(0, '')
            self.entry2.config(fg = 'black')

    def on_focus2out(self,event):
        if self.entry2.get() == '':
            self.entry2.insert(0, 'Enter a PublicKey (to encrypt) or a PrivateKey (to decrypt)...')
            self.entry2.config(fg = 'grey')

    def OnButtonEncryptClick(self):
        self.result.delete('0.0', END)
        self.message=self.entry1.get()
        if all(c in string.hexdigits for c in self.entry2.get())==False:
            self.result.insert('1.0','ERROR: PubKey has to be in hexadecimal')
        elif len(self.entry2.get())%2!=0:
            self.result.insert('1.0','ERROR: odd-length hexadecimal PubKey')
        elif (len(self.entry2.get().decode('hex'))!=33 and len(self.entry2.get().decode('hex'))!=65):
            self.result.insert('1.0','ERROR: non recognized PubKey format')
        else:
            PubKey=self.entry2.get().decode('hex')
            self.EncMessage=jeeq.encrypt_message(PubKey,self.message)
            if self.CheckVar1.get()==1:
                self.EncMessage=self.EncMessage.encode('hex')
            self.result.insert('1.0',self.EncMessage)

    def OnButtonDecryptClick(self):
        self.C1.deselect()
        self.result.delete('0.0', END)
        self.EncMessage=self.entry1.get()
        if all(c in string.hexdigits for c in self.EncMessage)==False:
            self.EncMessage=self.EncMessage.encode('hex')
        self.EncMessage=self.EncMessage.decode('hex')
        if all(c in self.b58chars for c in self.entry2.get())==False:
            self.result.insert('1.0','ERROR: PrivKey has to be in base58')
        elif (len(base58.b58decode(self.entry2.get()).decode('hex'))!=32):
            self.result.insert('1.0','ERROR: non recognized PrivKey format')
        else:
            self.PrivKey=base58.b58decode(self.entry2.get()).decode('hex')
            self.Message=jeeq.decrypt_message(self.PrivKey, self.EncMessage, verbose=True, generator=jeeq.generatorBitcoin)
            self.result.insert( '1.0',self.Message)

    def OnButtonConvertClick(self):
        text=self.result.get('0.0', END).encode('ascii','ignore')[:-1]
        if len(text)==0:do=False
        elif len(text)<6:do=True
        elif text[:5]!='ERROR':do=True
        else:do=False
        if do==True:
            if self.CheckVar1.get()==1:
                self.result.delete('0.0', END)
                self.result.insert('1.0',text.encode('hex'))
            elif all(c in string.hexdigits for c in text):
                if len(text)%2!=0:
                    text='0'+text
                self.result.delete('0.0', END)
                self.result.insert('1.0',text.decode('hex'))

    def on_entry3_click(self,event):
        if self.entry3.get() == 'Enter hexadecimal string... ':
            self.entry3.delete(0, "end")
            self.entry3.insert(0, '')
            self.entry3.config(fg = 'black')

    def on_focus3out(self,event):
        if self.entry3.get() == '':
            self.entry3.insert(0, 'Enter hexadecimal string... ')
            self.entry3.config(fg = 'grey')

    def OnButtonHashClick(self):
        self.algo=self.listCombo.get()
        self.result_.delete('0.0', END)
        self.message=self.entry3.get()
        if all(c in string.hexdigits for c in self.message)==False:
            self.result_.insert('1.0','ERROR: string has to be in hexadecimal')
        elif len(self.message)%2!=0:
            self.result_.insert('1.0','ERROR: odd-length hexadecimal string')
        else:
            if self.algo=="RIPEMD-160":
                md=hashlib.new('ripemd160')
                md.update(self.message.decode('hex'))
                self.hash_message=md.hexdigest()
            elif self.algo=="SHA-1":
                self.hash_message=hashlib.sha1(self.message.decode('hex')).hexdigest()
            elif self.algo=="SHA-256":
                self.hash_message=hashlib.sha256(self.message.decode('hex')).hexdigest()
            elif self.algo=="HASH-160":
                md=hashlib.new('ripemd160')
                md.update(hashlib.sha256(self.message.decode('hex')).digest())
                self.hash_message=md.hexdigest()
            else:
                md=hashlib.new('sha256')
                md.update(hashlib.sha256(self.message.decode('hex')).digest())
                self.hash_message=md.hexdigest()
            self.result_.insert('1.0',self.hash_message)

if __name__ == "__main__":
    app = tools_tk(None)
    app.title('SmileyCoin Tools')
    app.mainloop()