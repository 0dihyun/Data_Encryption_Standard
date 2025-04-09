initial_permutation_table = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

inverse_initial_permutation_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

Permutation_table = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

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

s_boxes = [
    # S-Box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],

    # S-Box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],

    # S-Box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],

    # S-Box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],

    # S-Box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],

    # S-Box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],

    # S-Box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],

    # S-Box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

def binary_to_text_ascii(Ciper_binary):
    plaintext_bytes = ''
    for i in range(0, len(Ciper_binary), 8):
        byte = Ciper_binary[i:i+8]
        binary_string = ''.join(map(str, byte))
        decimal_number = int(binary_string, 2)
        text = chr(decimal_number)
        plaintext_bytes += text
            
    return plaintext_bytes

def binary_to_text_utf16(Ciper_binary):
    decimal_number_list = []
    plaintext_bytes = []
    btext = b''
    for i in range(0, len(Ciper_binary), 8):
        byte = Ciper_binary[i:i+8]
        binary_string = ''.join(map(str, byte))
        decimal_number = int(binary_string, 2)
        decimal_number_list.append(decimal_number)
        btext += decimal_number.to_bytes(1, byteorder='big')
    
    divided_sequence = [btext[i:i+2] for i in range(0, len(btext), 2)]
    for i in divided_sequence:
        texts = i.decode('utf-16')
        plaintext_bytes.append(texts)
        
    return plaintext_bytes

def check_block_size_func(bin_result_PT_len, bin_result_PT):
    block = []
    blocks = []
    if bin_result_PT_len == 64:
        block.extend(bin_result_PT)
        blocks.append(block)
        print("\nwrite bits == 64 bits", block)
        block_size = len(blocks)
        return blocks, block_size
        
    elif bin_result_PT_len > 64:
        block.extend(bin_result_PT)
        for i in range(0, len(block), 64):
            bin_chunk = block[i:i+64]
            if len(bin_chunk) != 64:
                bin_chunk.extend([0] * (64 - len(bin_chunk)))
            blocks.append(bin_chunk)
        print("\ninput bits > 64 bits")
        block_size = len(blocks)
        return blocks, block_size
        
    else:
        block.extend(bin_result_PT)
        while len(block) < 64:
            block.append(0)
        blocks.append(block)
        print("\ninput bits < 64 bits")
        block_size = len(blocks)
        return blocks, block_size

def decryption(CT, KEY):
    key_change_to_bin = string_to_binary(f"{KEY}")
    subkeys = generate_subkeys(key=key_change_to_bin)
    clone_CT = CT[:]
    
    if len(clone_CT) < 64:
        for i in range(len(clone_CT)):
            clone_CT.extend(clone_CT[i])
            
    if len(clone_CT) > 64:
        IP_Byte = []
        for i in range(len(CT)):
            IP_Cb = initial_permutation(CT[i])
            
            Left_Cb = IP_Cb[:32]
            Right_Cb = IP_Cb[32:]
            
            for j in range(16):
                Left_Cb, Right_Cb = round_Func(Right_Cb, Left_Cb, subkeys[15-j])

            Byte = Left_Cb + Right_Cb

            IP_Byte.extend(inverse_permutation(Byte))
    else:
        IP_Cb = initial_permutation(CT)
        
        Left_Cb = IP_Cb[:32]
        Right_Cb = IP_Cb[32:]
        
        for i in range(16):
            Left_Cb, Right_Cb = round_Func(Right_Cb, Left_Cb, subkeys[15-i])

        Byte = Left_Cb + Right_Cb

        IP_Byte = inverse_permutation(Byte)
    
    return IP_Byte



def round_Func(L_bits, R_bits, subkey):
    Left_bits = L_bits
    Right_bits = R_bits

    Clone_Right_Bits = R_bits[:]

    while len(Clone_Right_Bits) < 48:
        Clone_Right_Bits.append(0)      

    XOR_Right_Key = [a ^ b for a, b in zip(Clone_Right_Bits, subkey)]

    sub_lists = [XOR_Right_Key[i:i+6] for i in range(0, len(XOR_Right_Key), 6)]

    s_box_result = []

    for i in range(8):
        s_box_result += s_box(sub_lists[i], i)
        
    s_box_result = [int(x) for x in s_box_result]

    Permutation_result = permutation(s_box_result)

    XOR_Left_Key = [a ^ b for a, b in zip(Left_bits, Permutation_result)]

    #new right bits 수정 해야됨
    new_Left_Bits = Right_bits
    new_Right_Bits = XOR_Left_Key
    
    return new_Left_Bits, new_Right_Bits

def encryption(PT, KEY):
    key_change_to_bin = string_to_binary(f"{KEY}")
    subkeys = generate_subkeys(key=key_change_to_bin)
    
    bin_result_PT = string_to_binary(PT)
    bin_result_PT_len = len(bin_result_PT)
    
    block, block_size = check_block_size_func(bin_result_PT_len=bin_result_PT_len,bin_result_PT=bin_result_PT)
    
    all_ciper_binary = []
    
    if block_size > 1:
        for i in range(block_size):
            initial_permutated_PT = initial_permutation(block[i])
            Left_bits = initial_permutated_PT[:32]
            Right_bits = initial_permutated_PT[32:]
            for j in range(16):
                Left_bits, Right_bits = round_Func(Right_bits, Left_bits, subkeys[j])

            merge_bits = Left_bits + Right_bits
            
            all_ciper_binary.append(inverse_permutation(merge_bits))
    else:
        initial_permutated_PT = initial_permutation(block[0])

        Left_bits = initial_permutated_PT[:32]
        Right_bits = initial_permutated_PT[32:]

        for i in range(16):
            Left_bits, Right_bits = round_Func(Right_bits, Left_bits, subkeys[i])
            
        merge_bits = Left_bits + Right_bits
        
        all_ciper_binary.extend(merge_bits)
        all_ciper_binary = inverse_permutation(all_ciper_binary)
    
    
    if len(bin_result_PT) % 64 != 0:
        while len(bin_result_PT) % 64 != 0:
            bin_result_PT.append(0)

    return bin_result_PT, all_ciper_binary

def initial_permutation(block):
    permuted_block = [None] * 64
    for i in range(64):
        permuted_block[i] = block[initial_permutation_table[i] - 1]
    return permuted_block

def inverse_permutation(bits):
    inverse_permuted = [None] * 64
    for i in range(64):
        inverse_permuted[i] = bits[inverse_initial_permutation_table[i] - 1]
    return inverse_permuted

def permutation(input_bits):
    output_bits = [input_bits[i - 1] for i in Permutation_table]
    return output_bits

def generate_subkeys(key):
    
    if len(key) == 64:
        pass
    elif len(key) < 64:
        while len(key) < 64:
            key.append(0)
    elif len(key) > 64:
        while len(key) == 64:
            key.drop
    
    compressed_key = [key[i-1] for row in PC_1_table for i in row]
    left_half = compressed_key[:28]
    right_half = compressed_key[28:]
    allsubkey = []
    for j in range(16):
        left_half = left_half[1:] + [left_half[0]]
        right_half = right_half[1:] + [right_half[0]]
        shift_bits = left_half + right_half
        subkey = [shift_bits[j-1] for row in PC_2_table for j in row]
        allsubkey.append(subkey)
    return allsubkey

def s_box(input_val, s_box_num):
    row = input_val[0] + input_val[5]
    col = input_val[1] + input_val[2] + input_val[3] + input_val[4]
    s_box_val = s_boxes[s_box_num][row][col]

    return format(s_box_val, '04b')

def string_to_binary(input_string):
    binary_string = ""
    for char in input_string:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_string += binary_char
    return [int(bit) for bit in binary_string]
