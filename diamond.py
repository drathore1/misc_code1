side = int(input("side length: "))
count = 0

while count < side:
    str = [' ']*side*2
    str[side-count-1] = '*'
    str[side+count-1] = '*'
    str = ''.join(str) 
    print str
    count = count + 1

left = 1
right = (side*2)-3

while count > 1:
    str = [' ']*side*2
    str[left] = '*'
    str[right] = '*'
    str = ''.join(str) 
    print str
    left = left + 1
    right = right - 1
    count = count - 1
    
    
"""
while count < side:
    x = side - count
    print "side: ", side, " count: ", count
    str = x * " " + (count * "*")
    #print (x * " ", (count * "*") * 2)
    print (str)
    count += 2
while count >= 0:
    str = bl * " " + (count * "*")
    print (str)
    #print (bl * " ", (count * "*") * 2)
    count -= 1
    bl += 1
"""
