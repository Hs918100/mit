lis = [[1,2,3,],[7,4],[3,5]]
dic = {1:'h',2:'a',3:'r',4:'i',5:'s'}
tr = []
for i in range(len(lis)):
    val = 0
    cart = []
    limit = 10
    temp = limit
    for ele in lis[i]:
        val+=ele
        if val>10:
            break
        else:
            cart.append(ele)
    tr.append(cart)
if tr==lis:
    print('buenas tardes')
else:
    print('maricas')



