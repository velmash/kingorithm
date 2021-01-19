num_list = list(map(int, input().split(" ")))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]

if num_list == ascending:
    print("ascending")
elif num_list == list(reversed(ascending)):
    print("descending")
else:
    print("mixed")
