#==============================================================================
#FIND START OF REFERENCE LIST
#==============================================================================

# import relevant modules and data
#==============================================================================
from csv import reader

ref_list=[]
doc_sent=[]

#load and loop through data
with open('./input/sentences_nlp352','r') as fid:
    for r in fid:
        #file is table delimited
        row=r.replace('\n','').split('\t')
        #first three items are integers/strings        
        docid=row[0]
        sentid=row[1]
        tmp=row[2:]

        #the rest are comma-delimited lists
        wordidx=[l for l in reader([tmp[0][1:-1]])][0]
        wordidx=[int(w) for w in wordidx]
        words=[l for l in reader([tmp[1][1:-1]])][0]
        poses=[l for l in reader([tmp[2][1:-1]])][0]
        ners=[l for l in reader([tmp[3][1:-1]])][0]
        lemmas=[l for l in reader([tmp[4][1:-1]])][0]
        dep_paths=[l for l in reader([tmp[5][1:-1]])][0]
        dep_parents=[l for l in reader([tmp[6][1:-1]])][0]
        dep_parents=[int(d) for d in dep_parents]

        #build list of target occurences for this document
        targets = []
    
        #sentence string
        sent = ' '.join(words)
    
        #REF ID LOGIC: is the first word in a sentence 'References'?
        if words[0]=='References' or words[0]=='REFERENCES':
            ref_list.append([docid,sentid])
        
        #REF ID LOGIC: is the first word in a sentence 'Bibliography'?
        if words[0]=='Bibliography' or words[0]=='BIBLIOGRAPHY':
            ref_list.append([docid,sentid])
        
        #REF ID LOGIC: is the first word in a sentence French for 'Bibliography'?
        if words[0]=='Bibliographie' or words[0]=='BIBLIOGRAPHIE':
            ref_list.append([docid,sentid])

        #REF ID LOGIC: is there an all capitalized 'REFERENCES' in words array?
        if 'REFERENCES' in words:
            ref_list.append([docid,sentid])
            
        #REF ID LOGIC: is the word 'Acknowledgements' in words array?
        if 'Acknowledgements' in words or 'Acknowledgments' in words or 'ACKNOWLEDGEMENTS' in words or 'ACKNOWLEDGMENTS' in words:
            ref_list.append([docid,sentid])
      
        #list of docid-sentid tuples
        doc_sent.append([docid,sentid])
        
#list of unique docids
doc_list=list(set(a[0] for a in doc_sent))
sent_list=[]

#find max sentid for each unique docid
for d in doc_list:
    sent_list.append(max([int(a[1]) for a in doc_sent if a[0]==d]))
    
#zip together docid and sentid lists
doc_sent=zip(doc_list,sent_list)

#build list of 'buest guess' reference section start
final_ref_list=[]
for d in doc_sent:
    #default guess is that reference list starts at last sentence
    final_ref_list.append([d[0],str(d[1])])
    
    #list of all candidate reference starts
    tmp_refs=[a for a in ref_list if a[0]==d[0]]
    
    if tmp_refs:
        #unique list of candidate sentids
        bounds=list({int(a[1]) for a in tmp_refs})
        #sort them into descending order
        bounds.sort()

        #find "shallowest" candidate
        for b in bounds:
            #however, must be more than 25% of the way through the doc (arbitrary cut-off)
            if float(b)/float(d[1])>=0.25:
                final_ref_list[-1][1]=str(b)
                break

#write the output as tab-separated values
with open('./output/ref_start.tsv', 'w') as f:
    f.write('\n'.join(['\t'.join(frl) for frl in final_ref_list]))