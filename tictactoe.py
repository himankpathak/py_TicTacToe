
def printlist():
	print ("")
	print (l[0],"|",l[1],"|",l[2])
	print (l[3],"|",l[4],"|",l[5])
	print (l[6],"|",l[7],"|",l[8])

def funcm(ch,j):
	global l
	z=""
	while (z==""):
		z=input()
		
	z=ord(z)-97
	if(z>8 or l[z]=="O" or l[z]=="X"):
		print(">> enter a valid character to place X or O")
		return j
	else:
		l[z]=ch
		return j+1

def namefunc():
	global ch
	if ch=="X":
		return 0
	else:
		return 1

def win():
	global n
	global name
	n=1
	print ("\n",name[namefunc()],"Wins!!\n")

def maingame():

	global n
	global ch
	j=0
	while (j<9): 
		if(j%2==0):
			ch="X"
		else:
			ch="O"
		j=funcm(ch,j)
		
		printlist()
		
		if (l[0]==ch and l[1]==ch and l[2]==ch):
			win()
			break
		elif (l[3]==ch and l[4]==ch and l[5]==ch):
			win()
			break
		elif (l[6]==ch and l[7]==ch and l[8]==ch):
			win()
			break
		elif (l[0]==ch and l[3]==ch and l[6]==ch):
			win()
			break
		elif (l[1]==ch and l[4]==ch and l[7]==ch):
			win()
			break
		elif (l[2]==ch and l[5]==ch and l[8]==ch):
			win()
			break
		elif (l[0]==ch and l[4]==ch and l[8]==ch):
			win()
			break
		elif (l[6]==ch and l[4]==ch and l[2]==ch):
			win()
			break

	if(n==0):
		print ("Match Draw !!")


if __name__ == "__main__":
	l=["_","_","_","_","_","_"," "," "," "]
	n=0
	print("""    Instructions to input:
					
		a|b|c
		d|e|f
		g|h|i \n""")

	name=[]
	name.append(input("Enter the Name of First Player : "))
	name.append(input("Enter the Name of Second Player: "))

	printlist()

	maingame()
