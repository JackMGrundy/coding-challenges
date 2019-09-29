"""
Suppose we have a class:                                                        

public class Foo {                                                              

  public void first() { print("first"); }                                       

  public void second() { print("second"); }                                     

  public void third() { print("third"); }                                       

}                                                                               

The  same  instance  of  Foo will be passed to three different threads. Thread A
will  call first(), thread B will call second(), and thread C will call third().
Design  a  mechanism  and modify the program to ensure that second() is executed
after first(), and third() is executed after second().                          

                                                                                

Example 1:                                                                      

Input: [1,2,3]                                                                  

Output: "firstsecondthird"                                                      

Explanation:  There  are  three  threads  being  fired asynchronously. The input
[1,2,3]  means  thread  A  calls  first(), thread B calls second(), and thread C
calls third(). "firstsecondthird" is the correct output.                        

Example 2:                                                                      

Input: [1,3,2]                                                                  

Output: "firstsecondthird"                                                      

Explanation:  The  input  [1,3,2]  means  thread A calls first(), thread B calls
third(), and thread C calls second(). "firstsecondthird" is the correct output. 

                                                                                

Note:                                                                           

We  do  not know how the threads will be scheduled in the operating system, even
though  the  numbers  in the input seems to imply the ordering. The input format
you see is mainly to ensure our tests' comprehensiveness.                       

"""
# 64ms. 81 percentile.
# BARRIERS
from threading import Barrier
class Foo:
    def __init__(self):
        self.firstBarrier = Barrier(2)
        self.secondBarrier = Barrier(2)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.firstBarrier.wait()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.firstBarrier.wait()
        printSecond()
        self.secondBarrier.wait()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.secondBarrier.wait()
        printThird()


#  68ms. 66 percentile.
# LOCKS
from threading import Lock
class Foo:
    def __init__(self):
        self.locks = (Lock(), Lock())
        self.locks[0].acquire()
        self.locks[1].acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.locks[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.locks[0]:
            printSecond()
            self.locks[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            printThird()


# 64ms. 81 percentile.
# EVENTS
from threading import Event
class Foo:
    def __init__(self):
        self.done = (Event(), Event())

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.done[0].set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.done[0].wait()
        printSecond()
        self.done[1].set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.done[1].wait()
        printThird()


# 60ms. 92 percentile.
# SEMAPHORES - basically locks since value = 0
from threading import Semaphore
class Foo:
    def __init__(self):
        self.gates = (Semaphore(0), Semaphore(0))

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.gates[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.gates[0]:
            printSecond()
            self.gates[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.gates[1]:
            printThird()
            

"""
Notes:

Great questions for playing around with various concurrency mechanisms. 

"""