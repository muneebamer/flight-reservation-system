# Name: Muneeb Bin Amer #
# Roll No: 21-10579 #

#---------------------------------------#
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

root=Tk()
class PlaneManagement:
	ReserveList=[]
	BusButton_Id=[]
	EcoButton_Id=[]
	StuButton_Id=[]
	SeatWin=Tk() #Seating Plan Window
	SeatsOccupied=0
	CargoLimit=2000
	PassengerWeight=0
	Revenue=0
	LuggageLimit=100
	IsiFileId=[]
	def __init__(self):
		self.body()
	def SeatReservation(self):
		self.SeatResWin=Tk()
		self.SeatResWin.geometry('320x200+300+150')
		self.SeatResWin.title('Reserve a Seat')
		self.Name= Label(self.SeatResWin,text='Name:',font=('Times New Roman',10))
		self.entry1=Entry(self.SeatResWin,width=30)
		self.Id=Label(self.SeatResWin,text='ID:',font=('Times New Roman',10))
		self.entry2=Entry(self.SeatResWin,width=30)
		self.SeatClass=Label(self.SeatResWin,text='Seat Class:',font=('Times New Roman',10))
		self.c=Scrollbar(self.SeatResWin)
		self.listbox=Listbox(self.SeatResWin,width=30,height=1) #Use Arrow keys to select class
		self.listbox.insert(0,'Business')
		self.listbox.insert(0,'Economy')
		self.listbox.insert(0,'Student')
		self.button=Button(self.SeatResWin,text='Reserve',width=12,command=self.Reserve)
		self.SeatNumber=Label(self.SeatResWin,text='Seat Number:',font=('Times New Roman',10))
		self.entry3=Entry(self.SeatResWin,width=30)
		self.LuggageWeight=Label(self.SeatResWin,text='Luggage weight:',font=('Times New Roman',10))
		self.entry4=Entry(self.SeatResWin,width=30)
		self.Name.grid(row=0)
		self.entry1.grid(row=0,column=1)
		self.Id.grid(row=1)
		self.entry2.grid(row=1,column=1)
		self.SeatClass.grid(row=2)
		self.listbox.grid(row=2,column=1)
		self.c.grid(row=2,column=5)
		self.SeatNumber.grid(row=3)
		self.entry3.grid(row=3,column=1)
		self.LuggageWeight.grid(row=4)
		self.entry4.grid(row=4,column=1)
		self.button.grid(row=5,padx=10,pady=15)

	def SeatCancel(self):
		self.SeatCncl=Tk()
		self.SeatCncl.geometry('320x100+300+150')
		self.SeatCncl.title('Cancel a Seat')
		self.id=Label(self.SeatCncl,text='ID:',font=('Times New Roman',10))
		self.id.grid(padx=10,pady=5,row=0)
		self.entry=Entry(self.SeatCncl,width=30)
		self.entry.grid(row=0,column=1)
		self.CancelButton=Button(self.SeatCncl,text='Cancel a Seat',width=12,command=self.Cancel)
		self.CancelButton.grid(row=1,column=0,padx=5,pady=30)

	def Cancel(self):
		if self.SeatsOccupied>0:
			self.SeatsOccupied-=1 
		###### ERROR CHECKING ######
		if len(self.entry.get())!=7: #Invalid ID
			messagebox.showinfo('Error','Please enter a valid ID')
			self.SeatCncl.destroy()
			self.SeatCancel()
		
		for x in range(len(self.ReserveList)-1): #Id doesnot exist
			if self.entry.get() not in self.ReserveList[x][1]:
				messagebox.showinfo('Error','No seat reserved with this ID')
				self.SeatCncl.destroy()
				self.SeatCancel()
		if self.ReserveList==[]: # No seats reserved
			messagebox.showinfo('Error','Reserve a Seat First')
			self.SeatCncl.destroy()
			self.SeatCancel()
		############################
		if self.ReserveList!=[]:
			try:
				for n in range(len(self.ReserveList)):
					if int(self.ReserveList[n][1])==int(self.entry.get()) and self.ReserveList[n][2]=='Business':
						self.BusButton_Id[int(self.ReserveList[n][3])-1].configure(bg='black',disabledforeground='red')
						self.Revenue-=200000
						self.CnclPercent=(int(self.ReserveList[n][4])/self.CargoLimit)*100 # Luggage weight %age of an individual
						self.CargoPercent-=self.CnclPercent
						self.BlistBox.delete(ACTIVE)
						self.ReserveList.remove(self.ReserveList[n])

					elif int(self.ReserveList[n][1])==int(self.entry.get()) and self.ReserveList[n][2]=='Economy':
						self.EcoButton_Id[int(self.ReserveList[n][3])-1].configure(bg='black',disabledforeground='red')
						self.Revenue-=100000
						self.CnclPercent=(int(self.ReserveList[n][4])/self.CargoLimit)*100 # Luggage weight %age of an individual
						self.CargoPercent-=self.CnclPercent
						self.ElistBox.delete(ACTIVE)
						self.ReserveList.remove(self.ReserveList[n]) #Removing Economy class tuple from Reservelist
					elif int(self.ReserveList[n][1])==int(self.entry.get()) and self.ReserveList[n][2]=='Student':
						self.StuButton_Id[int(self.ReserveList[n][3])-1].configure(bg='black',disabledforeground='red')
						self.Revenue-=40000
						self.CnclPercent=(int(self.ReserveList[n][4])/self.CargoLimit)*100 # Luggage weight %age of an individual
						self.CargoPercent-=self.CnclPercent
						self.SlistBox.delete(ACTIVE)
						self.ReserveList.remove(self.ReserveList[n]) #Removing Student class tuple from Reservelist
			except IndexError:
				pass
			self.label5.configure(text='Seats Occupied : %d' %(self.SeatsOccupied),font=('Times New Roman',15))
			self.label6.configure(text='Cargo filled : %d %s '%(self.CargoPercent,'%') ,font=('Times New Roman',15))
			self.label7.configure(text='Revenue : %d'%(self.Revenue),font=('Times New Roman',15))
			self.SeatCncl.destroy()

	def Reserve(self):
		self.isiFile=open('isidata.txt','r+')
		
		############### Checking for Errors in form ##############
		

		if len(self.entry2.get())!=7: #Invalid ID
			messagebox.showinfo('Error','Please enter a valid ID')
			self.SeatResWin.destroy()
			self.SeatReservation()

		elif len(self.ReserveList)>=1: #Id Doesnot exist
			for x in range(len(self.ReserveList)):
				if self.entry2.get()==self.ReserveList[x][1]:
					messagebox.showinfo('Error','ID already exists')
					self.SeatResWin.destroy()
					self.SeatReservation()

		elif self.entry1.get()=='' or self.entry2.get()=='' or self.entry3.get()=='' or self.entry4.get()=='': #Empty Fields
			messagebox.showinfo('Error','Please fill all fields')
			self.SeatResWin.destroy()
			self.SeatReservation()

		elif int(self.entry4.get()) > 100: #Luggage Weight
			messagebox.showinfo('Error','Maximum Luggage Weight of 100kg is allowed')
			self.SeatResWin.destroy()
			self.SeatReservation()

		elif self.listbox.get(ACTIVE) == 'Business': #Invalid Seat no in Business Class
			if int(self.entry3.get()) > 12:
				messagebox.showinfo('Error','Invalid Seat Number.')
				self.SeatResWin.destroy()
				self.SeatReservation()	

		elif self.listbox.get(ACTIVE) == 'Economy' and int(self.entry3.get() ) > 24: #Invalid Seat no in Economy class
			messagebox.showinfo('Error','Invalid Seat Number.')
			self.SeatResWin.destroy()
			self.SeatReservation()

		elif self.listbox.get(ACTIVE) == 'Student' and int(self.entry3.get() ) > 8:  #Invalid Seat no in Student class
			messagebox.showinfo('Error','Invalid Seat Number.')
			self.SeatResWin.destroy()
			self.SeatReservation()

		if self.listbox.get(ACTIVE)=='Business': #Seat already reserved in business class
			for n in range(len(self.ReserveList)):
				if self.ReserveList[n][2]=='Business' and self.entry3.get() == self.ReserveList[n][3]:
					messagebox.showinfo('Error','Seat already Taken')
					self.SeatResWin.destroy()
					self.SeatReservation()

		if self.listbox.get(ACTIVE)=='Economy': #Seat already reserved in Economy class
			for n in range(len(self.ReserveList)):
				if self.ReserveList[n][2]=='Economy' and self.entry3.get() == self.ReserveList[n][3]:
					messagebox.showinfo('Error','Seat already Taken')
					self.SeatResWin.destroy()
					self.SeatReservation()

		if self.listbox.get(ACTIVE)=='Student': #Seat already reserved in Student class
			for n in range(len(self.ReserveList)):
				if self.ReserveList[n][2]=='Student' and self.entry3.get() == self.ReserveList[n][3]:
					messagebox.showinfo('Error','Seat already Taken')
					self.SeatResWin.destroy()
					self.SeatReservation()

		############################################################

		if len(self.entry2.get())==7:
			self.SeatsOccupied+=1
			self.PassengerWeight+=int(self.entry4.get())
			self.CargoPercent=(self.PassengerWeight/self.CargoLimit)*100
			self.ReserveList.append((self.entry1.get(),self.entry2.get(),self.listbox.get(ACTIVE),self.entry3.get(),self.entry4.get()))
			if self.listbox.get(ACTIVE)=='Business': #Adding Person to listbox
				self.Revenue+=200000
				self.BlistBox.insert(0,self.entry1.get())
				self.BusButton_Id[int(self.entry3.get())-1].configure(bg='green',disabledforeground='white')
				for line in self.isiFile: 
					if self.entry2.get() in line and 'TERRORIST' in line:#Checking for Terrorist
						self.BusButton_Id[int(self.entry3.get())-1].configure(bg='red',disabledforeground='white')
				if self.entry2.get() not in self.IsiFileId: # Checking for ID
					self.BusButton_Id[int(self.entry3.get())-1].configure(bg='orange',disabledforeground='black')

					
					
			elif self.listbox.get(ACTIVE)=='Economy':
				self.Revenue+=100000
				self.ElistBox.insert(0,self.entry1.get())
				self.EcoButton_Id[int(self.entry3.get())-1].configure(bg='green',disabledforeground='white')
				for line in self.isiFile:
					if self.entry2.get() in line and 'TERRORIST' in line:
						self.EcoButton_Id[int(self.entry3.get())-1].configure(bg='red',disabledforeground='white')
				if self.entry2.get() not in self.IsiFileId:
					self.EcoButton_Id[int(self.entry3.get())-1].configure(bg='orange',disabledforeground='black')

					
			elif self.listbox.get(ACTIVE)=='Student':
				self.Revenue+=40000
				self.SlistBox.insert(0,self.entry1.get())
				self.StuButton_Id[int(self.entry3.get())-1].configure(bg='green',disabledforeground='white')
				for line in self.isiFile:
					if str(self.entry2.get()) in line and 'TERRORIST' in line:
						self.StuButton_Id[int(self.entry3.get())-1].configure(bg='red',disabledforeground='white')
				if self.entry2.get() not in self.IsiFileId:
					self.StuButton_Id[int(self.entry3.get())-1].configure(bg='orange',disabledforeground='black')

			self.label5.configure(text='Seats Occupied : %d' %(self.SeatsOccupied),font=('Times New Roman',15))
			self.label6.configure(text='Cargo filled : %d %s '%(self.CargoPercent,'%') ,font=('Times New Roman',15))
			self.label7.configure(text='Revenue : %d'%(self.Revenue),font=('Times New Roman',15))			
		
			self.SeatResWin.destroy()

	def LoadFile(self):
		self.name=askopenfilename(filetypes=(('Files','*.txt'),('All Files','*.*')))
		print(self.name)
		self.file=open(self.name,'r')
		print(self.file.read())
		self.file.close()
	def SaveFile(self):
		self.name=asksaveasfile(mode='w+', defaultextension=".txt")
		if self.name == None:
			return
		self.name.write(str(self.ReserveList))
		self.name.close()

	def body(self):
		root.title('PIA Airline Reservation')
		root.geometry('500x400+300+150')

		self.isiFile=open('isidata.txt','r+')
		for line in self.isiFile: #Adding id to list
			self.IsiFileId.append(line[:7])
		
		self.lbl1=Label(root,text='PIA Ticket Reservation',font=('Times New Roman',18),fg='blue')
		self.lbl1.pack()	
		self.SeatRes=Button(root,text='Seat Reservation',command=self.SeatReservation)
		self.SeatCncl=Button(root,text='Seat Cancellation',command=self.SeatCancel)
		self.SeatRes.pack(),self.SeatCncl.pack()
		self.seperator=Label(root ,text='------------------------------')
		self.seperator.pack(pady=5)
		self.Load=Button(root,text='Load from File',command=self.LoadFile)
		self.Save=Button(root,text='Save to File',command=self.SaveFile)
		self.Load.pack(),self.Save.pack()
		self.f=Frame(root)
		self.f.pack(side='top',fill=BOTH)
		self.B=Label(self.f,text='Business Class',font=('Times New Roman',15),fg='blue')
		self.S=Label(self.f,text='Economy Class  ',font=('Times New Roman',15),fg='blue')
		self.E=Label(self.f,text='Student Class',font=('Times New Roman',15),fg='blue')
		self.B.pack(padx=30,side='left'),self.S.pack(side='left'),self.E.pack(padx=30,side='left')
		self.BlistBox=Listbox(root,fg='red')
		self.SlistBox=Listbox(root,fg='red')
		self.ElistBox=Listbox(root,fg='red')
		self.BlistBox.pack(side='left',fill=BOTH,expand=True),self.ElistBox.pack(side='left',fill=BOTH,expand=True),self.SlistBox.pack(side='left',fill=BOTH,expand=True)
		self.BlistBox.bind('<<ListboxSelect>>', self.LBClick)
		self.ElistBox.bind('<<ListboxSelect>>', self.LBClick)
		self.SlistBox.bind('<<ListboxSelect>>', self.LBClick)
		############# Labels for Seating Plan Window #######################3
		self.label7=Label(self.SeatWin,text='Revenue : 0' ,font=('Times New Roman',15),bg='#cfe0e8')
		self.label7.pack(side=BOTTOM)
		self.label6=Label(self.SeatWin,text='Cargo filled : 0 %' ,font=('Times New Roman',15),bg='#cfe0e8')
		self.label6.pack(side=BOTTOM)
		self.label5=Label(self.SeatWin,text='Seats Occupied : %d' %(self.SeatsOccupied),font=('Times New Roman',15),bg='#cfe0e8')
		self.label5.pack(side=BOTTOM)
	def LBClick(self,event): #Button turns yellow when selected in Listbox
		try:
			self.w=event.widget
			self.index=int(self.w.curselection()[0])
			self.value=self.w.get(self.index)
			for n in range(len(self.ReserveList)):
				if self.value == self.ReserveList[n][0] and self.ReserveList[n][2]=='Business':
					self.BusButton_Id[int(self.ReserveList[n][3])-1].configure(bg='yellow',disabledforeground='black')
				elif self.value == self.ReserveList[n][0] and self.ReserveList[n][2]=='Student':
					self.StuButton_Id[int(self.ReserveList[n][3])-1].configure(bg='yellow',disabledforeground='black')
				elif self.value == self.ReserveList[n][0] and self.ReserveList[n][2]=='Economy':
					self.EcoButton_Id[int(self.ReserveList[n][3])-1].configure(bg='yellow',disabledforeground='black')
		except IndexError:
			pass	
		
###########Seating Class###############

class SeatingPlan(PlaneManagement):
	
	def __init__(self):
		self.SeatNo=1
		self.body()

	def body(self):
		self.SeatWin.title('Seating Plan')
		self.SeatWin.geometry('250x550+820+90')
		self.SeatWin.configure(background='#cfe0e8')
		self.label=Label(self.SeatWin,text='Plane # 1',font=('Times New Roman',18),fg='blue',bg='#cfe0e8').pack()
		self.label2=Label(self.SeatWin,text='Business Class',font=('Times New Roman',15),bg='#cfe0e8').pack()
		self.frame1=Frame(self.SeatWin,bg='#cfe0e8')
		self.frame1.pack()
		for n in range(3):
			for x in range(4):
				self.btn=Button(self.frame1,text=str(self.SeatNo),width=5,state=DISABLED,bg='black',disabledforeground='red')
				self.btn.grid(row=n,column=x)
				self.BusButton_Id.append(self.btn)
				self.SeatNo+=1
		self.SeatNo=1
		self.label3=Label(self.SeatWin,text='Economy Class',font=('Times New Roman',15),bg='#cfe0e8').pack()
		self.frame2=Frame(self.SeatWin,bg='#cfe0e8')
		self.frame2.pack()

		for n in range(6):
			for x in range(4):
				self.btn=Button(self.frame2,text=str(self.SeatNo),width=5,state=DISABLED,bg='black',disabledforeground='red')
				self.btn.grid(row=n,column=x)
				self.EcoButton_Id.append(self.btn)
				self.SeatNo+=1
		self.SeatNo=1
		self.label4=Label(self.SeatWin,text='Student Class',font=('Times New Roman',15),bg='#cfe0e8').pack()
		self.frame3=Frame(self.SeatWin,bg='#cfe0e8')
		self.frame3.pack()
		for n in range(2):
			for x in range(4):
				self.btn=Button(self.frame3,text=str(self.SeatNo),width=5,state=DISABLED,bg='black',disabledforeground='red')
				self.btn.grid(row=n,column=x)
				self.StuButton_Id.append(self.btn)
				self.SeatNo+=1

#---------------------------------#				
x=PlaneManagement()
y=SeatingPlan()
root.mainloop()