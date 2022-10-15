


class Node:
    def __init__(self,dataval = None) :
        self.dataval = dataval
        self.nextval = None

class slinkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval,end = "->")
            printval = printval.nextval
        print("")

    def atbeginning(self,newdata):
        newnode = Node(newdata)
        newnode.nextval = self.headval
        self.headval = newnode
    def atend(self,newdata):
        newnode = Node(newdata)
        if self.headval is None:
            self.headval = newnode
            return
        curr = self.headval
        while(curr.nextval):
            curr = curr.nextval
        curr.nextval = newnode
    
    def inbetw(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        newnode = Node(newdata)
        newnode.nextval = middle_node.nextval
        middle_node.nextval = newnode

    def delete(self,removekey):
        Headval = self.headval
        if Headval is not None:
            if Headval == removekey:
                self.headval = Headval.nextval
                Headval = None
                return
        while (Headval is not None):
            if Headval.dataval == removekey:
                break
            prev = Headval
            Headval = Headval.nextval
        if (Headval == None):
            return
        prev.nextval = Headval.nextval
        Headval = None


list1 = slinkedlist()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list1.headval.nextval = e2
e2.nextval = e3

list1.listprint()
list1.atbeginning("Sun")
list1.listprint()
list1.atend("Thu")
list1.listprint()
list1.inbetw(list1.headval.nextval,"Fri")
list1.listprint()
list1.delete("Tue")
list1.listprint()
