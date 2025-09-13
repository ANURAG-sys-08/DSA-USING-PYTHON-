# CHECK WHETHER A ARRAY IS SORTED OR NOT USING RECURSION

# def checksorted(l1):
#     if (len(l1)==0 or len(l1)==1):
#         return True
#     else:
#         return False
    
#     ans = checksorted(l1[1:])

#     if (l1[0]<l1[1]):
#         return True
#     else:
#         return False

#  MORE CORRECT AND EFFICIENT ANSWER

def checksorted(l1):
    if (len(l1)==0 or len(l1)==1):
        return True
    if (l1[0]>=l1[1]):
        return False
    return checksorted(l1[1:])

