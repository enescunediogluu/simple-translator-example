LAB5 Quiz
Assoc. Prof. Dr. Hacer YALIM KELEŞ
Date: 27/11/2020 – 03/12/2020
Write a Python program which takes a sequence of inputs that contain some English-Turkish word pairs and some query items. Input data will contain a number of word pairs, i.e. M_WORDS, at the beginning and then followed by word pairs in the order of English:Turkish. After that, a query string, which contains language option to translate to, i.e. TR or EN, and a set of words will be provided.
Write a program that searches given words from the given dictionary and translates the words in the query items and prints them in alphabetical order. It is expected that your program will be able to translate both from Turkish to English and from English to Turkish. Program details and the output format is specified below. Please also look at the sample I/O files.
Specification details:
- You can assume that there will be at least one word pair in the dictionary and one word in the query string.
- Each word pairs will be provided in different lines.
- If the query string starts with “EN”, then your program is expected to translate the given words into English, if starting with “TR”, then it is expected to translate them into Turkish.
- Sometimes the same word can be searched more than once in the query. In this case, do not print and count duplicate words.
- When printing the words which has meaning in the dictionary, you must first print the searched language, then the translated language. You should print these pairs in alphabetical order according to the searched language.
- If the query contains words that do not have meaning in the dictionary, print the total number of not found words and the list of these words in alphabetical order.
- A word can be written more than once in both languages. If these word are searched in query, you must print the last word in the dictionary. For example little:kucuk, small:kucuk are given in the dictionary. The word "kucuk" was asked in input 1. Because "small" is the last word in the dictionary, in the output1 it is printed as "small".