import threading

def loop_print():
    for i in range(0, 3):
        print(i)

# 直接Threadを生成するパターン
thread1 = threading.Thread(target=loop_print())
thread2 = threading.Thread(target=loop_print())

thread1.start()
thread2.start()


# classの継承を使うパターン
class LoopPrintTread(threading.Thread):
    def __init__(self):
        super(LoopPrintTread, self).__init__()

    def run(self):
        """スレッドで処理する内容"""
        for i in range(0, 3):
            print('class:{}'.format(i))

thread1 = LoopPrintTread().start()
thread2 = LoopPrintTread().start()
