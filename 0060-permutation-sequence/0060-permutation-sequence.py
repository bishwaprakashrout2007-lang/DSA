class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]

        # Precompute factorials
        fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        # Convert k to 0-based index
        k -= 1

        result = []

        for i in range(n, 0, -1):
            block_size = fact[i - 1]

            index = k // block_size

            result.append(numbers[index])

            numbers.pop(index)

            k %= block_size

        return "".join(result)