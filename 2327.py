class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        person = 1

        for i in range(1, n+1):
            print(f"Day {i}", end=" ")
            if delay == 0:
                print("Share a secret!")
                person += 1
                if i == forget:
                    person -= 1
                    print("I forget that!")
            else:
                print("Subtracting the delay!")
                delay -= 1

        person += person

        return print(f"This is the people who knows: {person}")


test = Solution()
test.peopleAwareOfSecret(4, 1, 3)


"""


"""