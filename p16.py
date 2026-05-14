# Parameterized and Functional Recursion

# Sum of 1 to N [Parameterized]

def func(Sum,i,N):
    if i > N:
        print(Sum)
        return
    func(Sum+i,i+1,N)
func(0,1,4) # 1+2+3+4 = 10