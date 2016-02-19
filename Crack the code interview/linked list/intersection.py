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
		return s#[::-1]  #reverses string
	
       
	

     


l = LinkedList()

#build an array list based on the numbers in this list
numList=[1,2,3,4,5,6,5,5,5,7,6,6,6,5,10]

for num in numList:
    l.add(num)
    
    

print "original list: "
print l

