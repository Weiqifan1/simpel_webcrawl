
class Dictlist: 

    def __init__(self, start_list = None):
        self.pub_list = []
        self.pub_dict = {}  
        if not start_list == None:
            self.pub_list = start_list

    def add_to_dict(self, mykey, mylistoffuturekeys):
        for item in mylistoffuturekeys:
            self.pub_list.append(item)
        self.pub_dict[mykey] = mylistoffuturekeys
    
    def append_item(self, mykey):
        self.pub_list.append(mykey)

    def append_list(self, mykey, mylist):
        for item in mylist:
            self.pub_list.append(item)
        self.pub_dict[mykey] = mylist