import clientpy2
a=1
status=clientpy2.run("a", "a","STATUS")
status=status.split()
playerx=status[1]
playery=status[2]
#while a == 1:
clientpy2.run("a", "a","ACCELERATE 0 0.5")
clientpy2.run("a", "a","ACCELERATE 3.14 1")
clientpy2.run("a", "a","ACCELERATE 1.57 0.5")
clientpy2.run("a", "a","ACCELERATE 4.71 1")
print(playerx+" "+playery)
while a==1:
    status=clientpy2.run("a", "a","STATUS")
    status=status.split()
    playerx=status[1]
    playery=status[2]
    clientpy2.run("a", "a","BOMB "+playerx+" "+playery)
    #print(status[6])
#(playerx)
#print(status)
