l=['a','b','c','a','d','c','p','o','a','p']
print("Original list\n",l)
print("List after removing duplicates\n",list(dict.fromkeys(l)))