def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def mulitply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return ("bajanarary chi kara 0 lini")
    return x / y
while True:
    
    tarberakner=input("Choose one of the digitis, {1=add,2=subtract,3=multiply,4=divide,5=exit:}")
    ls=['1','2','3','4','5']
    if tarberakner not in ls:
        print("choose one of them")
        continue
    if tarberakner=='5':
        print("Exit")
        break
    num1=input('Enter firts number:')
    if not num1.isdigit():
        print('Enter a number')
        continue
    num2=input("Enter a second number:")
    if not num2.isdigit():
        print("asum em tiv chi")
        continue
    num1=float(num1)
    num2=float(num2)
    

    if tarberakner =='1':
        result=add(num1,num2)
    elif tarberakner =='2':
        result=subtract(num1,num2)
    elif tarberakner =='3':
        result=multiply(num1,um2)
    elif tarberakner=='4':
        result=divide(num1,num2)

    print("Result:", result)
        
