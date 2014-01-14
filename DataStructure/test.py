from pprint import pprint
n=10
edge=[[0 for i in range (n)] for j in range (n)]
#pprint (edge)
edge[1][1]=20
#pprint (edge)
vert=[0 for i in range (n)]
a=[1,2,3]
if 5 in a:
    print 'yes'


def increase():
    '''   
    adict={}
    i=0
    while True:
        adict[i+1]=i+2
        i+=1
        print adict
        yield adict
    '''
    adict={}
    for i in range (3):
        adict[i]=i*i
        yield adict

for a in increase():
    print a
    
    
def test():
    a=[0]
    test_helper(a)
    return a
def test_helper(b):
    b.append(1)

num_return=test()
print "num_return is "
print num_return



print 'Testing for loop'
seq=[7,9,3,1,10,2,5,4,6]


a={'(())':1}
print a
a['(())']=1
print a

a=['(',')']

a=[None]*4
a[0]='('
print a

print sorted([3,1,4])
print (1,2) +3
