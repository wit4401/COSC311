"""
COSC 311 Lab 1

The attached is a Science paper (.txt file) published in Feb. 9, 2023. Write a Python program 
to analyze this paper and answer the following questions.
"""
# open the file for read only purposes
science_text=open("SciencePaper.txt","r")

# create a dictionary for to analyze the file
words={}
new_line=science_text.readline()
while new_line!="":
    for word in new_line.split():
        try:
            words[word]+=1
        except:
            words[word]=1
    new_line=science_text.readline()
"""
Task 1: How many different words appeared in this paper?
"""
print("Task 1:")
print('Number of Unique "Words":',len(words),"\n")

"""
Task 2: What are the 10 words that appear most frequently (from high to low)? 
"""
print("Task 2:")
print("Top 10 Most Frequent Words:")
it=10
for i in sorted(words.items(),key=lambda x: x[1])[-10:]:
    print(it,end=". ")
    print(str(i[0])+" ("+str(i[1])+")")
    it-=1
print()

"""
Task 3: What are the appearance frequencies for the following words?
    - Summerfelt 
    - wastewater
    - greenhouse 
    - salmon
"""
print("Task 3:")
print("Appearence of Summerfelt: ",words['Summerfelt'])
print("Appearence of wastewater: ",words['wastewater'])
print("Appearence of greenhouse: ",words['greenhouse'])
print("Appearence of salmon: ",words['salmon'],'\n')

"""
Task 4: What are the words appear exactly 1 time, 2 times, 5 times, and 10 times, respectively?
"""
print("Task 4:")
print("Word Appeared 1 time:")

print("Found 1 time","("+str(len(once))+"):")
print(*[i for i in words if words[i]==1],sep=', ')
print()

print("Found 2 times","("+str(len(twice))+"):")
print(*[i for i in words if words[i]==2],sep=', ')
print()

print("Found 5 times","("+str(len(five))+"):")
print(*[i for i in words if words[i]==5],sep=', ')
print()

print("Found 10 times","("+str(len(ten))+"):")
print(*[i for i in words if words[i]==10],sep=', ')
print()

"""
Task 5: Draw a bar figure to show the average length of words for each appearance frequency.
"""
import numpy as np # import numpy
import matplotlib.pyplot as plt #import matplotlib
print("Task 5:\nOutput pending...")
wlist={}
for word,count in words.items():
    try:
        wlist[count].append(word)
    except:
        wlist[count] = [word]

num_words = [len(value) for value in wlist.values()]
avg_len = [sum([len(word) for word in value]) / len(value) for value in wlist.values()]
plt.bar(list(wlist.keys()),avg_len)
plt.show()