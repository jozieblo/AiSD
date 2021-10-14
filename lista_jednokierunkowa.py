from typing import Any
class Node:
    value: Any
    next: "Node"
class LinkedList:
    head:Node
    tail:Node
    def push(self,value: Any)->:
