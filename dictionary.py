#questions = {"name":"anna","age":"101","country of birth":"the United States","favorate language":"Python"}
#def qAndA():
#    print "My name is", str(questions["name"])
#    print "My age is", str(questions["age"])
#    print "my countery of birth is", str(questions["country of birth"])
#    print "my favorate language is", str(questions["favorate language"])
#qAndA()

questions = {"name":"anna","age":"101","country of birth":"the United States","favorate language":"Python"}
def qAndA(q):
    print "My name is {} '\n' My age is {} '\n' my countery of birth is {} '\n' my favorate language is {}".format(str(questions["name"]), str(questions["age"]), str(questions["country of birth"]), str(questions["favorate language"]))
    
qAndA(questions)