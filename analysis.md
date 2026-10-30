Analysis Question

A linked-list stack pushes and pops at the head because the head can be updated in constant time, O(1), without searching through the list. Removing an item from the tail of a singly linked list would require traversing the list to find the previous node, which takes O(n) time.

An array queue must be circular so that spaces freed at the beginning can be reused after the rear reaches the physical end of the array. The size counter distinguishes a full queue from an empty queue, even when the front and rear positions could otherwise appear the same.
