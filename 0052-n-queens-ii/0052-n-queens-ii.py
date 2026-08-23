class Solution:
    def totalNQueens(self, n: int) -> int:

        cols = set()
        diag1 = set()   # row - col
        diag2 = set()   # row + col

        count = 0

        def backtrack(row):
            nonlocal count

            # All queens placed
            if row == n:
                count += 1
                return

            for col in range(n):

                # Check if position is attacked
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Backtrack
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)

        return count
        