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
	
	
	#find the kth to element of a linked list
        def Return_kth_last(self,k):
            p=self.head
            cnt=0                     
            
            print "%dth element to last element: "% k
            while p:               
                if cnt<k-1:                
                    cnt+=1
                else:
                    print p.get_data()," "
                p=p.next    
            
                

l = LinkedList()

#build an array list based on the numbers in this list
numList=[1,2,3,4,5,6,7,8,9,10]

for num in numList:
    l.add(num)    

print "original list: "
print l


l.Return_kth_last(5)
