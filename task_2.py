# ---------- Step 1: Store building data ----------
# name: (build_time, earning_per_unit)
BUILDINGS = {
    "T": (5, 1500),   # Theatre
    "P": (4, 1000),   # Pub
    "C": (10, 2000),  # Commercial Park
}

# Order used when printing / counting: T, P, C
ORDER = ["T", "P", "C"]


def max_profit(n):
    # ---------- Step 5: memory so we don't repeat work ----------
    memo = {}

    # ---------- Step 2: best earnings starting from time t ----------
    def solve(t):
        # If we already solved this time, return the saved answer
        if t in memo:
            return memo[t]

        # Option "stop building": earns 0, and builds nothing (0 T, 0 P, 0 C)
        best_earn = 0
        best_solutions = {(0, 0, 0)}   # a set, so duplicates are removed

        # ---------- Step 3: try each building ----------
        for name in ORDER:
            build_time, rate = BUILDINGS[name]
            finish = t + build_time

            # Building must finish BEFORE time n to earn anything
            if finish >= n:
                continue

            # Money this building earns until time n
            gain = (n - finish) * rate

            # Best we can do after this building is finished
            future_earn, future_solutions = solve(finish)

            total = gain + future_earn

            # ---------- Step 4: keep only the best (and ties) ----------
            new_solutions = set()
            for (t_cnt, p_cnt, c_cnt) in future_solutions:
                # Add 1 to the building we just chose
                if name == "T":
                    new_solutions.add((t_cnt + 1, p_cnt, c_cnt))
                elif name == "P":
                    new_solutions.add((t_cnt, p_cnt + 1, c_cnt))
                else:
                    new_solutions.add((t_cnt, p_cnt, c_cnt + 1))

            if total > best_earn:
                # Found a better answer: replace everything
                best_earn = total
                best_solutions = new_solutions
            elif total == best_earn:
                # Tie: keep both sets of solutions
                best_solutions = best_solutions | new_solutions

        # Save in memory and return
        memo[t] = (best_earn, best_solutions)
        return memo[t]

    # Start at time 0
    return solve(0)


# ---------- Step 6: print the result ----------
def print_result(n):
    earnings, solutions = max_profit(n)
    print(f"Time Unit: {n}")
    print(f"Earnings: ${earnings}")
    print("Solutions")
    # sorted(..., reverse=True) just makes the output order neat
    for i, (t, p, c) in enumerate(sorted(solutions, reverse=True), start=1):
        print(f"{i}. T: {t} P: {p} C: {c}")
    print()


# Test the 3 given cases
print_result(7)
print_result(8)
print_result(13)