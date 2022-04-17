def problem3(x):
    start = [1,1] #initail point
    for i in range(3,x+1):#start from the given initial and count
        next_num = start[-1] + start[-2] #using indexing add the last two numbers in list
        start.append(next_num)
    return start
