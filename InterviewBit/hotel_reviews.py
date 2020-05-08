'''
Given a set of reviews provided by the customers for different hotels and a string containing “Good Words”, you need to sort the reviews in descending order according to their “Goodness Value” (Higher goodness value first). We define the “Goodness Value” of a string as the number of “Good Words” in that string.

Note: Sorting should be stable. If review i and review j have the same “Goodness Value” then their original order would be preserved.

You are expected to use Trie in an Interview for such problems

Constraints:

1.   1 <= No.of reviews <= 200
2.   1 <= No. of words in a review <= 1000
3.   1 <= Length of an individual review <= 10,000
4.   1 <= Number of Good Words <= 10,000
5.   1 <= Length of an individual Good Word <= 4
6.   All the alphabets are lower case (a - z)

Input:

S : A string S containing "Good Words" separated by  "_" character. (See example below)
R : A vector of strings containing Hotel Reviews. Review strings are also separated by "_" character.

Output:

A vector V of integer which contain the original indexes of the reviews in the sorted order of reviews. 

V[i] = k  means the review R[k] comes at i-th position in the sorted order. (See example below)
In simple words, V[i]=Original index of the review which comes at i-th position in the sorted order. (Indexing is 0 based)

Example:

Input: 
S = "cool_ice_wifi"
R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]

Output:
ans = [2, 0, 1]
Here, sorted reviews are ["cool_wifi_speed", "water_is_cool", "cold_ice_drink"]
'''

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def query(self,word):
        node = self.root
        for char in word:
            if not char.isalpha() :
                return 0
            node = node.next_node(char)
            if node is None :
                return 0
        return node.terminating
    
    def insert(self,word):
        node = self.root
        for char in word:
            if node.trieNodes[ord(char)-ord('a')] is None :
                node.trieNodes[ord(char)-ord('a')] = TrieNode()
            node = node.next_node(char)
        node.terminating = 1

class TrieNode:
    def __init__(self):
        self.terminating = 0
        self.trieNodes = [None]*26
    
    def next_node(self,char) :
        return self.trieNodes[ord(char)-ord('a')]

class Solution:
    # Store all the good words in a trie , trie is implemented here in a separate class .
    # Mistake i made at first was keeping count of occurence of words in trie , which will give wrong results here
    # just keep track when a word ends using terminating variable ( 1 for ending, 0 for non ending)
    # Then go through each review
    # each word in a review is queried on trie to see if there's a match or not , if there is increment goodness score
    # store the score,index pair in a list
    # sort list using score ( python inbuilt sort(timsort) is stable )
    # return the indexes from the pairs in the sorted list
    # time complexity : for search in trie of a word in worse case is O(m) ,total reviews * words per review * O(m)
    ,
    # optimization : instead of using python split() ,get the words using string manipulation in loop
    
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        trie = Trie()
        g_words = A.split('_')
        for g_word in g_words:
            trie.insert(g_word)
        R = []
        index = 0
        for review in B :
            g_score = 0
            words = review.split('_')
            for word in words:
                g_score += trie.query(word)
            R.append((g_score,index))
            index += 1
        R.sort(key = lambda x:x[0],reverse = True)
        return [x[1] for x in R]
