dna_string='TCAATGCATGCGGGTCTATATGCAT'
#print(dna_string_reverse)
def swapping(ncs, n1, n2):
    ncs = ncs.replace(n2, '!',)
    ncs = ncs.replace(n1, n2)
    ncs = ncs.replace('!', n1)
    return ncs
def palindrom(dna_string):
    dna_string_reverse=dna_string[::-1]
    dna_string_reverse=swapping(dna_string_reverse,'C','G')
    dna_string_reverse=swapping(dna_string_reverse,'A','T')
    list_matched_substrings=[]
    positions=[]
    len_of_substrings=[]
    for i in range(len(dna_string)):
        for k in range(len(dna_string_reverse)):
            for l in range(k+4,len(dna_string)):
                for j in range(4,13,2):
                    if dna_string[i:i+j]==dna_string_reverse[k:l]:
                        if dna_string[i:i+j] not in list_matched_substrings and len(dna_string[i:i+j])% 2 == 0:
                           list_matched_substrings.append(dna_string[i:i+j])
                           positions.append(dna_string.find(dna_string[i:i+j])+1)
                           len_of_substrings.append(len(dna_string[i:i+j]))
    return positions,len_of_substrings
print(palindrom(dna_string))
tuple_of_lists_of_2_outputs=palindrom(dna_string)
import pandas as pd
df=pd.DataFrame(list(tuple_of_lists_of_2_outputs))
df_t=df.T
df_t.rename(columns={0: '', 1: ''}, inplace=True)
print(df_t.to_string(index=False))

                       

                       
