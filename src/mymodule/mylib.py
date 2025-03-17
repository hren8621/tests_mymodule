class MySimpleModule():
    def __init__(self):
        self._msg = "my default msg"
        self._count = 1

    def printMyMsgCount(self):
        print("Hi, you're using MySimpleModule")
        print("MySimpleModule properties: msg =", self._msg, ", count =", self._count)

    def changeMyMsgCount(self, newMsg, newCount):
        self._msg = newMsg
        self._count = newCount

if __name__ == '__main__':
    mm = MySimpleModule()
    mm.printMyMsgCount()
    mm.changeMyMsgCount("This is a new msg", 10)
    mm.printMyMsgCount()