question = ["which one is software","what is set of instruction called","which is a programming language","which is a framework","which code is a machine code","what is needed to connect to server","which is operating system","what is brain of computer","which one is hardware","what is assignment to a value called"]
first_option = ["mouse","server","english","django","source code","internet","data","keyboard","apps","variable"]
second_option = ["application","client","hindi","java","diff code","usb","software","speaker","program","boolean"]
third_option = ["keyboard","data","pytohn","java.script","sudo code","remote","linux","monitor","laptop","operators"]
fourth_option = ["monitor","variable","spanish","c++","object_code","program","monitor","CPU","python","function"]
all_option = [first_option,second_option,third_option,fourth_option]
answer_key = [1,2,2,0,3,0,2,3,2,0]
length = len(question)# this will show the length of the list
correct_ans = 0
print length
i=0
answer_list = []# here we assigned the empty list
while i < length:# condition for the loop to run till
    print ("* " +question[i] + "? - " + str(len(question[i])))# as per thew loop and condition this will print the question as well as the length of the question ans we have converted the length into string bcoz string and integer cannot add 
    k=0# here we assign the new vaiable for the second loop inside the first loop
    while k < len(all_option):# this loop will run till the length of all_option list
        print (str(k) + "." + all_option[k][i] )# by using first and second loop this will print according to the condition
        k=k+1# here we do the increment so that it can move further and go to the next part
    user = input("enter a number from 0 to 4:-")# here we take the in-put from the user as he will put the answer of the questrion that will be on his screen through our code
    if user > 3:# here if the user put the answer which is not in option we give the condition
        i = i-1# then this would not be taken as an answer and due to decrement the index wont go further and the user will get the second chance to answer the question again
        print "not valid"# this will print that the user had put the invaid answer    
    if user < 4:#if the user answer is fron the option given to him we give the condition
        answer_list.append(user)# then user answer will be appended means added to the empty list
        if user == answer_key[i]:#now through the index we will check weather the answer which our code has and users amswer match or not
            correct_ans = correct_ans+1#if it matches it will count the munbers of corerect answers fiven by the user
            print "your answer is correct"# so the answer is correct thats y the computer will print answer is correct
        else:# here we give the else that means that if the earlier condition is not true then we come to thids that if our answer is not correct
            print "Sadly, your answer is incorrect"# it wiil print that u lost the game
            print "you lost the game better luck next time and you have won rs " + str(price) #here we declare that the user has lost his game and won that much amount
            break# so if the user gives wrong answer then the loop will beark and he game would stop
    if correct_ans == 3:# thsi will chk if user has given 3 right answers
        print "congrats you have completed first level and you have won rs 10000"# this will tell the user that he has won this much amt
    if correct_ans == 5:# thsi will chk if user has given 5 right answers
        print "congrats you have completed the second level and you have won rs 50000"# this will tell the user that he has won 50000
    if correct_ans == 8:# thsi will chk weather the user have given 8 right answers
        print "congrats you have completed third level and you have won rs 1,00000"# this will tell the user that he has won 8 right answers
    if correct_ans == 10:# this will chk weather the user has givne 10 right answers
        print "congrats yothsi will chk if user has given 3 right u have completed fourth level and you have won rs 10,00000"#this will tell the user that hwe has won 10 lakh ruppes
    if correct_ans == 12:# this will chk weather the user has given 12 right answers
        print "conrats you have completed second last level and you have won rs 50,00000"# this will tell the user that he has won 50 lakh
    if correct_ans == 15:# this will chk weather the user has given 15 correct answers
        print "congrats you have completed last level and you havce won rs 1,00,00000"#this will tell the user that he as won 1 crore rupees
        print "you have won the game congratulations"#this will tell the user that he has won the game
    i=i+1