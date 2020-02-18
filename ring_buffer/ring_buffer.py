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
        self.storage = [None] * capacity
        self.capacity = capacity
        self.current = 0

    def append(self, item):
        # if len(self.storage) < self.capacity:
        #     self.storage.append(item)
        #     if self.current is None:
        #         self.current = self.storage[0]

        # else:
        #     self.storage.append(item)
        #     if self.storage[0] is self.current:
        #         self.storage.pop(0)
        #         self.current = self.storage[len(self.storage)-1]
        #     else:
        #         self.storage.pop(0)

        self.storage[self.current] = item


        if self.current + 1 == self.capacity:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        list_buffer_contents = []

        # TODO: Your code here

        for i in self.storage:
            if i is not None:
                list_buffer_contents.append(i)

        return list_buffer_contents


test = RingBuffer(5)

test.append('a')
test.append('b')
test.append('c')
test.append('d')
test.append('e')
test.append('f')