def stage1(x):
    return x+x

def stage2(x):
    return x*x

def stage3(x):
    return pow(x,x)
    
print(x := stage1(1), x := stage2(x), stage3(x))

x = 1
print([x:=[1,1]] + [x := [x[1], sum(x)] for i in range(100)])