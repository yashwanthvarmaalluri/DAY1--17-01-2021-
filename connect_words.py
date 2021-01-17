#User function Template for python3

#I have done this problem after watching your explaination video sir.Instead of storing neighbours indexes i have directly stored neighbours

def distance(s1,s2):
    different=0
    for i in range(len(s1)):
        if(s1[i]!=s2[i]):
            different+=1
    return different==1
def WordLadderLength(start, target, D):
    if target not in D:
        return 0
    if start not in D:
        D.append(start)
    friends={}
    visited={}
    for i in D:
        friends[i]=set()
        visited[i]=False
    for i in range(len(D)):
        for j in range(i+1,len(D)):
            if(distance(D[i],D[j])):
                friends[D[i]].add(D[j])
                friends[D[j]].add(D[i])
    queue=[]
    ans=1
    queue.append(start)
    while(len(queue)!=0):
        ans+=1
        temp=set()
        for i in range(len(queue)):
            word=queue.pop(0)
            for j in friends[word]:
                if target==j:
                    return ans
                if visited[j]==False:
                    queue.append(j)
                    temp.add(j)
            for _ in temp:
                visited[_]=True
    return 0
