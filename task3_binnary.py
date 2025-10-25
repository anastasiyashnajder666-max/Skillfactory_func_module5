def binary_search(lst, target):
   if len(lst) == 0:
       return False
   else:
       midpoint = len(lst) // 2
       if lst[midpoint] == target:
           return True
       else:
           if lst[midpoint] < target:
               return binary_search(lst[midpoint+1:], target)
           else:
               return binary_search(lst[:midpoint], target)
