tup1=input("enter the first tuple: ")
list1= tup1.split(",")
tup1=tuple(list1)
tup2=input("enter the second tuple: ")
list2=tup2.split(",")
tup2=tuple(list2)
tup3=input("enter the third tuple: ")
list3=tup3.split(",")
tup3=tuple(list3)
print(type(tup1))
if (type(tup1)==tuple):
	while(True):
		print("menu")
		print("1=creating tuple")
		print("2=concatination")
		print("3=repitation")
		print("4=rang slicing")
		print("5=slicing")
		print("6=string membership")
		print("7=iterating through string")
		print("8=length of a tuple")
		print("9=maximum value from a tuple")
		print("10=deleting a tuple")
		print("11=exit")
		rece=int(input("enter your choice: "))
		if (rece==1):
			val1=tuple(input("enter to create a list"))
			print(val1)
		elif (rece==2):
			print(tup1+tup2)
		elif (rece==3):
			print(tup2*2)
		elif(rece==4):
			sl1=int(input("enter the starting slicig"))
			sl2=int(input("enter the ending slincig: "))
			print(tup1[sl1:sl2])
		elif (rece==5):
			slicing=int(input("enter the slicingi number: "))
			print(tup1[slicing])
		elif (rece==6):
			meme=str(input("enter the character: "))
			print(meme in tup1)
		elif (rece==7):
			for i in tup2:
				print(i)
		elif (rece==8):
			print(len(tup1))
		elif (rece==9):
			print(max(tup1))
		elif (rece==10):
			del tup1 
			print("succefully deleted the first tuple")

		else:
			break	
else:
	print("invalid input")	
