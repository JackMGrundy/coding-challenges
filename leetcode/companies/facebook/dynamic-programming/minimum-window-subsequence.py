"""
"""
def minWindow(S, T):
    """
    :type S: str
    :type T: str
    :rtype: str
    """
    n = len(S)
    m = len(T)
    
    dic = dict()
    for i, s in enumerate(T):
        # print(i, s, dic)
        dic.setdefault(s, []).append(i)
    # print(dic)

    dp = [-1 for i in range(m)]
        
    count = n+1
    start = -1

    print(dic, dic['b'][::-1])

    # for index, c in enumerate(S):
        # if c in dic:
            # for i in dic[c][::-1]:

S = "abcdebdde"
T = "bdbe"
minWindow(S, T)