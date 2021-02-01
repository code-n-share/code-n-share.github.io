class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def printlist_reverse(self, head):
        if head == None:
            return;
        self.printlist_reverse(head.next)
        print(head.data)
        
    
    def insert_after(self, data1, data2):
        temp = self.head
        while temp:
            if temp.data == data1:
                temp1 = temp.next
                newNode = Node(data2)
                temp.next = newNode
                newNode.next = temp1
            temp = temp.next
    
    def delete(self, data):
        curr = self.head
        prev = curr
        if curr.data == data:
            self.head = curr.next
            return
        else:
            curr = curr.next
        while curr:
            if curr.data == data:
                prev.next = curr.next
            curr = curr.next
            prev = prev.next
    
    def get_mid(self, head):
        if head == None:
            return head;
        
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def sorted_merge(self, head1, head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        head = None
        if head1.data <= head2.data:
            head = head1
            head.next = self.sorted_merge(head1.next, head2)
        else:
            head = head2
            head.next = self.sorted_merge(head1, head2.next)
        return head
    
    def merge_sort(self, head):
        if head == None or head.next == None:
            return head
        
        mid = self.get_mid(head)
        head2 = mid.next
        mid.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(head2)
        sortedlist = self.sorted_merge(left, right)
        return sortedlist
                
        

if __name__ == '__main__':
    list = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(5)
    list.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    list.printlist()
    print(' ')
    list.insert_after(3,4)
    list.printlist()
    list.delete(3)
    print('')
    list.printlist()
    print('')
    list.printlist_reverse(list.head)
    node6 = Node(3)
    node4.next = node6
    node7 = Node(8)
    node6.next = node7
    print('')
    list.printlist()
    list.merge_sort(list.head)
    print('')
    list.printlist()
