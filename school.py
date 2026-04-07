#name = "Ebuka"
#lastname = "Okereke"
#print(name+lastname)

#name = input("my name is :")
#print(name)

#age = int(input("I am :"))
#print(age)

#amt = float(input("how much is bag of rice?"))
#print(amt)

#GOAT = bool(input("Is Ronaldo the goat?"))
#print(GOAT)

#name = 200
#name += name
#print(name)            

#GOAT = "ronaldo"
#user_choice = input("Who is the GOAT ?")
#is_goat = (user_choice == GOAT)
#if is_goat: print("TRUE")
#else: print("FALSE")

#age = 19
#if age >= 90:
#    print("VERY OLD")
#elif age >= 50:
#    print('mid age')
#elif age >= 30:
#    print('adult')
#elif age >= 20:
#    print('teen')
#else:
#    print('child')                        

#try:
#    num_str = "abc"
#    num = float (num_str)
#    print (f"Converted number: {num}")
#except ValueError:
#    print(f"ERROR: Could not convert '{num_str}'to a float")    

#fruits = ['coconut','pineapple','mango','apple','orange','banana']
#for f in fruits:
#    print(f"i love {f}")

#arr = [4,8,9,7,6,12] # list [0,1,2,3,4,5]

#def b_sort (arr):
#    n = len(arr)
#
#    for i in range(n):
#        swapp = False

#        for j in range(0, n-i-1):
#            if arr[j] > arr[j + 1]:
#                temp = arr[j]
#                arr[j] = arr[j + 1]
#                arr[j+1] = temp
#                swapp = True 
#        if not swapp:
#            break
#    return arr           


#ll = b_sort(arr)
#print(ll)


#arr = [64,34,25,12,22,11,90]               
#def b_sort (arr):
#    n = len(arr)

#    for i in range(n):
#        swapp = False
#        for j in range(0, n-i-1):
#            if arr[j] < arr[j + 1]:
#                temp = arr[j]
#                arr[j] = arr[j + 1]
#                arr[j+1] = temp
#                swapp = True 
#        if not swapp:
#            break
#    return arr           


#ll = b_sort(arr)
#print(ll)

#my_list = [5,1,4,2,8]
#def insertion_sort(arr):
#    for i in range(1, len(arr)):
#        key = arr[i]
#        j = i - 1
       #key = 1
       #j = 0
       #arr[j]= 5
       #arr[j+1] = 1
       #arr[j+1] = arr[j] = 5 
#        while j >= 0 and key < arr[j] :
#            arr[j+1] = arr[j]
#            j -= 1
#            print(j)
#        arr[j+1] = key
#    return arr
#ll = insertion_sort(my_list)
#print(ll)



#fruit_list = ["banana","mango","apple","pineapple","cherry"]  
#def insertion_sort(arr):
#    for i in range(1, len(arr)):
#        key = arr[i]
#        j = i - 1
#        while j >= 0 and key < arr[j] :
#            arr[j+1] = arr[j]
#            j -= 1
#            print(j)
#        arr[j+1] = key
#    return arr
#ll = insertion_sort(fruit_list)                                                                                                                 
#print(ll)



#arr = [43,41,23,57,45,12]

#def selection_sort(arr):
#    for i in range(len(arr)):
#        print(i)
#        min_idx = i
#        for j in range(i + 1, len(arr)):
#            if arr [min_idx] > arr [j]:
#                arr[min_idx] = j
#        print(f"before swapping {arr}")
#        print("before adding it :",arr[min_idx])
#        print("second add on :", arr[i])
#       arr[i], arr[min_idx] = arr[min_idx], arr[i]
#        print("after swap:", arr)
#    return arr            

#selection_sort(arr)


#def selection_sort_tuples(arr):
#    n = len(arr)
    
#    for i in range(len(arr)):
#        min_idx = i
        
#        for j in range(i + 1, n):
#                min_idx = j
#        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#    return arr


#data = [('a', 0), ('b', 1), ('c', 7), ('d', 3), ('e', 2), ('f', 6), ('g', 9)]
#sorted_data = selection_sort_tuples(data)
#print(sorted_data)

#def merge_sort(arr):
   # size_of_list = len(arr)
   # if size_of_list > 1 :
        #right = arr[middle:]
        #merge_sort(left)
        #merge_sort(right)

        #        else :
   #             arr[k] = right[j]
  #           k += 1
#
      #  while i < len(left):
     #        i += 1
   #         k += 1
  #          
 #       while j < len(right):
#            arr[k] = right[j]
#            j += 1
#            k += 1
#        return arr                
                  

#my_list = [12,11,13,5,6,7]
#sorted_list = merge_sort(my_list)

#graph = {
 #   'A': ['B', 'C'],
  #  'B': ['D'],
   # 'C': ['E'],
    #'D': [],
    #'E': []
#}

#visited = set()

#def dfs(node):
#       print(node)
 #       visited.add(node)

  #      for neighbor in graph[node]:
   #         dfs(neighbor)

 
#from collections import deque

#def num_islands(grid):
#    rows, cols = len(grid), len(grid[0])
#    visited = set()
#    count = 0

#    def bfs(r, c):
#        queue = deque([(r, c)])
#        visited.add((r, c))

#        directions = [(1,0), (-1,0), (0,1), (0,-1)]

#        while queue:
#            row, col = queue.popleft()

#            for dr, dc in directions:
#                nr, nc = row + dr, col + dc

#                if (0 <= nr < rows and
#                    0 <= nc < cols and
#                    grid[nr][nc] == '1' and
#                    (nr, nc) not in visited):

#                    visited.add((nr, nc))
#                    queue.append((nr, nc))

#    for i in range(rows):
#        for j in range(cols):
#            if grid[i][j] == '1' and (i, j) not in visited:
#                count += 1
#                bfs(i, j)

#    return count

 

#from collections import deque

#def ladderLength(beginWord, endWord, wordList):
#    word_set = set(wordList)
    
    # If endWord is not in list → impossible
#    if endWord not in word_set:
#        return 0
    
#    queue = deque([(beginWord, 1)])  # (current_word, steps)
    
#    while queue:
#        word, steps = queue.popleft()
        
        # Try changing every letter
#        for i in range(len(word)):
#            for c in 'abcdefghijklmnopqrstuvwxyz':
#                new_word = word[:i] + c + word[i+1:]
                
#                if new_word == endWord:
#                    return steps + 1
                
#                if new_word in word_set:
#                    queue.append((new_word, steps + 1))
#                    word_set.remove(new_word)  # mark visited
    
#    return 0


#  01 MATRIX (LeetCode 542)
from collections import deque

def updateMatrix(mat) :
    rows, cols = len(mat), len(mat[0])
    queue = deque()

    # Step 1: initialize distances
    dist = [[float('inf')] * cols for _ in range(rows)]

    # Step 2: Push all 0s into queue
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    # Step 3: BFS
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions :
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    return dist






    # 6. Walls and Gates (Leetcode 286)
    from collections import deque

    def wallsAndGates(rooms) :
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # Step 1: Add all gates to queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0: #Gate
                    queue.append((r,c))

        # Step 2: BFS
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    # Only update empty rooms
                    if rooms[nr] [nc] == 2147483647:
                        rooms[nr][nc] = rooms[r][c] + 1
                        queue.append((nr, nc))                                     