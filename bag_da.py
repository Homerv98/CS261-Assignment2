# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        add value to bag
        """
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        remove any one occurrence of value from bag.
        return true if removed, false otherwise
        """
        for i in range(self._da.length()):
            if value == self._da.get_at_index(i):
                self._da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
        return number of occurrences of value from bag
        """
        count = 0;

        for i in range(self._da.length()):
            if value == self._da.get_at_index(i):
                count += 1
        return count

    def clear(self) -> None:
        """
        clear the array
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        return true if two bags are equal
        """
        #size check
        if self.size() != second_bag.size():
            return False

        #both empty
        if self.size() == 0:
            return True

        #compare counts for each element in both bags
        for i in range(self._da.length()):
            val = self._da.get_at_index(i)

            #check if this has been seen befor
            seen = False
            for j in range(self._da.length()):
                if self._da.get_at_index(j) == val:
                    seen = True
                    break
            if seen:
                continue
            if self.count(val) != second_bag.count(val):
                return False
        return True

    def __iter__(self):
        """
        enable iteration on bag
        """
        self._iter_index = 0
        return self

    def __next__(self):
        """
        Return next element from bag or raise StopIteration
        """
        if self._iter_index >= self._da.length():
            raise StopIteration
        value = self._da.get_at_index(self._iter_index)
        self._iter_index += 1
        return value



# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
