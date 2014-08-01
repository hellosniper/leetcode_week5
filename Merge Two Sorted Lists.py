# Merge Two Sorted Lists.py


# Question: Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
# Question from: https://oj.leetcode.com/problems/merge-two-sorted-lists/
# Sulotion:
# Author: DongDing 
# Date: 2014/08/01
# Time complexity:  O(n)
# space complexity:  O(1)  
# Tag:  # linked list  
# Comment: 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        curr = head
        while l1 != None:
            if l2 == None:
                curr.next = l1    
                break
            
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
                

        if l1 == None:
            curr.next = l2
        return head
