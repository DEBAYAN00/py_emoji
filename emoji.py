words= input("> ")
words1= words.split(' ')
emoji={
":)":"😄",
":]":"😁",
"X]":"😆",
"XD":"😂",
":-@":"🧐",
":(":"😫",
":%":"😖"
}
op=""
for w in words1:
    op += emoji.get(w,w)+ " "
print("\n",op)