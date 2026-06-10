class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the people list in ascending order
        # having 2 pointer starting at 0 and the ending
        # Having a count as 0 to return
        # While l < r: 
        # a. if people[l] > limit, break and return count
        # b. while l < r and people[r] > limit, move the right pointer inward.
        # Note: after this, people[r] < limit,
        # c. while l < r and people[l] + people[r] > limit, increase the count and move the right pointer inward
        # (right peson is in boat)
        # d. while l < r and people[l] + people[r] <= limit, increase the count and move 2 pointers.
        # e. if l == r and people[l] <= limit (last person), increase the count
        # Return the count 

        # Time complexity: o(nlogn)
        # Space complexity: O(1)

        people.sort()
        l, r = 0 , len(people) - 1
        count = 0
        while l <= r:
            total = people[l] + people[r]
            if total > limit:
                count += 1
            elif total <= limit:
                count += 1
                l += 1

            r-= 1
        return count