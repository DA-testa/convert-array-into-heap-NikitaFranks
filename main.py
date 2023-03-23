import sys
import threading
import numpy

def read_input():
    input_type = input().lower()
    
    if input_type == "i":
        n = int(input())
        parents = list(map(int, input().split()))
        
    elif input_type == "f":
        while True:
            try:
                file_name = input()
                if "a" in file_name:
                    raise ValueError("File name should not contain the letter 'a'")
                with open(f"test/{file_name}") as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
                break
            except FileNotFoundError:
                print("File not found, please enter a valid file name")
            except ValueError as e:
                print(e)
                
    return n, parents

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            children[parent].append(i)
    
  
    def get_height(node):
        if not children[node]:
            return 1
        heights = [get_height(child) for child in children[node]]
        return 1 + max(heights)
    
    return get_height(root)


def main():
    n, parents = read_input()
    print(compute_height(n, parents))



sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)   
threading.Thread(target=main).start()
