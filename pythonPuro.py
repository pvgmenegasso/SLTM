#------------------------------------------------------------------------------------------------------------
# programa que realiza o pre processamento de um arquivo repbase, separando o conteúdo em dois vetores
# um deles (arrays) contém as sequencias e tem o formato arrays[sequencia][basenasequencia][valordabase] 
# o outro vetor (arrayc) armazena a classificação das sequencias, e é do formato 
# arrayc[classificacao][valordaclassificacao]. As bases estão codificadas da seguinte forma:
# A - 1000   C - 0100  T - 0010  G - 0001   (conforme sugerido pelos resultados de: 
# https://www.researchgate.net/publication/298860781_FEATURE_REPRESENTATION_OF_DNA_SEQUENCES_FOR_MACHINE_LEARNING_TASKS )
# as classificacoes foram mapeadas como se segue:
# jockey -10000000000000000000  copia -01000000000000000000  gypsy -00100000000000000000  
# pao -00010000000000000000  rte -00001000000000000000  l1 -00000100000000000000  
# trna -00000010000000000000  7sl -00000001000000000000  
# 5s -00000000100000000000  tcmar -00000000010000000000  hat -00000000001000000000
# mutator -00000000000100000000  merlin -00000000000010000000  transib -00000000000001000000  
# piggybac -00000000000000100000  pif-harbinger -00000000000000010000  cacta -00000000000000001000  
# r2 -00000000000000000100  ltr -0000000000000000001  outros -00000000000000000001
#------------------------------------------------------------------------------------------------------------

# importa as bibliotecas necessárias
import numpy as np


# declara as variáveis que serão utilizadas
# string auxiliar que armazenará as classificações
classification = ''
# string auxiliar que armazenará as sequencias
sequence =  ''
# nome do arquivo a ser aberto para preprocessamento
doc_name = 'repbase.fasta'
# numero maximo de bases nas sequencias
tam_seqs = len(max(open(doc_name, 'r'), key=len))

# nao usado (ainda)
tam_batch = 20

# le o documento e adiciona as classificações na variável
for s in open(doc_name,'r').readlines() :
    if s.startswith('>'):
        classification += s[s.find("|")+1:-1]
        classification += '\n'

# le o documento e adiciona as sequencias na variável
for s in open(doc_name, 'r').readlines() :
    if not s.startswith('>'):
         sequence += s[:-1]
         sequence += '\n'


# separa as classificações em array
classification = classification.split('\n')

# imprime para teste
print(sequence)

print(classification)


# define o numero de linhas do documento
num_lines = sum(1 for line in open(doc_name))

# inicializa os vetores np das sequencias e classificações
arrays = np.zeros(shape=((int)(num_lines/2), tam_seqs, 4))
arrayc = np.zeros(shape=((int)(num_lines/2), 20))
  
# declara variaveis auxiliares
x = 0
y = 0

#percorre as sequencias e faz a transferencia da variável sequence para o vetor np arrays
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

#percorre as sequencias e faz a transferencia da variável classification para o vetor np arrayc
        
for a in range((len(classification) - 1 )):
    
    if classification[a] == 'jockey':
        arrayc[a] += np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'copia':
        
        
            arrayc[a] += np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'gypsy':
        
        
            arrayc[a] += np.array([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'pao':
        
        
            arrayc[a] += np.array([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'rte':
        
        
            arrayc[a] += np.array([0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'l1' :
        
        
            arrayc[a] += np.array([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'trna':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == '7sl':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == '5s':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'tcmar':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'hat':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'mutator':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0])
        
    elif classification[a] == 'merlin':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
        
    elif classification[a] == 'transib':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
        
    elif classification[a] == 'piggybac':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
        
    elif classification[a] == 'pif-harbinger':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0])
        
    elif classification[a] == 'cacta':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
        
    elif classification[a] == 'r2':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0])
        
    elif classification[a] == 'ltr':
        
        
            arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
        
    else:
        
        arrayc[a] += np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

#mostra como tam_batch poderia ser usado 
print(arrays[:,:-(tam_seqs-tam_batch)])
print(arrayc)
    
    

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
    
    
