'''
Design an IdManager.

IdManager manages a pool of integer ids. (from 1 to n). It should provide 

apis to get_id() and free_id()

get_id(): It returns any id , available in the pool. An Id cannot be given away

again, unless it has been freed.

free_id(): It returns the id back to the pool, so that it can be given out

again.

Discuss the apis definitions, data structures and write tests.

'''
import threading
import logging
import time
import random
from datetime import datetime

TEST = 0

FORMAT = '[%(levelname)s] (%(threadName)-10s) %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

class LinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.val)

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return '%s(%r)' %(self.__class__.__name__, self.head)
        
    def __nonzero__(self):
        return self.head != None
    
    def addHead(self, newHead):
        newHead.next = self.head
        self.head = newHead
        logging.debug('newHead: {}'.format(self.head))
        
    def delHead(self):
        oldHead = self.head
        self.head = self.head.next
        logging.debug('oldHead: {}, newHead: {}'.format(oldHead, self.head))
        return oldHead
    
    def printList(self):
        p = self.head
        while p:
            print p.val,
            p = p.next
        print

class IdManager(object):
    def __init__(self, n):
        self.freeList = LinkedList()
        self.hashmap = [False] * n
        self.totalNum = n
        self.CreateFreeList(n)
        self.lock = threading.Lock()

    
    def get_id(self):
        ''' Returns available id if succeeds, otherwise returns -1.
        '''
#         if TEST:
#             time.sleep(1)   # for testing only
        with self.lock:
            if not self.freeList:
                logging.error('[{}] Get id error: list is empty'.format(datetime.now()))
                return -1
            id = self.freeList.delHead().val
            assert self.hashmap[id-1] == False
            self.hashmap[id-1] = True
            
            logging.info('[{}] Get id success: gets {}'.format(datetime.now(), id))
        return id
    
    def free_id(self, id):
        ''' Returns True if successful, False otherwise.
        '''
#         if TEST:
#             time.sleep(1)   # for testing only
        if id > self.totalNum or id < 1:
            logging.error('[{}] Free id error: invalid id {}'.format(datetime.now(), id))
            return False
        with self.lock:
            if self.hashmap[id-1] == False:
                logging.error('[{}] Free id error: id {} is not in use'.format(datetime.now(), id))
                return False
            
            self.freeList.addHead(LinkedListNode(id))
            self.hashmap[id-1] = False
            logging.info('[{}] Free id succeeds: frees {}'.format(datetime.now(), id))
        return True
        
    
    def CreateFreeList(self, n):
        for i in xrange(n, 0, -1):
            self.freeList.addHead(LinkedListNode(i))
    
    def printFreeList(self):
        self.freeList.printList()
            
if __name__ == '__main__':
    N = 6
    idManager = IdManager(N)
    idManager.printFreeList()
    
    threads = []
    for i in xrange(4*N):
#         #Add 2 Get threads and 2 Free threads each time.
#         for j in xrange(2):
#             threads.append(threading.Thread(target = idManager.get_id))
#         for k in xrange(2):
#             # id to be freed is generated randomly ranging from 0 to 1.5*N 
#             threads.append(threading.Thread(target = idManager.free_id, args=(random.randint(0,N*3/2),)))
        choice = random.randint(0, 1)
        if choice == 0:
            input = random.randint(0,N*3/2)
            t = threading.Thread(target = idManager.free_id, args=(input,))
            print '{}: free id {}'.format(t.name, input)
            threads.append(t)
        else:
            t = threading.Thread(target = idManager.get_id)
            print '{}: get id'.format(t.name)
            threads.append(t)
    print len(threads)
    for i in xrange(len(threads)):
        threads[i].start()
    