import numpy as np

classification = ''
sequence =  ''
doc_name = 'repbase.fasta'
tam_seqs = len(max(open(doc_name, 'r'), key=len))
tam_batch = 20


for s in open(doc_name,'r').readlines() :
    if s.startswith('>'):
        classification += s[s.find("|")+1:-1]
        classification += '\n'

for s in open(doc_name, 'r').readlines() :
    if not s.startswith('>'):
         sequence += s[:-1]
         sequence += '\n'



classification = classification.split('\n')

print(sequence)

print(classification)

num_lines = sum(1 for line in open(doc_name))


arrays = np.zeros(shape=((int)(num_lines/2), tam_seqs, 4))
arrayc = np.zeros(shape=((int)(num_lines/2), 4))
  
x = 0
y = 0

for a in range(len(sequence)):
    
    if sequence[a] == 'A':
        arrays[x][y] += np.array([1,0,0,0])
        y += 1

    if sequence[a] == 'C':
        arrays[x][y] +=np.array([0,1,0,0])
        y += 1

    if sequence[a] == 'T':
        arrays[x][y] +=np.array([0,0,1,0])
        y += 1

    if sequence[a] == 'G':
        arrays[x][y] +=np.array([0,0,0,1])
        y += 1
 
    if sequence[a] == '\n':
        x += 1
        y = 0

for a in range(len(classification)):
    
    if classification[a] == 'jockey':
        arrayc[a] += np.array([1,0,0,0])

    if classification[a] == '7sl':
        arrayc[a] += np.array([0,1,0,0])
    


print(arrays[:,:-(tam_seqs-tam_batch)])
print(arrayc)
    
    
