# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False
        maxCount = 0
        if self.ranks[dst_parent] < self.ranks[src_parent] :
            self.parents[src_parent] = self.parents[dst_parent]
            self.row_counts[dst_parent] += self.row_counts[src_parent]
            maxCount = self.row_counts[dst_parent]
        else:
            self.parents[dst_parent] = self.parents[src_parent]
            if self.ranks[src_parent] == self.parents[dst_parent] :
                self.ranks[src_parent] += 1
            self.row_counts[src_parent] += self.row_counts[dst_parent]
            maxCount = self.row_counts[src_parent]
        if self.max_row_count < maxCount :
            self.max_row_count = maxCount
        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, table):
        # find parent and compress path
        index = table
        while index != self.parents[index] :
            index = self.parents[index]

        while table != self.parents[table] :
            tmp = table
            table = self.parents[table]
            self.parents[tmp] = self.parents[index]

        
        # if table != self.parents[table] :
        #     self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():

    ip1 = input()
    n_tables, n_queries = map(int, ip1.split())
    ip2 = input()
    counts = list(map(int, ip2.split()))
    assert len(counts) == n_tables
    db = Database(counts)
    # ip4 = ["6 6", "6 5", "5 4", "4 3"]
    for i in range(n_queries):
        ip3 = input()
        dst, src = map(int, ip3.split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
