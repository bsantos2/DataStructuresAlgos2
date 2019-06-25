import sys

class Double_Node:
    def __init__(self, value = None):
        self.head = None
        self.value = value
        self.left = None
        self.right = None

def create_sorted_char_list(data):
    temp_char_list = dict()
    for x in data:
        if x in temp_char_list:
            temp_char_list[x] += 1
        else:
            temp_char_list[x] = 1
    char_list = sorted(temp_char_list.items(), key=lambda x: x[1], reverse=False)
    return char_list

def insert_to_char_list(char_list, insert_data):
    try:
        value = insert_data.value[1]
        for x in range(0, len(char_list)):
            try:
                current_freq = char_list[x][1]
            except:
                node = char_list[x]
                current_freq = node.value
                current_freq = current_freq[1]
            if value <= current_freq:
                slice1 = char_list[0:x]
                slice2 = char_list[x:len(char_list)]
                slice1.append(insert_data)
                char_list = slice1 + slice2
                return char_list
        if value > current_freq:
            char_list.append(insert_data)
    except:
        char_list.append(insert_data)
    return char_list

def get_value(value):
    try:
        int(value[1])
        return value
    except:
        value = value.value
        return (None, value[1])

def draw_tree(char_list):
    left = char_list.pop(0)
    right = char_list.pop(0)
    freq_left = get_value(left)
    freq_right = get_value(right)
    current_node = Double_Node((None, freq_left[1] + freq_right[1]))
    current_node.left = Double_Node(left)
    current_node.right = Double_Node(right)
    if not char_list:
        current_node.head = Double_Node(current_node)
        return current_node
    char_list = insert_to_char_list(char_list, current_node)
    return draw_tree(char_list)

def encode_tree(node, code_list = "", code_table = dict()):
    if node is None:
        return
    elif type(node.value) is tuple:#node.value.left is None and node.value.right is None:
        if code_list == "":
            code_table[node.value[0]] = "0"
            return code_table
        else:
            code_table[node.value[0]] = code_list
            return
    if node.value.left is not None:
        code_list += "0"
        encode_tree(node.value.left, code_list)
    # remove last bit of code_list
    code_list = code_list[0:len(code_list) - 1]
    if node.value.right is not None:
        code_list += "1"
        encode_tree(node.value.right, code_list)
    # remove last bit of code_list
    code_list = code_list[0:len(code_list) - 1]
    return code_table

def huffman_encoding(data):
    #Generate sorted char lies
    char_list = create_sorted_char_list(data)
    if len(char_list) == 0:
        return "0", Double_Node((None, None)), []  # returning dummy value of 0 so it won't crash
    elif len(char_list) == 1:
        tree = Double_Node(tuple(char_list))
        tree.head = tree
    else:
        #Generate the huffman tree
        tree = draw_tree(char_list)
    #Create a dict containing bit stream per character
    if tree is not None:
        code_table = encode_tree(tree.head)
        if len(code_table) == 1:
            data_code = code_table[char_list[0]] #for the case of only one letter, repeated or not
        else:
            #Generate bit stream for entire sentence
            data_code = ""
            for x in data:
                data_code += code_table[x]
        return data_code, tree, code_table


def huffman_decoding(data,tree):
    word = ""
    node = tree.head
    dummy = ""
    if data == "0": #on encode portion, if nothing is detected, it will output only "0"
        decode_me = tree.value
        if decode_me[0] is None:
            return word
        else:
            decode_me = decode_me[0]
            for x in range(0, decode_me[1]):
                word += decode_me[0]
        return word
    else:
        for x in data:
            if x == "0":
                if type(node.value.left.value) is tuple:  # node.value.left is None and node.value.right is None
                    word += node.value.left.value[0]
                    node = tree.head
                    dummy = ""
                else:
                    node = node.value.left
                    dummy += x
            elif x == "1":
                if type(node.value.right.value) is tuple:  # node.value.left is None and node.value.right is None
                    word += node.value.right.value[0]
                    node = tree.head
                    dummy = ""
                else:
                    node = node.value.right
                    dummy += x
        return word

if __name__ == "__main__":
    codes = list()

    '''
    For the following strings below, the decoded sequence should reflect/mirror the same strings.
    Also, since Huffman requires binary tree, all my examples at least have 2 distinct letters. 
    '''
    codes.append("")
    codes.append("aaaaa")
    codes.append("The bird is the word")
    codes.append("In Python, the tendency is usually that one would use a non-fixed size list (that is to say items can be appended/removed to it dynamically). If you followed this, there would be no need to allocate a fixed-size collection ahead of time and fill it in with empty values. Rather, as you get or create strings, you simply add them to the list. When it comes time to remove values, you simply remove the appropriate value from the string. I would imagine you can probably use this technique for this.")

    for x in range(0, len(codes)):
        a_great_sentence = codes[x]#"The bird is the word"

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree, code_table = huffman_encoding(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))