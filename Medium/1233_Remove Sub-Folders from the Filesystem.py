class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        def is_subfolder(parent, child):
            # Check if child is a subfolder of parent
            if not child.startswith(parent):
                return False
            return len(child) > len(parent) and child[len(parent)] == '/'
        
        folder.sort()  
        result = []      
        for f in folder:
            # Add folder if result is empty or current folder is not subfolder of last added folder
            if not result or not is_subfolder(result[-1], f):
                result.append(f)
        
        return result

s = Solution()
print(s.removeSubfolders(["/a","/a/b/c","/a/b/d"]))