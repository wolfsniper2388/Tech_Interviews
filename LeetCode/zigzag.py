'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

def zigzag_convert(s, nRows):
        t=[]
        step = 2*nRows-2
        if step == 0:
            return s
        for i in range(nRows):
            if i < len(s):
                t.append(s[i])
            boundary=step
            while boundary < len(s)+step:
                if i!=0 and i!=step/2 and boundary-i<len(s):
                    t.append(s[boundary-i])
                if boundary+i<len(s):
                    t.append(s[boundary+i])
                boundary+=step
        return ''.join(t)


if __name__=='__main__':
    test_cases = [('PAYPALISHIRING',3), ('PAYPALISHIRING', 5), ('',10), ('A',1)]
    for each_test_case in test_cases:
        s,nRows = each_test_case
        print zigzag_convert(s, nRows)