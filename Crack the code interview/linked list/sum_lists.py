
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
	
	def size(self):
	    p=self.head
	    cnt=1
	    while p.next:
	        p=p.next
	        cnt+=1
	    return cnt
	        	    	

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

'''                
2 numbers stored in the reverse order, in separate linked lists
sum them together in a linked list, also in the reverse order

consider linked lists of different lengths
 9->7->8   6->8->5        answer: 5->6->4->1


USE RECURSION
'''       
def sum_lists_backwards(s,t):
    return


def sum_lists_forwards(s,t):
    return 
    
    
    




            
s = LinkedList()
t = LinkedList()

#build an array list based on the numbers in this list
sList=[5,6,7]
tList=[1,2,3,4]

for num in sList:
    s.add(num)
for num in tList:
    t.add(num)  
        
print "original lists: "
print "s: ",s
print "t: ",t            
            
    