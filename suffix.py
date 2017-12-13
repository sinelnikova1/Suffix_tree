import twitter
import os.path
import suffix_tree
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

sys.setrecursionlimit(100000)
if not os.path.exists("Output.txt"):
    api = twitter.Api(consumer_key='CqEaH5DYazS7EWnPXWKfx7uBi',
                      consumer_secret= 'JaMUAdm0oMGBwnJNk0m1TxAnIPSva3wh5jWV1OSyFuRAxQvchw',
                      access_token_key= '455872244-dmZiMi7NmPpm4vmYMoAN9q45VFwaOj7IspKwrIpg',
                      access_token_secret='jAg09eFhw1KLSbQ0JyjNCE3qeicJng90bo2zcMXgl6CPE')

    api.VerifyCredentials()
    statuses = api.GetUserTimeline(screen_name='rihanna')
    messages = [i.text for i in statuses];
    text_file = open("Output.txt", "w", encoding='utf-8');

    for message in messages:
        print (message.translate(non_bmp_map))
        text_file.write("%s\n" % message.translate(non_bmp_map))
    text_file.close()

text_file = open("Output.txt", "r", encoding='utf-8');
all_message = ''.join([i for i in text_file.readlines()])
print (all_message)
text_file.close()
tree = suffix_tree.SuffixTree(all_message)
print('Longest Repeated Substring:"%s"'%(tree.longest_repetable_substring()))
print('Most frequent Repeated Substring:"%s"'%(tree.most_frequently_string()))

##tree = suffix_tree.SuffixTree("THIS IS A TEST TEXT")     # Пример
##for i in ["T","THIS","TEST","A"," ","IS A",'TEST1','THIS IS GOOD', "THIS IS A TEST TEXT"]:   #Проверка на подстроки
##   print('indexes for "%s":%s'%(i,tree.search(i)))
##
### тесты для самых длинных повторяющихся подстрок и для самы частых повт. подстрок
##tests=["GEEKSFORGEEKS$", "AAAAAAAAAA$", "ABCDEFG$", "ABCDEFG$", "ABABABA$", "ATCGATCGA$", "banana$", "abcpqrabpqpq$", "pqrpqpqabab$"]
##
### ответы для самой длинной повт. подстроки, не используются при проверке. P.s. в последнем тесте 2 возможных ответа ab и pq
##answers=["GEEKS","AAAAAAAAA","","ABABA","ATCGA","ana","ab","pq"]
##
##for i in tests:  #для каждого теста
##   tree=suffix_tree.SuffixTree(i)  #строим суффиксное дерево
##   print('Longest Repeated Substring in "%s":"%s"'%(i,tree.longest_repetable_substring())) 
##  ##   
##   print('Most frequent Repeated Substring "%s":"%s"'%(i,tree.most_frequently_string()))
##   print('====')


    
