import random

for x in range(0,1000):
    print "create (n"+ str(x) + ":Person {Name:'" + str(x) + "'})"
    print "create (b"+ str(x) + ":Book {Name:'" + str(x) + "'})"

for x in range(0,1000):
    a = str(random.randint(0, 1000))
    b = str(random.randint(0, 1000))
    print "create (n" + a + ")-[:WROTE]->(b" + b + ")"
#    print "with n" + a + ", m" + b + " "
    
