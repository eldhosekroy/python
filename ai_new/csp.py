class CSP:
    def _init_(self, vars, domains, cons):
        self.vars, self.domains, self.cons = vars, domains, cons
        self.assignments = {}

    def is_consistent(self, var, val):
        return all(self.assignments[c[0]] != val for c in self.cons[var] if c[0] in self.assignments)

    def backtrack(self):
        if len(self.assignments) == len(self.vars):
            return self.assignments
        var = [v for v in self.vars if v not in self.assignments][0]
        for val in self.domains[var]:
            if self.is_consistent(var, val):
                self.assignments[var] = val
                result = self.backtrack()
                if result:
                    return result
                del self.assignments[var]
        return None

vars = ['A', 'B', 'C', 'D']
domains = {v: ['Red', 'Green', 'Blue'] for v in vars}
cons = {'A': [('B',), ('C',)], 'B': [('A',), ('D',)], 'C': [('A',), ('B',)], 'D': [('B',)]}

solution = CSP(vars, domains, cons).backtrack()
if solution:
    print("Solution:", solution)
else:
    print("No solution found.")
