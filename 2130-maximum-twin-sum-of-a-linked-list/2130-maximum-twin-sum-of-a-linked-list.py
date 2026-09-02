class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        current = head

        while current != None:
            arr.append(current.val)
            current = current.next

        first = 0
        current = len(arr) - 1
        ans = 0

        while first < current:
            sums = arr[first] + arr[current]
            ans = max(ans, sums)

            first += 1
            current -= 1

        return ans