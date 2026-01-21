#There are N people standing in a circle waiting to be executed. 
# The counting out begins at some point in the circle and proceeds around the circle in a fixed direction. 
# n each step, a certain number of people (K) are skipped and the next person is executed. 
# The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, 
# who is given freedom. 

#TIP: When we have something like circular fashion use % operator to wrap around the index.


def josephus_problem(n,k):
    index=0
    if len(n) == 1:
        return n[0]
    while len(n) > 1:
        index = (index + k) % len(n)
        n.pop(index)
        print("people left:", n)
    return n[0]




n = 7
k = 3 #k-1 are skipped and next is executed because we are using 0-based indexing

people=[]
for i in range(1,n+1):
    people.append(i)
print("people", people)
print("who is given freedom:", josephus_problem(people,k-1))