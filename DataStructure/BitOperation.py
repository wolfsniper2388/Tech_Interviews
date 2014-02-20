''' simple bit operation
'''

def get_bit(num, i):
    'get bit i of num'
    return 1 if num & (1<<i) !=0 else 0

def set_bit(num,i):
    'set bit i of num to be 1'
    return num | (1<<i)

def clear_bit(num, i):  
    'clear bit i of num to be 0'
    return num & ~(1<<i)

def clear_bits_right(num,i):
    'clear bits right to i (exclusive)'
    return num & (~0 << i)

def clear_bits_left(num,i):
    'clear bits left to i (exclusive)'
    return num & ((1<<(i+1))-1)
    
def update_bit(num, i, b):
    'update bit i of num with b'
    return num & ~(1<<i) | (b<<i)

def toggle_bit(num,i):
    'toggle bit i of num'
    return num ^ (1<<i)


if __name__=='__main__':
    num = 0b1010
    print get_bit(num,2), set_bit(num,2),clear_bit(num,2), update_bit(num,2,1), clear_bits_right(num,3), clear_bits_left(num,1)