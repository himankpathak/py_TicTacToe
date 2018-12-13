
def printlist():
	print ("\n")
	print (l[0],"|",l[1],"|",l[2])
	print (l[3],"|",l[4],"|",l[5])
	print (l[6],"|",l[7],"|",l[8])
	print ("\n")

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
