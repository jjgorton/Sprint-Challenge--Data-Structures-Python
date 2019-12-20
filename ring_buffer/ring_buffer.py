from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            if self.current is None:
                self.current = self.storage.tail

        else:
            self.storage.add_to_tail(item)
            if self.storage.head is self.current:
                self.storage.remove_from_head()
                self.current = self.storage.tail
            else:
                self.storage.remove_from_head()
            # print('else', self.storage.tail.value)
            # print('head', self.storage.head.value)
            # print('cur', self.current.value)
        
        # if self.current is None:
        #     self.current = self.storage.tail
        #     print(self.current.value)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        j = self.storage.head
        i = self.current
        while len(list_buffer_contents) < self.storage.length:
            if i is not None:
                list_buffer_contents.append(i.value)
                i = i.next
            else:
                list_buffer_contents.append(j.value)
                j = j.next


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


test = RingBuffer(5)

test.append('a')
test.append('b')
test.append('c')
test.append('d')
test.append('e')
test.append('f')