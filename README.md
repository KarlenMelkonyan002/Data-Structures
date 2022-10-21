# AVL-Tree
In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property. Lookup, insertion, and deletion all take O(log n) time in both the average and worst cases, where n is the number of nodes in the tree prior to the operation. Insertions and deletions may require the tree to be rebalanced by one or more tree rotations.
# Functions
insert() - inserting value in tree,while inserting we calculate height and update balance factor.\
right_rotate(),left_rotate() - rotating for fixing AVL properties(make tree balanced).\
clear() - deleting tree.\
get_height() - height of entire tree.\
erase() - delete node with given key(calculate height, update balance like in insert().\
get_number_of_nodes() - number of nodes in tree.\
preorder(),postorder(),inorder(),levelorder() - specific ways for traversing whole tree by visiting all nodes(pre,post,in) and by level(level). 
get_root_data() - data of root in AVL\
merge() - merging two AVL trees\
find() - find specific node if exists and return data of node\
contains() - find specific node if exists
# Operators
== operator - equality of AVL trees\
print() - print AVL tree\
!= - inequality of AVL trees\
+, += - sum of AVL trees
