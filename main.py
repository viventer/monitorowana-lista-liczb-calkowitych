from datetime import datetime

class IntList(list):
    @staticmethod
    def check_type(value):
        if type(value) is not int:
            raise ValueError("Not an integer type")

    def __setitem__(self, index, value):
        IntList.check_type(value)
        list.__setitem__(self, index, value)
    
    def append(self, value):
        IntList.check_type(value)
        list.append(self,value)

    def extend(self, iterable):
        for element in iterable:
            IntList.check_type(element)
        list.extend(self, iterable)

    def insert(self, index, value):
        IntList.check_type(value)
        list.insert(self, index, value)

    def __add__(self, iterable):
        for element in iterable:
            IntList.check_type(element)
        list.__add__(self, iterable)

class MonitoredIntList(IntList):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp("MonitoredIntList created")
    
    def log_timestamp(self, message):
        timestampStr = datetime.now().strftime("%H:%M:%S, %d/%m/%y")
        self.log.append(f"{timestampStr} -> {message}")

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
        self.log_timestamp(f"number {value} has been set as the {index} index")

    def append(self, value):
        super().append(value)
        self.log_timestamp(f"number {value} has been append to the IntList")
    
    def extend(self, iterable):
        super().extend(iterable)
        self.log_timestamp(f"IntList has been extended by the {iterable} colection")
        
    def insert(self, index, value):
        super().insert(index, value)
        self.log_timestamp(f"number {value} has been inserted into the list at the {index} index")

    def __add__(self, iterable):
        super().__add__(iterable)
        self.log_timestamp(f"{iterable} has been added to the list")

monitored = MonitoredIntList()

monitored.append(14)
monitored.insert(1,2)
monitored.extend([1,2,3])

print(monitored)

print("\n".join(monitored.log))