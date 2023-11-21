def create_counter(value=0):
        counter=value

        def increment_counter(hashivy=1):
            nonlocal counter
            counter+=hashivy
            print("after increment=",counter)

        def decrement_counter(hashivy=1):
            nonlocal counter
            counter-= hashivy
            print("after decrement=",counter)

    

        def get_counter_value():
            return counter
        return increment_counter,decrement_counter,get_counter_value


    
while True:
    yntreq=input("Choose one of them.{1=increment,2=decrement,3=exit}: ")
    if yntreq == '1':
        tivy=int(input("Enter a number you want to increment:"))
        obj = create_counter(tivy)
        obj[0]()
    elif yntreq =='2':
        tivy=int(input("Enter a number you want to decrement:"))
        obj = create_counter(tivy)
        obj[1]()
    elif yntreq =='3':
        break
    else:
        print("invalid number you choose:")


