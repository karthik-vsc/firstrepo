class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def InsertNode(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            head=self.head
        else:
            head=self.head
            while head.next:
                head=head.next
            head.next=new_node
    """def print_ll(self):
        while self.head:
            print(self.head.data)
            self.head=self.head.next"""
    #usinf iteration
    def reverse_ll(self):
        head=self.head
        prev=None
        while head:
            next=head.next
            head.next=prev
            prev=head
            head=next
        self.head=prev
        return self.head

#using recursion
def reverse(head):
    if (head == None):
        return head
         
    if (head.next == None):
        #remained last node is returned to node i.e ->reverse(head->next)
        return head
         
    node = reverse(head.next)
    head.next.next = head
    head.next = None
    return node
 
def print_ll(head):
    while head:
        print(head.data)
        head=head.next
ll1=LinkedList()
n=int(input("Enter no of elements to be entered in linked list:"))
for _ in range(n):
    ll1.InsertNode(int(input('Enter element to be entered in ll:')))
head=reverse(ll1.head)
print_ll(head) 