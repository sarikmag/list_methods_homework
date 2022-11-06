def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    i=0
    n=len(list1)
    m=[]
    while i<n:
        if list1[i]==1:
            m.append(list1[i])
            
        i+=1
    c=len(list1)-len(m)
    a=[]
    a+=[len(m)]
    a+=[c]
    
    return a
print(main((0,0,1,0,0,0,0,0,1,1)))