#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node(object):                              #创建表结点类
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class LinkList(object):                          #创建链表类
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):                  #得到一个链表元素的值
        if self.is_empty():
            print ('linklist is empty.')
            return
        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return
        else:
            return self.getitem(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print ('linklist is empty.')
            return
        elif key <0  or key > self.getlength():
            print ('the given key is error')
            return
        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
            
    def getlength(self):                           #求链表的长度
        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length
    
    def is_empty(self):                             #判断链表是否为空
        if self.getlength() ==0:
            return True
        else:
            return False
        
    def clear(self):
        self.head = 0

    def append(self,item):                          #后端操作，插入元素
        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getitem(self,index):                         #获得链表中下标为index的元素值
        if self.is_empty():
            print ('Linklist is empty.')
            return
        j = 0
        p = self.head
        while p.next!=0 and j <index:
            p = p.next
            j+=1
        if j ==index:
            return p.data
        else:
            print ('target is not exist!')

    def insert(self,index,item):                                   #插入元素
        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return
        if index ==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p

    def delete(self,index):                                       #删除元素
        if self.is_empty() or index<0 or index >self.getlength():
            print ('Linklist is empty.')
            return
        if index ==0:
            q = Node(item,self.head)
            self.head = q
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1
        if index ==j:
            post.next = p.next

    def index(self,value):                                #得到链表元素的下标
        if self.is_empty():
            print ('Linklist is empty.')
            return
        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1
        if p.data == value:
            return i
        else:
            return -1


l = LinkList()
l.initlist([1,2,3,4,5])
print (l.getitem(4))
l.append(6)
print (l.getitem(5))

l.insert(4,40)
print (l.getitem(3))
print (l.getitem(4))
print (l.getitem(5))

l.delete(5)
print (l.getitem(5))

l.index(5)
