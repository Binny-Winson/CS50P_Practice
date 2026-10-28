class Jar:
    def __init__(self, capacity=12):
        if type(capacity) is not int or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        # if not isinstance(capacity, int) or capacity < 0:
        #     raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
           raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(5)
custom_jar = Jar(20)
print(jar)
print(custom_jar.capacity)