class Solution(object):
    def listnode_to_pylist(self, listnode):
        ret = []
        while True:
            ret.append(listnode.val)
            if listnode.next != None:
                listnode = listnode.next
            else:
                return ret

    def pylist_to_listnode(self, pylist, link_count):
        if len(pylist) > 1:
            ret = precompiled.listnode.ListNode(pylist.pop())
            ret.next = self.pylist_to_listnode(pylist, link_count)
            return ret
        else:
            return precompiled.listnode.ListNode(pylist.pop(), None)
    
    def addTwoNumbers(self, l1, l2):
        l1_ = self.listnode_to_pylist(l1)
        l2_ = self.listnode_to_pylist(l2)
        
        l1_.reverse()
        n1 = int(''.join([ str(_) for _ in l1_]))
        l2_.reverse()
        n2 = int(''.join([ str(_) for _ in l2_]))
        ret = list(map(int, list(str(n1 + n2))))

        return self.pylist_to_listnode(ret, len(ret))