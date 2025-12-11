class Solution:
    def countCoveredBuildings(self, n, buildings):
        from bisect import bisect_left
        rowToCol = {}
        colToRow = {}
        for x, y in buildings:
            rowToCol.setdefault(x, []).append(y)
            colToRow.setdefault(y, []).append(x)

        for v in rowToCol.values():
            v.sort()
        for v in colToRow.values():
            v.sort()

        cnt = 0
        for x, y in buildings:
            cols = rowToCol[x]
            rows = colToRow[y]

            i = bisect_left(cols, y)
            left = cols[i-1] if i > 0 else None
            right = cols[i+1] if i+1 < len(cols) else None

            j = bisect_left(rows, x)
            up = rows[j-1] if j > 0 else None
            down = rows[j+1] if j+1 < len(rows) else None

            if left is not None and right is not None and up is not None and down is not None:
                cnt += 1

        return cnt