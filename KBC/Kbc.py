question_list = [
	"How many continents are there?",  	
	"What is the capital of India?",		
	"NG mei kaun se course padhaya jaata hai?",
    "where is mumbai?",
    "capital of karnataka?",
]
options_list = [
	#pehle question ke liye options
	["Four", "Nine", "Seven", "Eight"],
	#second question ke liye options
	["Chandigarh", "Bhopal", "Chennai", "Delhi"],
	#third question ke liye options
	["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["china","rajasthan","maharashtra","punjab"],
    ["chennai","bangalore","kolkata","mumbai"]
]
solution_list = [3, 4, 1,3,2]

i=0
list1 = []
while i<len(question_list):
    print str(question_list[i]) 
    j=0
    while j<len(options_list[i]):
        print str(j+1 ) + " " + str(options_list[i][j])
        j=j+1
    if 5 not in list1:
        print str(j+1) + " 50 50"
    user = input("enter the answer")
    if user > 5 :
        print "not valid"
        i=i-1
    elif user == 5 and 5 in list1:
        print "not valid"
        i=i-1
    elif user == solution_list[i]:
        print "Aapka answer sahi hai"
    elif user == 5 and 5 not in list1:
        new_list = [2,1,1,2,2]
        if solution_list[i] == 1:
            print " 1  " + str(options_list[i][0])
            print " 2  " + str(options_list[i][3])
        elif solution_list[i] ==2:
            print " 1 " + str(options_list[i][2]) 
            print " 2 " + str(options_list[i][1])
        elif solution_list[i] == 3:
            print " 1  " + str(options_list[i][3]) 
            print " 2  " + str(options_list[i][2])
        else:
            print " 1 " + str(options_list[i][3]) 
            print " 2 " + str(options_list[i][1])
        use = input("enter number") 
        if use == new_list[i]:
            print "congrats appka anser sahi hai"
        else:
            print "Sadly aapka anser wrong hai"
            print "aap haar chuke ho"
            break 
    else:
        print "Sadly aapka answer galat hai"
        print "you lost the game"
        break
    list1.append(user)
    i=i+1
    
