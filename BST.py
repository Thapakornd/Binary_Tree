
class node:

    # Init value to tree -----------------------------
    def __init__(self,val):
        self.val = val
        self.right = ""
        self.left = ""

    # Insert value Tree Function -------------------------------
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

    # Delete Tree Function ------------------------------
    def delete(self,val):
        while True:
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

        # Case 1: No child ----------------------
        if temp.left == "" and temp.right == "":
            if val > self.val:
                self.right = ""
            else:
                self.left = ""

        # Case 2: 1 Child ----------------------
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
        
        # Case 3: 2 Children ---------------------
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


# Find height of BST ------------------------------
def val_hi(bst):
    if bst == "":
        return 0
    left_h = val_hi(bst.left)
    right_h = val_hi(bst.right)
    return 1 + max(left_h, right_h)

def height(bst):
    val = val_hi(bst)
    print(f"\n\nHeight of Tree : {val}")
# ---------------------------------------------------
    
# Find parent of BST ----------------------------------
def val_par(bst):
    if bst == "":
        return 0
    if bst.left != "" or bst.right != "":
        p = 1
        temp.append(bst.val)
    else: 
        p = 0
    left_h = val_par(bst.left)
    right_h = val_par(bst.right)
    return p + left_h + right_h

def parent(bst):
    val_par(bst)
    val = len(temp)
    print(f"\n\nTotal Parent : {val}\nParent : ",end="")
    for i in temp:
        print(i,end=" ")
    temp.clear()
# ---------------------------------------------

# Find children of BST -----------------------------
def retur(bst):
    if bst == "":
        return 0
    if bst.val != "":
        chil_d = 1
        temp.append(bst.val)
    else:
        chil_d = 0
    left_h = retur(bst.left)
    right_h = retur(bst.right)
    return chil_d + left_h + right_h

def child(bst):
    retur(bst) 
    temp.pop(0)
    val = len(temp)
    print(f"\n\nTotal Children : {val}\nChildren : ",end="")
    for i in temp:
        print(i,end=" ")
    temp.clear()
# ------------------------------------------

# Find Leaves of BST ----------------------
def val_leav(bst):
    if bst == "":
        return 0 
    if bst.left == "" and bst.right == "":
        l = 1
        temp.append(bst.val)
    else:
        l = 0
    left_h = val_leav(bst.left)
    right_h = val_leav(bst.right)
    return left_h + right_h + l

def find_leav(bst):
    val_leav(bst)
    val = len(temp)
    print(f"\n\nTotal Leaves : {val}\nLeaves : ",end="")
    for i in temp:
        print(i,end=" ")
    temp.clear()
# -----------------------------------------
       
# Temp to keep value to monitor
temp = []

# Ex-2.1 Create binary tree
head = node(50)
head.apped(25)
head.apped(75)
head.apped(30)
head.apped(60)
head.apped(40)
head.apped(35)
head.apped(70)
head.apped(90)
head.apped(15)
head.apped(45)
head.apped(27)
head.apped(55)
head.apped(85)
head.apped(100)

# Ex-2.2 Remove value in binary tree

# Ex-2.3 Theory part (coding is need)
# Find maximum height
height(head)

# Find parent
parent(head)

# Find children
child(head)

# Fine leaves
find_leav(head)

# Find sibling