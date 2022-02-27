from multiprocessing import Process, freeze_support, Queue
from threading import Thread


def Thread1(queue):
    msgs = 0
    queue.put(msgs)

def Process1(queue_send):
    th1 = Thread(target=Thread1, args=(queue_send,))

    th1.setDaemon(True)
    th1.start()
    th1.join()

def Thread2(queue):
    if not queue.empty():
        msgs = queue.get()

def Process2(queue_rev):
    th1 = Thread(target=Thread2, args=(queue_rev,))

    th1.setDaemon(True)
    th1.start()
    th1.join()


if __name__ == "__main__":
    freeze_support()

    queue1 = Queue()
    queue2 = Queue()

    send_process = Process(target=Process1, args=(queue1,))
    rev_process  = Process(target=Process2, args=(queue2,))

    send_process.start()
    rev_process.start()