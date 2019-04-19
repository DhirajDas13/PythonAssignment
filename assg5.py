f=open("input.txt","r+")
s=f.read()
l=s.split("\n")

outfile=open("output.txt","w+")

outfile.write(str("Count of words per line: \n"))

word_list=[]
for i in l:
    i=i.strip()
    word_list=i.split(" ")
    outfile.write(str (len(word_list)) + "\n")

outfile.write(str("Count of letters per line: \n"))

word_count=0
for i in l:
    i=i.strip()
    word_list=i.split(" ")
    word_count=0
    for j in word_list:
        word_count= word_count + len(j)
    outfile.write(str(word_count) + "\n")

f.close()
