cnt=0 #for count of conversation
letter={}
word={}
'''maintaining letter and word count dictionary'''
while(1):
    ping=input("A :")
    if ping=='quit':# read the contineous input if ping is quite break
        break
    cnt+=1
    pong=input("B :")
    if pong=='quit':# read the contineous input if pong is quite break
        break
    # ping : "hi how are you"
    #pong :" i am fine"
    cnt+=1
    pinli=list(map(str,ping.split(" ")))#['hi','how','are','you']
    ponli=list(map(str,pong.split(" ")))#['i','am','fine']
    for i in range(len(pinli)):
        if pinli[i] not in word: #to store the count of words in word dict as{'hi':1,'how':1}
            word[pinli[i]]=1     #to store as key and and value
        else:
            word[pinli[i]]+=1
    for i in range(len(ponli)):#same as for pong in same dict stogage
        if ponli[i] not in word:
            word[ponli[i]]=1
        else:
            word[ponli[i]]+=1
    for i in range(len(pinli)):
        temp=list(pinli[i])      #to convert the list in to words['hi'] as ['h','i'] for word count 
        for i in range(len(temp)):
            if temp[i] not in letter:
                letter[temp[i]]=1
            else:
                letter[temp[i]]+=1
    for i in range(len(ponli)):
        temp=list(ponli[i])   #same as for pong
        for i in range(len(temp)):
            if temp[i] not in letter:
                letter[temp[i]]=1
            else:
                letter[temp[i]]+=1
n=0
while n!=4:
    print("1,to know the repitition character\n2,to know number of repitition words\n3,to know the length of conversation\n4,to Exit")
    n=int(input())
    if n==1:
        z=input("Enter the character :")
        if z in letter:
            print("{} : {}".format(z,letter[z]))  #count of letter not there 0
        else:
            print("{} : {}".format(z,0))  #if present print count
    elif n==2:
        z=input("Enter the word :")
        if z in word:
            print("{} : {}".format(z,word[z])) #for word count
        else:
            print("{} : {}".format(z,0))
    elif n==3:
        print("Count :",cnt)    #conver sation count
    elif n==4:
        print("Exit")
    else:
        print("Invalid")

    
            
