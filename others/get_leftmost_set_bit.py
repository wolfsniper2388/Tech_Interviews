def get_leftmost_set_bit(num):
    bits = 0
    if num & 0xffff0000:
        num &= 0xffff0000
        bits += 16
    if num & 0xff00ff00:
        num &= 0xff00ff00
        bits += 8
    if num & 0xf0f0f0f0:
        num &= 0xf0f0f0f0
        bits += 4
    if num & 0xcccccccc:
        num &= 0xcccccccc
        bits += 2
    if num & 0xaaaaaaaa:
        num &= 0xaaaaaaaa
        bits += 1
    return bits


left_shifts = range(0,32)
for left_shift in left_shifts:
    print left_shift, get_leftmost_set_bit(1<<left_shift)
    
print get_leftmost_set_bit(0x30a0)