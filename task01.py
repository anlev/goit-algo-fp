class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None

        if iterable is None:
            return

        for item in iterable:
            self.append(item)

    def prepend(self, data) -> None:
        self.head = Node(data, self.head)

    def append(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find(self, data):
        current = self.head

        while current:
            if current.data == data:
                return current
            current = current.next

        return None

    def delete(self, data) -> bool:
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def reverse(self) -> None:
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def to_list(self) -> list:
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result


def merge_sort(head):
    if not head or not head.next:
        return head

    middle = _get_middle(head)
    right_half = middle.next
    middle.next = None

    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right_half)

    return merge_sorted_lists(left_sorted, right_sorted)


def merge_sorted_lists(left, right):
    dummy = Node(None)
    tail = dummy

    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
    return dummy.next


def _get_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def test_constructor_from_list():
    ll = LinkedList([1, 2, 3])
    assert ll.to_list() == [1, 2, 3]


def test_basic_operations():
    ll = LinkedList([2, 3])
    ll.prepend(1)

    assert ll.to_list() == [1, 2, 3]
    assert ll.find(2) is not None
    assert ll.delete(2) is True
    assert ll.to_list() == [1, 3]


def test_reverse():
    ll = LinkedList([1, 2, 3, 4])
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1]


def test_merge_sort():
    ll = LinkedList([4, 2, 5, 1, 3])
    ll.head = merge_sort(ll.head)
    assert ll.to_list() == [1, 2, 3, 4, 5]


def test_merge_sorted_lists():
    ll1 = LinkedList([1, 3, 5])
    ll2 = LinkedList([2, 4, 6])

    merged = LinkedList()
    merged.head = merge_sorted_lists(ll1.head, ll2.head)

    assert merged.to_list() == [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    test_constructor_from_list()
    test_basic_operations()
    test_reverse()
    test_merge_sort()
    test_merge_sorted_lists()
    print("All tests passed.")
