

"""     Subsets     """

"""      Modified binary search
            Whenever you are given a sorted array, linked list, or matrix, and are asked to find a certain element, 
            the best algorithm you can use is the Binary Search. This pattern describes an efficient way to handle all 
            problems involving Binary Search.
            First, find the middle of start and end. An easy way to find the middle would be: middle = (start + end) / 2. But this has a good chance of producing an integer overflow so it’s recommended that you represent the middle as: middle = start + (end — start) / 2
            If the key is equal to the number at index middle then return middle
            If ‘key’ isn’t equal to the index middle:
            Check if key < arr[middle]. If it is reduce your search to end = middle — 1
            Check if key > arr[middle]. If it is reduce your search to end = middle + 1
"""

"""     Top K elements
            Any problem that asks us to find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.
            How to identify the Top ‘K’ Elements pattern:
                If you’re asked to find the top/smallest/frequent ‘K’ elements of a given set
                If you’re asked to sort an array to find an exact element
            The best data structure to keep track of ‘K’ elements is Heap. This pattern will make use of the Heap to solve multiple
                problems dealing with ‘K’ elements at a time from a set of given elements. The pattern looks like this:
            Insert ‘K’ elements into the min-heap or max-heap based on the problem.
            Iterate through the remaining numbers and if you find one that is larger than what you have in the heap, then remove
                that number and insert the larger one.
"""

"""     K-way merge
            The pattern looks like this:
                Insert the first element of each array in a Min Heap.
                After this, take out the smallest (top) element from the heap and add it to the merged list.
                After removing the smallest element from the heap, insert the next element of the same list into the heap.
                Repeat steps 2 and 3 to populate the merged list in sorted order.
                How to identify the K-way Merge pattern:


"""

"""     TOPOLOGICAL SORT
                    find linear ordering of elements that have dependencies on each other
                    for example if b was depend on A than A needs to run before B

                    How to identify the Topological Sort pattern:

                    The problem will deal with graphs that have no directed cycles
                    If you’re asked to update all objects in a sorted order
                    If you have a class of objects that follow a particular order
                    Problems featuring the Topological Sort pattern:

                    Initialization
                    a) Store the graph in adjacency lists by using a HashMap
                    b) To find all sources, use a HashMap to keep the count of in-degreesBuild the graph and find in-degrees of all vertices
                    Build the graph from the input and populate the in-degrees HashMap.
                    Find all sources
                    a) All vertices with ‘0’ in-degrees will be sources and are stored in a Queue.
                    Sort
                    a) For each source, do the following things:
                    —i) Add it to the sorted list.
                    — ii)Get all of its children from the graph.
                    — iii)Decrement the in-degree of each child by 1.
                    — iv)If a child’s in-degree becomes ‘0’, add it to the sources Queue.
                    b) Repeat (a), until the source Queue is empty.
"""
