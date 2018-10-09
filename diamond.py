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
