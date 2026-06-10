class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # iterate each operation.
        # havign a stack list and a total
        # if that operation is a number, append that number in stack and sum it in total.
        # else if it is a "+", sum = stack[-1] + stack[-2] and append that sum in stack. sum it to total
        # else if it it a "C", minus stack[-1] from the total and pop it from stack
        # else if it is a "D", double = stack[-1] * 2 and append that double in stack, sum it to total

        # time complexity: 0(n)
        # Space complexity: O(n)

        stack, total = [], 0
        for op in operations:
            if op == "+":
                top_two = stack[-1] + stack[-2]
                stack.append(top_two)
                total += top_two
            elif op == "C":
                total -= stack[-1]
                stack.pop()
            elif op == "D":
                double = stack[-1] * 2
                stack.append(double)
                total += double
            else:
                number =int(op)
                stack.append(number)
                total += number
            
        return total