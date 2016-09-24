
import multiprocessing
import s
import threading

class Singleton(object):
    def __new__(cls, *args, **kw):  
	    if not hasattr(cls, '_instance'):  
	        orig = super(Singleton, cls)  
	        cls._instance = orig.__new__(cls, *args, **kw)  
	    return cls._instance  
    queue = multiprocessing.Queue()
    queue.put("1")
    queue.put("2")


def test(event):
	event.wait()
	event.clear()
	print("11111111111111111")
	event.set()
	#print(s.queue.get(False))

def main():
	event = multiprocessing.Event()
	event.set()
	# p1 = multiprocessing.Process(target = test, daemon = True)
	# p2 = multiprocessing.Process(target = test, daemon = True)

	p1 = threading.Thread(target = test, args = (event, ), daemon = True)
	p2 = threading.Thread(target = test, args = (event, ), daemon = True)
	p3 = threading.Thread(target = test, args = (event, ), daemon = True)
	p1.start()
	p2.start()
	p3.start()
	p1.join()
	p2.join()
	p3.join()

if __name__ == '__main__':
	main()
	input()
