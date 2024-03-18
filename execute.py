import subprocess
import time
import os
import evaluation.evaluation as eval
#import hash as h

for i in range(1,2):
    if i == 0:
        model = "cc.en.300.bin cc.es.300.bin cc.de.300.bin cc.fi.300.bin cc.fr.300.bin cc.it.300.bin cc.nl.300.bin cc.pt.300.bin cc.pl.300.bin cc.tr.300.bin"
        c = str(0.5)
        n = str(3)
        l = str(25)
    if i == 1:
        model = "glove-twitter-200"
        c = str(0.5)
        n = str(3)
        l = str(8)
    if i == 2:
        model = "glove-wiki-gigaword-300"
        
        c = str(0.55)
        n = str(3)
        l = str(18)
    if i == 3:
        model = "word2vec-google-news-300"
        
        c = str(0.55)
        n = str(3)
        l = str(17)
    if i == 4:
        model = "fasttext-wiki-news-subwords-300"
        c = str(0.5)
        n = str(3)
        l = str(8)
    # if i == 5:
    #     model = "cc.it.300.bin"
    # if i == 6:
    #     model = "cc.nl.300.bin"
    # if i == 7: 
    #     model = "cc.pt.300.bin"
    # if i == 8:
    #     model = "cc.pl.300.bin"
    # if i == 9:
    #     model = "cc.tr.300.bin"
    
    # process_trainer = subprocess.Popen(["python","trainer.py","-tdata/train.txt","-c"+c,"-rhash_2try","-l"+l,"-n"+n,"-m"+model])
    # # #process_trainer = subprocess.Popen(["python","trainer.py","-tdata/Kiteforum_train_plain.txt","-c"+str(0.5),"-rhash_2try","-l"+str(8),"-n"+str(3),"-mcc.en.300.bin cc.es.300.bin cc.de.300.bin cc.fi.300.bin cc.fr.300.bin cc.it.300.bin cc.nl.300.bin cc.pt.300.bin cc.pl.300.bin cc.tr.300.bin"])
    # process_trainer.wait()
    # process_trainer.kill()
    # print("fertig")
    # # try:
    # #     os.remove("output.txt")
    # # except:
    # #     print("hash.txt")
    # output_file = open(str(i)+".txt","w")
    # # output_file = open("google_news_c5_maxlen18_ngram3.txt","w")
    # process = subprocess.Popen(["python","pcfg_guesser.py","-ssession2","-rhash_2try"], stdout=output_file,universal_newlines=True)
            
    # abbort = -1
    # x = 0

    # while x < 55000000:

        
                
    #             # if x < abbort:
    #             #     return 0

                
            
    #     x = 0
    #     try:
    #         file = open (str(i)+".txt","r")
    #         #content = file.read()
    #         for line in file:
    #              x+=1
    #         file.close()

    #                 # if x == abbort:
    #                 #     return 0
    #                 #abbort = x
    #         time.sleep(3)
    #     except:
            
            
    #         process.kill()
            
    
    # process.kill()
        
            


    # # h.has_list()
    eval.main("test.txt")
