import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f"Instance {self.name} called with args: {args} and kwargs: {kwargs}")


if __name__ == '__main__':
    # Usage
    singleton_instance1 = Singleton("Instance 1")
    singleton_instance2 = Singleton("Instance 2")

    print(singleton_instance1 is singleton_instance2)  # Output: True

    # Calling as callable
    singleton_instance1(1, 2, a=3, b=4)
    singleton_instance2(5, 6, c=7, d=8)
