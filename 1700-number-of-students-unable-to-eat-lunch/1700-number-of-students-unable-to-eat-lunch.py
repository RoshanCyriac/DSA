
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sd = deque(sandwiches)

        failed = 0   # count of consecutive failures

        while st and sd:
            if st[0] == sd[0]:
                st.popleft()
                sd.popleft()
                failed = 0      # reset because someone ate
            else:
                st.append(st.popleft())
                failed += 1

            if failed == len(st):
                break

        return len(st)