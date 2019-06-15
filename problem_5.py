import hashlib
import time
import sys


class Block:
    def calc_hash(self, data):
        sha = hashlib.sha256()

        hash_str = data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __init__(self, timestamp = None, data = None, previous_hash = None):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None
        return

class Listing:
    def __init__(self):
        self.head = None
        self.tail = None
        self.prev = None
        self.next = None
        self.value = None

    def append(self, data):
        if len(sys.argv) < 1: sys.exit("ERROR: No data provided.")
        if self.head is None:
            node = Block(time.gmtime(), data, None)
            self.head = node
            self.tail = self.head
            return
        else:
            node = self.tail
            new_node = Block(time.gmtime(), data, node.hash)
            node.next = new_node
            self.tail = node.next


    def __str__(self):
        node = self.head
        out_string = ""
        while node:
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", node.timestamp)
            out_string += "==========" + "\n"
            out_string += "time: " + time_string + "\n"
            out_string += "data: " + str(node.data) + "\n"
            out_string += "previous_hash: " + str(node.previous_hash) + "\n"
            out_string += "current_hash:  " + str(node.hash) + "\n"
            out_string += "==========" + "\n"
            node = node.next
        return out_string

blockchainz = Listing()
blockchainz.append("Pet #1's name is Freddie.")
blockchainz.append("Saket loves Freddie.")
blockchainz.append("Hi")
print(str(blockchainz))
#For these three examples, Data will be respective string
#Notice how current hash of previous link is prev_hash of the following link
#For last example, in case function is empty, it will indicate so

error = Listing()
error.append()
print(str(error))