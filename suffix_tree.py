class SuffixTreeNode:     
    def __init__(self, level):   
        self.children = []       
        self.chars = []             
        self.indexes = []        
        self.level = level;      
        
    def insertSuffix(self, suffix, index, level):        
        self.indexes.append(index)       
        if len(suffix) > 0:  
            try:
               char_position = self.chars.index(suffix[0]) 
               self.children[char_position].insertSuffix(suffix[1:],index+1,level+1) 
            except ValueError:
                self.children.append(SuffixTreeNode(level+1))  
                self.chars.append(suffix[0])  
                self.children[-1].insertSuffix(suffix[1:],index+1,level+1) 
   
    def search(self, text):      
        if len(text) == 0:       
            return self.indexes  
        try:                     
            char_position = self.chars.index(text[0])  
            return self.children[char_position].search(text[1:])  
        except ValueError:  
            return []       

    def longest_repetable_substring(self,results):    
        if len(self.children) > 1 and results[0].level < self.level:  
            results.pop()           
            results.append(self)    
        for i in self.children:     
            i.longest_repetable_substring(results)
        return results              

    def leaf_count(self):          
        if (len(self.children) == 0): return 1;    
        return sum([i.leaf_count() for i in self.children]) 
        

class SuffixTree:    
    def __init__(self, text):
        self.root = SuffixTreeNode(0)     
        self.text = text      
        for i in range(0, len(text)):    
            self.root.insertSuffix(text[i:],i,0) 
        

    def search(self,text):          
        return [i - len(text) for i in self.root.search(text)]   

    def isSubstring(self,text):        
        return len(self.search(text)) != 0 

    def longest_repetable_substring(self):     
        result_children = self.root.longest_repetable_substring([self.root])[0]    
        return self.text[result_children.indexes[0]-result_children.level:result_children.indexes[0]]   

    def most_frequently_string(self):     
        result_children = max(self.root.children,key=self._node_leaf); 
        while(len(result_children.children) == 1):  
            result_children = result_children.children[0]
        return self.text[result_children.indexes[0]-result_children.level:result_children.indexes[0]] 

    def _node_leaf(self,node):  
        return node.leaf_count()
