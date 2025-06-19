n = int(input())
int_list = map(int, input().split())

# Create tuple
t = tuple(int_list)

# Compute and print hash
print(hash(t))

