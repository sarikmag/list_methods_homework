def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    m=[]
    n=5
    i=0
    while i<n:
        if fruits[i]=="apple":
            m.append(i)
        i+=1
    m.insert(0,len(m))

    return m
print(main(("apple","banana","apple","pear","apple")))