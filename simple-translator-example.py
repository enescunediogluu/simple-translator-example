numOfPairs = int(input())

eng2tr = {}

for i in range(numOfPairs):
    str1 = input()
    list1 = str1.split(":")
    eng2tr[list1[0]] = list1[1]

tr2eng = {}

keys = list(eng2tr.keys())
values = list(eng2tr.values())

for i in range(len(keys)):
    tr2eng[values[i]] = keys[i]

sentence = input()  
sentence =  sentence.split(" ")

sentenceLast = []
for item in sentence:
    if sentence.count(item) == 1:
        sentenceLast.append(item)

    elif sentence.count(item) > 1:
        if sentenceLast.count(item) == 0:
            sentenceLast.append(item)

mistake_count = 0

result_sentence = []
wrong_words = []

for i in range(1,len(sentenceLast)):
    try:
        if sentenceLast[0] == "TR":
            result = eng2tr[sentenceLast[i]]
            result_sentence.append((sentenceLast[i],result))
        
        if sentenceLast[0] == "EN":
            result = tr2eng[sentenceLast[i]]
            result_sentence.append((sentenceLast[i],result))

    except Exception:
        wrong_words.append(sentenceLast[i])
        mistake_count += 1

result_sentence = sorted(result_sentence)
wrong_words = sorted(wrong_words)
wrong_words = " ".join(wrong_words)

if mistake_count == 0:
    for i in range(len(result_sentence)):
        print(f"{result_sentence[i][0]}={result_sentence[i][1]}")

else:
    for i in range(len(result_sentence)):
        print(f"{result_sentence[i][0]}={result_sentence[i][1]}")
    
    print(f"{mistake_count} word not found: {wrong_words}")

