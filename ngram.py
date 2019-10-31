#!/usr/bin/env python
# coding: utf-8



import os
import datetime
import re
from nltk import sent_tokenize
from nltk import word_tokenize
import re
import pandas as pd  
from nltk.corpus import stopwords
import string 
import sys
root_dir="C://Users//r-naveenj//Desktop//tasks//temp//"
stopword_set = set(stopwords.words("english"))    





#common set of functions and preprocesssing for all tasks 
def read_file(fileName): #reading file 
    input_file = open(fileName,'r+')
    return input_file.read()
def sent_split(input_file):# sentence tokenization
    sentence = read_file(input_file) #calling the readfile_fuction
    return sent_tokenize(sentence)
def remove_whitespace(text): #function to remove white space
    return  " ".join(text.split()) 
def remove_punctuation(text): #function removing punctuation
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator) 
def sent_normalize(text):# sentence normalization function
    #text=list_text(text)
    text = remove_punctuation(text)
    text = remove_whitespace(text)
    return text





class Ngramfiles():  #Ngram class
    def __init__(self, dirname,ngram_value):
        self.dirname = dirname
        self.ngram_value = ngram_value

    def main(self):#main function
        for (root, dirs, files) in os.walk(self.dirname):   
            for file in  files:
                try:
                    page_NO=""
                    ngrams=""
                    folder_name=""
                    sentence_id=0
                    empty="1.txt"
                    first_file=files[0]
                    if file.endswith('.txt'):
                        page_NO=str(file.replace('.txt',''))
                        folder_name=os.path.basename(os.path.normpath(root))   
                        #break
                        each_file=self.dirname+folder_name+"//"+file
                        splited_sentences = sent_split(each_file) #sentence tokennize function calling
                        #wring flies specific to the folder 
                        writeFile = open(self.dirname+folder_name+"//"+"Ngram_output"+"--"+str(folder_name)+".tsv", 'a')
                        if file==first_file:
                            writeFile.write("folder_name"+"\t"+ "page_NO"+"\t"+"sentence_id"+"\t"+"Ngram"+"\t"+"\n")

                        for each_sentence in splited_sentences:
                            each_sentence=sent_normalize(each_sentence)
                            ngrame_sent=self.extract_ngrams(each_sentence,self.ngram_value)
                            if ngrame_sent!=[]: #removing null values n grams 
                                sentence_id+=1 #sentence id generation
                                writeFile.write(folder_name+"\t"+page_NO+"\t"+str(sentence_id)+"\t"+str(ngrame_sent)+'\n')
                        #else:
                            #pass
                        writeFile.close()    
                except:
                    ngram_value="ERROR in input"    


    def extract_ngrams(self,document,ngram_value):   #code for Ngram generation
        #print(document)
        if(ngram_value > 1 and ngram_value< 7): #defining N-gram range
         #Get the words in the document
            document = re.sub(r"\s+", r" ", document) #preprocessing
            document= re.sub("[^a-zA-Z0-9]", " ", document)#preprocessing
            words = word_tokenize(document)
            #lower casing ans stop word removal
            words_filtered = [word.lower() for word in words if word.lower() not in stopword_set and len(word) >= 2]
            ngrams=[]
            for count in range(0,len(words_filtered)-(ngram_value-1)):
                ngram = " ".join(words_filtered[count:count+ngram_value])
                ngrams.append(ngram)
            return ngrams
        else:
            print("please enter ngram_value betweeen 2 and 6 ")
if __name__ == "__main__":# main function calling
    objName = Ngramfiles(root_dir,2)#Ngramfiles(sys.argv[0],sys.argv[1])
    objName.main() 
    





