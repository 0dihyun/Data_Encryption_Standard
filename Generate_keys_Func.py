from String_To_binary_Func import string_to_binary

PC_1_table = [
    [57, 49, 41, 33, 25, 17, 9],
    [1, 58, 50, 42, 34, 26, 18],
    [10, 2, 59, 51, 43, 35, 27],
    [19, 11, 3, 60, 52, 44, 36],
    [63, 55, 47, 39, 31, 23, 15],
    [7, 62, 54, 46, 38, 30, 22],
    [14, 6, 61, 53, 45, 37, 29],
    [21, 13, 5, 28, 20, 12, 4]
]

PC_2_table = [
    [14, 17, 11, 24, 1, 5],
    [3, 28, 15, 6, 21, 10],
    [23, 19, 12, 4, 26, 8],
    [16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55],
    [30, 40, 51, 45, 33, 48],
    [44, 49, 39, 56, 34, 53],
    [46, 42, 50, 36, 29, 32]
]

# def generate_subkeys(key):
#     compressed_key = [key[i-1] for row in PC_1_table for i in row]
#     left_half = compressed_key[:28]
#     right_half = compressed_key[28:]
#     subkeys = []
#     for i in range(4):
#         left_half = left_half[1:] + [left_half[0]]
#         right_half = right_half[1:] + [right_half[0]]
#         subkey = [left_half[row-1] for row in PC_2_table[i]] + [right_half[row-1] for row in PC_2_table[i]]
#         # subkeys.append(subkey)
#         subkeys += subkey
#     return subkeys

def generate_subkeys(key):
    compressed_key = [key[i-1] for row in PC_1_table for i in row]
    left_half = compressed_key[:28]
    right_half = compressed_key[28:]
    subkeys = []
    allsubkey = []
    for i in range(16):
        left_half = left_half[1:] + [left_half[0]]
        right_half = right_half[1:] + [right_half[0]]
        subkey = [left_half[row-row] for row in PC_2_table[i-i]] + [right_half[row-row] for row in PC_2_table[i-i]]
        subkeys += subkey
        allsubkey.append(subkeys[:])
    return allsubkey

key = "thisis64"
bin_key = string_to_binary(key)

if len(bin_key) == 64:
    print(" == 64")
elif len(bin_key) < 64:
    while len(bin_key) < 64:
        bin_key.append(0)
    print(" < 64")
elif len(bin_key) > 64:
    print(" > 64 ")
    
all_subkeys = generate_subkeys(bin_key)

print(len(all_subkeys))