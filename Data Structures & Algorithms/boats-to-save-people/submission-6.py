class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the people list in ascending order
        # having 2 pointer starting at 0 and the ending
        # Having a count as 0 to return
        # While l < r: 
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
            # Pair matched: loading 2 ppl
            if total <= limit:
                l += 1

            count += 1 #1 boat per iteration
            r -= 1 #heavy always board 
        return count