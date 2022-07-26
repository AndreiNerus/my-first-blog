k = int(input())

peoples = {a:int(b) for a, b in input().split()}

def get_youngest(x):
    return min(x)

print(get_youngest(peoples))