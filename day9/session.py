class Session:

    def __del__(self):
        print("Session Ended")


obj = Session()

del obj
