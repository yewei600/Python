class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None
		
	def get_data(self):
	    return self.data
	    

class LinkedList :
	def __init__( self ) :
		self.head = None		

	def add( self, data ) :
                cur = self.head
		node = Node( data )
		if cur == None :	
			self.head = node
		else:
		    while cur.next!= None:
		        cur=cur.next
		    cur.next=node
		    node.prev=cur

	def search( self, k ) :
		p = self.head
		if p != None :
			while p.next != None :
				if ( p.data == k ) :
					return p				
				p = p.next
			if ( p.data == k ) :
				return p
		return None

        def get_node(self,num):
            p=self.head
            cnt=0
            while p.next:
                if cnt<num:
                    p=p.next
                    cnt+=1
                else:
                    return p
                

	def remove( self, p ) :
		tmp = p.prev
		p.prev.next = p.next
		p.next.prev = p.prev		

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += str(p.data)
                                s +=" "
				p = p.next
			s += str(p.data)
		return s
	
        def DelMiddleNode(self,mid): 
            #iterate to the middle node          
            p=self.head
            cnt=0
            while p.next:
                p=p.next
                cnt+=1              
                if cnt==(mid-1):
                    print "pointer at index",p.get_data()
                    p.next=p.next.next
                    break
        
        def DelMiddleNode2(self,midNode):
            #given access already to middle node
            midNode.data=midNode.next.data
            midNode.next=midNode.next.next
            
            


l = LinkedList()

#build an array list based on the numbers in this list
numList=[1,2,3,4,5,6]


for num in numList:
    l.add(num)

l.get_node(3)    
    
print "original list: "
print l



l.DelMiddleNode2(l.get_node(len(numList)/2))
print "after delete:"
print l
