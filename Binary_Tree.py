
# Python Binary Tree
# Class Structure Node
class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

# Class Function Node Tree
class TreeNode:
	
	# Insert Node
	def insert(self,head,val):
		if head == None:
			return Node(val)
		elif val < head.val:
			head.left = self.insert(head.left,val)
		else:
			head.right = self.insert(head.right,val)
		return head

	# Delete Node
	def delete_value(self,temp):
		
		# Assign temp : delete value address
		# No child (Return None)
		if temp.left == None and temp.right == None:
			return None
		
		# 1 Child (Return New head with left or right)
		elif temp.left != None and temp.right == None:  # Child in left
			return temp.left
		elif temp.right != None and temp.left == None:  # Child in right
			return temp.right
		
		# 2 Children
		else:
			temp_replace = None  # <-- New Head Node
			temp_swap = None
			temp_right = temp.right
			if temp_right.left != None:   # <-- Move Right Del val : temp_right
				while temp_right.left.left != None:  # <-- Move Left until left.left == None
					temp_right = temp_right.left  
				if temp_right.left.right != None: # <-- If temp_right.left has child assign : temp_swap
					temp_swap = temp.left.right
				temp_replace = temp_right.left  # <-- Assign : temp_replace -> temp_right.left 
				temp_replace.left = temp.left    # \ 
				temp_replace.right = temp.right  # | <-- Swap Replace to Delte Val address
				temp_right.left = temp_swap      # /
				return temp_replace  # Return New Head
			else:
				temp_right.left = temp.left  # <-- If temp_right == None then Move left
				return temp_right # Return New Head

	# Search Delete node before main del			 
	def delete(self,head,val):
		if head.left != None and head.left.val == val:
			head.left = self.delete_value(head.left)
		elif head.right != None and head.right.val == val:
			head.right = self.delete_value(head.right)
		else:
			if val < head.val:
				head.left = self.delete(head.left,val)
			else:
				head.right = self.delete(head.right,val)
		return head

	# Parent Node
	par_list = []
	def parent(self,head):
		if head == None:
			return 0
		elif head.left != None or head.right != None:
			self.par_list.append(head.val)
		return self.parent(head.left),self.parent(head.right)

	# Children Node
	child_list = []
	def children(self,head):
		if head == None:
			return 0
		if head.left != None:
			self.child_list.append(head.left.val)
		if head.right != None:
			self.child_list.append(head.right.val)
		return self.children(head.left),self.children(head.right)

	# Leaves Node
	leave_node = []
	def leaves(self,head):
		if head == None:
			return 0
		if head.left == None and head.right == None:
			self.leave_node.append(head.val)
		return self.leaves(head.left),self.leaves(head.right)

	# Sibling Node
	sib_node = [] 
	def sibling(self,head):
		if head == None:
			return 0
		if head.left != None and head.right != None:
			self.sib_node.append([head.left.val,head.right.val])
		return self.sibling(head.left),self.sibling(head.right)

	# Print Pre_order Tree Node 
	def pre_order(self,head):
		if head == None:
			return 0
		print(head.val, end=" -> ")
		return self.pre_order(head.left) + self.pre_order(head.right)

	# Update Height Tree Node
	def get_height_all(self,head):
			if head == None:
				return 0
			head.height = 1 + max(self.get_height_all(head.left),self.get_height_all(head.right))
			return head.height

	# All Balance Node Function
	def balance(self,head):
		
		def left_rotate(head):  # Left Rotate
			temp = head.right
			if temp.left != None:
				temp = right_rotate(temp)
			head.right = temp.left
			temp.left = head

			# Update Height
			head.height = 1 + max(get_height(head.left),get_height(head.right))
			temp.height = 1 + max(get_height(temp.left),get_height(head.right))
			return temp

		def right_rotate(head):  # Right Rotate
			temp = head.left
			if temp.right != None:
				temp = left_rotate(temp)
			head.left = temp.right
			temp.right = head

			# Update Height
			head.height = 1 + max(get_height(head.left),get_height(head.right))
			temp.height = 1 + max(get_height(temp.left),get_height(head.right))
			return temp

		def get_height(head):  # Get Height each node
			if head == None:
				return 0
			return head.height

		# Function Balance Tree
		def balance_tree(head):
			if head == None:
				return None
			head.left = balance_tree(head.left)  # <-- Travel with preorder
			head.right = balance_tree(head.right)
			balance_val = get_height(head.left) - get_height(head.right)
	
			while balance_val < -1 or balance_val > 1: # <-- Check balance currently
				if balance_val < -1:
					head = left_rotate(head)
				if balance_val > 1:
					head = right_rotate(head)
				balance_val = get_height(head.left) - get_height(head.right)
			return head  # Return New Head
		
		# Function Check No need to balance
		def loop_return(head):
			if head == None:
				return 0
			get_left = loop_return(head.left)
			get_right = loop_return(head.right)
			check_bal = get_height(head.left) - get_height(head.right)
			b = 0
			if check_bal < -1 or check_bal > 1:
				b = 1
			return b + get_left + get_right

		# Init Height each node
		head.height = self.get_height_all(head)
		
		# Find balance node
		bal_loop = 1
		while bal_loop:
			head = balance_tree(head)
			bal_loop = loop_return(head)  # Check stop balancing

		return head
		
# init Treenode
func_tree = TreeNode()
head = None

# Insert Node
list_ap = [50,25,75,30,60,40,35,70,90,15,45,27,55,85,100]
for node in list_ap:
	head = func_tree.insert(head, node)

# Delete
head = func_tree.delete(head, 30)
head = func_tree.delete(head, 75)
head = func_tree.delete(head, 35)

# Maximum Height
func_tree.get_height_all(head)
print(f'Maximum Height : {head.height}')

# Parent
func_tree.parent(head)
print(f"Parent {len(func_tree.par_list)} : {func_tree.par_list}")

# Children
func_tree.children(head)
print(f"Children {len(func_tree.child_list)} : {func_tree.child_list}")

# Leaves
func_tree.leaves(head)
print(f"Leaves {len(func_tree.leave_node)} : {func_tree.leave_node}")

# Siblings
func_tree.sibling(head)
print(f"Sibing {len(func_tree.sib_node)} : {func_tree.sib_node}")

# Balance node
# head = func_tree.balance(head)

print("Preorder Travel")
func_tree.pre_order(head)
