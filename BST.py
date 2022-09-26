
class node:
    
    def __init__(self,val):
        self.val = val
        self.right = ""
        self.left = ""

    def apped(self,val):
        while True:
            if val > self.val:
                if self.right == "":
                    self.right = node(val)
                    break
                else:
                    self = self.right
            elif val < self.val:
                if self.left == "":
                    self.left = node(val)
                    break
                else:
                    self = self.left

    def delete(self,val):
        while self.val != val:
            # Find address to delete
            if val < self.val:
                if self.left != "" and self.left.val == val:
                    temp = self.left
                    break
                else: 
                    self = self.left
            elif val > self.val:
                if self.right != "" and self.right.val == val:
                    temp = self.right
                    break
                else:
                    self = self.right

        # Case 1: No child
        if temp.left == "" and temp.right == "":
            if val > self.val:
                self.right = ""
            else:
                self.left = ""

        # Case 2: 1 Child
        elif temp.left == "":
            if self.val < val:
                self.right = temp.right
                temp.right = ""
            elif self.val > val:
                self.left = temp.right
                temp.right = ""
        elif temp.right == "":
            if self.val < val:
                self.right = temp.left
                temp.left = ""
            elif self.val > val:
                self.left = temp.left
                temp.left = ""
        
        # Case 3: 2 Children
        else:
            temp_min = temp.left
            temp = temp.right
            while temp.left != "":
                temp = temp.left
            temp.left = temp_min
            if self.val < val:
                self.right = self.right.right
            elif self.val > val:
                self.left = self.left.right
    

# Ex-2.1 Create binary tree
head = node(50)
head.apped(25)
head.apped(75)
head.apped(30)
head.apped(60)
head.apped(40)

# Ex-2.2 Remove value in binary tree
head.delete(30)
head.delete(75)
head.delete(40)

# Ex-2.3 Theory part (coding is need)
# Find maximum height

# Find parent

# Find children

# Fine leaves

# Find sibling