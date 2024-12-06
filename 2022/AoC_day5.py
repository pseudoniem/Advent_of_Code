AoC_input_stacks = '''                        [R] [J] [W]
            [R] [N]     [T] [T] [C]
[R]         [P] [G]     [J] [P] [T]
[Q]     [C] [M] [V]     [F] [F] [H]
[G] [P] [M] [S] [Z]     [Z] [C] [Q]
[P] [C] [P] [Q] [J] [J] [P] [H] [Z]
[C] [T] [H] [T] [H] [P] [G] [L] [V]
[F] [W] [B] [L] [P] [D] [L] [N] [G]
 1   2   3   4   5   6   7   8   9 '''

AoC_input_reaproc = '''move 2 from 2 to 8
move 2 from 1 to 6
move 8 from 7 to 1
move 7 from 5 to 4
move 1 from 6 to 4
move 1 from 6 to 3
move 6 from 3 to 5
move 9 from 8 to 1
move 3 from 6 to 7
move 14 from 4 to 1
move 6 from 1 to 7
move 16 from 1 to 9
move 6 from 1 to 4
move 1 from 8 to 6
move 4 from 1 to 5
move 11 from 9 to 7
move 2 from 1 to 8
move 1 from 6 to 7
move 1 from 8 to 7
move 1 from 8 to 3
move 7 from 4 to 3
move 14 from 7 to 6
move 8 from 6 to 9
move 19 from 9 to 2
move 1 from 1 to 2
move 2 from 9 to 7
move 9 from 7 to 8
move 2 from 2 to 8
move 16 from 2 to 9
move 4 from 8 to 2
move 1 from 7 to 9
move 3 from 9 to 6
move 3 from 3 to 6
move 11 from 9 to 2
move 7 from 5 to 3
move 2 from 5 to 9
move 6 from 6 to 4
move 1 from 6 to 4
move 4 from 6 to 8
move 5 from 9 to 1
move 4 from 1 to 7
move 3 from 2 to 6
move 3 from 4 to 1
move 1 from 4 to 1
move 2 from 1 to 3
move 4 from 3 to 7
move 1 from 5 to 2
move 3 from 1 to 6
move 15 from 2 to 5
move 3 from 6 to 3
move 13 from 3 to 8
move 2 from 4 to 2
move 9 from 5 to 4
move 2 from 2 to 5
move 5 from 7 to 5
move 10 from 8 to 6
move 1 from 2 to 5
move 10 from 4 to 6
move 4 from 8 to 6
move 3 from 7 to 1
move 3 from 1 to 9
move 1 from 2 to 1
move 8 from 5 to 2
move 3 from 6 to 9
move 6 from 8 to 5
move 6 from 9 to 2
move 1 from 1 to 9
move 10 from 2 to 1
move 4 from 8 to 5
move 10 from 5 to 9
move 11 from 9 to 7
move 5 from 7 to 9
move 1 from 9 to 2
move 3 from 2 to 9
move 2 from 2 to 8
move 4 from 9 to 5
move 4 from 1 to 9
move 5 from 5 to 2
move 5 from 1 to 4
move 21 from 6 to 9
move 3 from 2 to 9
move 2 from 8 to 1
move 25 from 9 to 6
move 4 from 5 to 7
move 1 from 4 to 6
move 6 from 6 to 4
move 3 from 4 to 6
move 7 from 7 to 3
move 4 from 9 to 1
move 3 from 7 to 8
move 2 from 9 to 8
move 2 from 2 to 8
move 4 from 1 to 3
move 9 from 6 to 2
move 13 from 6 to 4
move 13 from 4 to 5
move 1 from 5 to 8
move 2 from 2 to 3
move 6 from 5 to 3
move 19 from 3 to 6
move 1 from 4 to 9
move 2 from 8 to 1
move 5 from 2 to 3
move 5 from 1 to 9
move 7 from 5 to 4
move 1 from 8 to 3
move 1 from 2 to 6
move 8 from 6 to 3
move 1 from 9 to 8
move 11 from 4 to 2
move 1 from 4 to 6
move 1 from 2 to 8
move 5 from 3 to 4
move 4 from 9 to 6
move 1 from 6 to 8
move 9 from 3 to 1
move 7 from 2 to 9
move 1 from 2 to 6
move 3 from 1 to 8
move 2 from 2 to 3
move 3 from 9 to 7
move 3 from 4 to 7
move 2 from 4 to 3
move 2 from 3 to 5
move 8 from 6 to 4
move 6 from 8 to 6
move 2 from 9 to 4
move 5 from 8 to 6
move 3 from 7 to 5
move 1 from 5 to 8
move 1 from 8 to 2
move 1 from 5 to 1
move 11 from 4 to 9
move 2 from 6 to 3
move 2 from 2 to 4
move 6 from 1 to 2
move 6 from 2 to 1
move 3 from 7 to 3
move 2 from 4 to 7
move 4 from 6 to 5
move 7 from 3 to 7
move 5 from 9 to 6
move 22 from 6 to 8
move 2 from 6 to 5
move 2 from 8 to 4
move 14 from 8 to 7
move 11 from 7 to 4
move 3 from 8 to 1
move 9 from 7 to 8
move 10 from 1 to 4
move 1 from 7 to 4
move 4 from 8 to 7
move 6 from 4 to 9
move 7 from 4 to 1
move 3 from 4 to 8
move 1 from 5 to 8
move 8 from 5 to 3
move 4 from 3 to 9
move 7 from 8 to 9
move 3 from 8 to 3
move 2 from 8 to 2
move 7 from 9 to 1
move 2 from 2 to 8
move 8 from 9 to 1
move 8 from 1 to 7
move 7 from 1 to 5
move 7 from 7 to 1
move 11 from 9 to 8
move 9 from 8 to 5
move 2 from 8 to 5
move 3 from 1 to 8
move 2 from 3 to 7
move 6 from 4 to 1
move 6 from 1 to 6
move 5 from 7 to 1
move 2 from 4 to 6
move 1 from 3 to 5
move 4 from 7 to 4
move 2 from 8 to 7
move 10 from 5 to 6
move 9 from 6 to 1
move 8 from 1 to 6
move 1 from 7 to 2
move 9 from 6 to 4
move 2 from 4 to 3
move 3 from 8 to 1
move 1 from 2 to 4
move 4 from 4 to 1
move 7 from 4 to 3
move 3 from 3 to 2
move 1 from 7 to 6
move 9 from 6 to 7
move 6 from 7 to 4
move 2 from 7 to 2
move 6 from 4 to 7
move 2 from 2 to 9
move 1 from 2 to 4
move 1 from 7 to 4
move 4 from 7 to 6
move 4 from 5 to 4
move 1 from 2 to 5
move 1 from 7 to 5
move 1 from 2 to 6
move 6 from 4 to 3
move 9 from 3 to 9
move 4 from 6 to 2
move 7 from 3 to 8
move 22 from 1 to 7
move 1 from 1 to 7
move 2 from 8 to 3
move 4 from 5 to 6
move 2 from 3 to 2
move 6 from 2 to 8
move 3 from 8 to 6
move 1 from 4 to 8
move 1 from 1 to 8
move 8 from 6 to 7
move 7 from 8 to 9
move 22 from 7 to 4
move 3 from 5 to 6
move 1 from 8 to 1
move 2 from 8 to 2
move 3 from 6 to 4
move 1 from 1 to 3
move 15 from 9 to 1
move 5 from 1 to 5
move 3 from 7 to 6
move 5 from 5 to 6
move 4 from 4 to 3
move 6 from 6 to 9
move 7 from 7 to 6
move 5 from 6 to 7
move 4 from 1 to 9
move 3 from 7 to 4
move 2 from 9 to 7
move 5 from 3 to 5
move 3 from 6 to 3
move 5 from 4 to 6
move 10 from 9 to 5
move 1 from 2 to 9
move 1 from 3 to 5
move 1 from 2 to 9
move 3 from 1 to 6
move 2 from 9 to 2
move 7 from 6 to 5
move 15 from 4 to 9
move 2 from 4 to 5
move 1 from 3 to 4
move 9 from 9 to 1
move 1 from 9 to 2
move 2 from 9 to 4
move 11 from 5 to 4
move 1 from 9 to 3
move 1 from 6 to 8
move 4 from 7 to 8
move 4 from 8 to 9
move 15 from 4 to 7
move 1 from 6 to 7
move 1 from 3 to 7
move 6 from 9 to 6
move 1 from 3 to 7
move 1 from 2 to 1
move 1 from 9 to 5
move 3 from 6 to 1
move 11 from 1 to 4
move 6 from 5 to 1
move 2 from 2 to 5
move 1 from 5 to 7
move 2 from 6 to 1
move 7 from 5 to 7
move 3 from 5 to 6
move 4 from 6 to 1
move 11 from 4 to 3
move 1 from 8 to 5
move 23 from 7 to 6
move 18 from 6 to 9
move 1 from 5 to 9
move 1 from 4 to 2
move 3 from 3 to 7
move 3 from 3 to 8
move 17 from 1 to 8
move 5 from 6 to 5
move 2 from 7 to 1
move 20 from 8 to 2
move 4 from 7 to 2
move 3 from 9 to 5
move 7 from 9 to 7
move 6 from 9 to 2
move 1 from 1 to 8
move 3 from 9 to 4
move 7 from 5 to 2
move 6 from 7 to 1
move 1 from 1 to 8
move 3 from 2 to 6
move 1 from 7 to 6
move 2 from 8 to 9
move 35 from 2 to 4
move 3 from 3 to 2
move 1 from 5 to 7
move 2 from 3 to 9
move 3 from 1 to 6
move 2 from 2 to 1
move 32 from 4 to 7
move 3 from 4 to 8
move 3 from 9 to 5
move 1 from 1 to 2
move 21 from 7 to 5
move 2 from 2 to 1
move 3 from 1 to 2
move 15 from 5 to 1
move 3 from 6 to 7
move 3 from 4 to 6
move 3 from 8 to 5
move 1 from 9 to 3
move 8 from 7 to 2
move 6 from 5 to 2
move 9 from 1 to 6
move 4 from 7 to 1
move 2 from 5 to 4
move 2 from 4 to 3
move 3 from 5 to 4
move 17 from 2 to 7
move 3 from 3 to 5
move 2 from 4 to 8
move 1 from 4 to 3
move 5 from 7 to 9
move 1 from 3 to 6
move 4 from 1 to 7
move 4 from 6 to 7
move 2 from 5 to 2
move 1 from 1 to 3
move 10 from 6 to 4
move 1 from 3 to 7
move 20 from 7 to 8
move 8 from 4 to 8
move 1 from 2 to 8
move 4 from 9 to 1
move 3 from 7 to 4
move 2 from 4 to 9
move 2 from 6 to 3
move 1 from 2 to 8
move 1 from 7 to 6
move 1 from 9 to 5
move 3 from 5 to 9
move 4 from 9 to 2
move 1 from 4 to 5
move 1 from 5 to 3
move 3 from 2 to 4
move 1 from 9 to 7
move 1 from 2 to 1
move 1 from 7 to 1
move 11 from 1 to 2
move 3 from 1 to 7
move 25 from 8 to 5
move 1 from 6 to 3
move 1 from 6 to 2
move 7 from 8 to 2
move 9 from 2 to 8
move 2 from 4 to 7
move 2 from 5 to 7
move 2 from 5 to 2
move 5 from 5 to 1
move 7 from 5 to 1
move 2 from 4 to 9
move 3 from 5 to 6
move 1 from 1 to 8
move 1 from 5 to 6
move 1 from 4 to 7
move 1 from 9 to 2
move 3 from 5 to 2
move 2 from 6 to 9
move 3 from 9 to 8
move 1 from 5 to 4
move 3 from 3 to 9
move 10 from 1 to 5
move 4 from 2 to 8
move 2 from 6 to 1
move 3 from 9 to 7
move 1 from 1 to 9
move 1 from 4 to 3
move 1 from 9 to 2
move 9 from 8 to 2
move 2 from 3 to 7
move 2 from 7 to 6
move 3 from 5 to 6
move 4 from 8 to 6
move 4 from 8 to 3
move 4 from 3 to 2
move 4 from 6 to 8
move 1 from 7 to 9
move 2 from 1 to 8
move 2 from 8 to 3
move 1 from 9 to 2
move 13 from 2 to 4
move 6 from 5 to 7
move 2 from 5 to 7
move 10 from 2 to 4
move 11 from 7 to 8
move 1 from 6 to 4
move 4 from 6 to 7
move 24 from 4 to 9
move 11 from 7 to 4
move 1 from 3 to 8
move 1 from 3 to 5
move 4 from 4 to 2
move 5 from 4 to 2
move 9 from 2 to 5
move 4 from 9 to 5
move 1 from 5 to 1
move 2 from 5 to 7
move 2 from 2 to 5
move 1 from 1 to 7
move 2 from 2 to 3
move 18 from 9 to 6
move 9 from 8 to 1
move 2 from 9 to 5
move 5 from 1 to 8
move 2 from 8 to 7
move 4 from 8 to 4
move 5 from 8 to 7
move 10 from 5 to 1
move 10 from 7 to 4
move 4 from 5 to 8
move 14 from 1 to 9
move 6 from 9 to 8
move 1 from 5 to 1
move 12 from 6 to 9
move 4 from 6 to 8
move 11 from 8 to 5
move 1 from 6 to 1
move 19 from 9 to 7
move 2 from 3 to 5
move 13 from 7 to 5
move 3 from 7 to 1
move 4 from 8 to 9
move 2 from 7 to 6
move 7 from 4 to 8
move 5 from 8 to 1
move 1 from 1 to 3
move 1 from 7 to 2
move 6 from 1 to 6
move 1 from 2 to 5
move 1 from 8 to 1
move 1 from 8 to 2
move 2 from 4 to 8
move 5 from 6 to 1
move 2 from 4 to 7
move 2 from 9 to 6
move 1 from 6 to 5
move 4 from 6 to 2
move 1 from 9 to 5
move 2 from 4 to 5
move 4 from 2 to 4
move 2 from 8 to 3
move 3 from 3 to 2
move 4 from 1 to 2
move 2 from 4 to 7
move 4 from 2 to 3
move 4 from 1 to 2
move 13 from 5 to 1
move 1 from 6 to 2
move 1 from 1 to 8
move 15 from 5 to 2
move 4 from 3 to 1
move 5 from 4 to 3
move 1 from 3 to 6
move 1 from 8 to 7
move 1 from 9 to 8
move 1 from 7 to 8
move 3 from 3 to 2
move 1 from 8 to 2
move 1 from 3 to 7
move 13 from 1 to 4
move 3 from 5 to 3
move 1 from 1 to 2
move 1 from 8 to 5
move 5 from 7 to 2
move 1 from 6 to 5
move 2 from 3 to 4
move 10 from 2 to 5
move 1 from 9 to 5
move 3 from 1 to 8
move 3 from 8 to 3
move 11 from 4 to 5
move 12 from 2 to 8
move 4 from 4 to 7
move 10 from 8 to 5
move 2 from 8 to 1
move 1 from 7 to 3
move 1 from 7 to 9
move 5 from 3 to 7
move 1 from 9 to 4
move 7 from 7 to 6
move 13 from 5 to 8
move 6 from 6 to 7
move 5 from 7 to 4
move 1 from 6 to 4
move 2 from 4 to 9
move 1 from 7 to 9
move 3 from 4 to 3
move 1 from 3 to 6
move 4 from 5 to 7'''

def si_to_dict(input_stacks):
    x = input_stacks.split('\n') #split input op \n
    x[-1]=x[-1].split(' ') #split laatste regel op ' ', zodat alleen stapelnummers (en lege strings)
    
    #verwijder lege strings uit lijst met stapelnummers
    while True:
        try:
            x[-1].remove('') 
        except:
            break
    
    #maak int's van stapelnummers
    for i in range(len(x[-1])):
        x[-1][i] = int(x[-1][i])

    d={} #lege dictionary
    for i in range(len(x[-1])): #voor elk stapelnummer
        d[x[-1][i]] = []            #maak nieuwe lege lijst: d[stapelnummer]=[]
        for j in range(len(x)-1):   #voor elke regel uit input
            if x[j][4*i+1] != ' ':  #als element 4*stapelnr. +1 (daar staat letter) geen spatie is (dus letter is)
                d[x[-1][i]].append(x[j][4*i+1]) #voeg letter to aan d[stapelnummer]
        d[x[-1][i]].reverse()
    
    return d


# In[202]:


stapels = si_to_dict(AoC_input_stacks)


# In[203]:


print(stapels)


# In[ ]:





# In[204]:


#make list with rearangement procedure (turn "move x from y to z" into [x,y,z])
def reaproc_to_list(input_proc):
    x = input_proc.split("move ")
    x.remove('')
    x = x[0]
    x = x.split(" from ")
    x[-1] = x[-1].split(" to ")
    y = [int(x[0]), int(x[1][0]), int(x[1][1])]
    
    return y


# In[205]:


#Do alles (eindresultaat) #Wijzigt stapels!!
for l_line in AoC_input_reaproc.split('\n'):
    for i in range(reaproc_to_list(l_line)[0]):
        stapels[reaproc_to_list(l_line)[2]].append(stapels[reaproc_to_list(l_line)[1]].pop())

print(stapels)


# In[206]:


#Maak string met laatste letters van eindresultaat (antwoord)
answer = ""
for j in stapels.keys():
    answer += stapels[j][-1]

print(answer)


# In[189]:


#Do alles (eindresultaat) #Wijzigt stapels!!
for l_line in AoC_input_reaproc.split('\n'):
    dummie = []
    for i in range(reaproc_to_list(l_line)[0]):
        dummie.append(stapels[reaproc_to_list(l_line)[1]].pop())
       #print(dummie)
    dummie.reverse()
    stapels[reaproc_to_list(l_line)[2]].extend(dummie)

print(stapels)


# In[190]:


#Maak string met laatste letters van eindresultaat (antwoord)
answer = ""
for j in stapels.keys():
    answer += stapels[j][-1]

print(answer)

