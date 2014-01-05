''' Sort a stack in ascending order. Only one addional stack can be used
'''

def sort_stack(st1):
    st2=[]
    while st1:
        tmp=st1.pop()
        # push st2's top back to st1 until st2's top is less than tmp
        while st2 and st2[-1]>tmp:
            st1.append(st2.pop())
        st2.append(tmp)
    return st2


if __name__=='__main__':
    st1=[2,7,9,3,4,6,5,8,9,10]
    print sort_stack(st1)