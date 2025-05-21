from math import comb as c

# The probability is calculated as:
# P = possible_outcomes / favorable_outcomes
#   = (Number of ways to choose allowed positions for Aces, Twos, Threes) / 
#     (Total number of ways to choose positions for Aces, Twos, Threes)

possible_outcomes = (
    c(40, 4)    # choose 4 positions for the aces from 40 total positions
    * c(36, 4)  # choose 4 positions for the twos from the 36 remaining positions
    * c(32, 4)  # choose 4 positions for the threes from the 32 remaining positions
)

# Position Partitions:
# P1: Positions p where p % 3 == 1. P1 = {1, 4, 7, ..., 37, 40}. Number of positions in P1 = 14.
# P2: Positions p where p % 3 == 2. P2 = {2, 5, 8, ..., 38}.     Number of positions in P2 = 13.
# P3: Positions p where p % 3 == 0. P3 = {3, 6, 9, ..., 39}.     Number of positions in P3 = 13.

favorable_outcomes = sum(
    (
        # --- Aces Placement (NOT in P1) ---
        # Place `k` Aces in P2, place the remaining `4-k` Aces in P3.
        # P2 has 13 total spots. P3 has 13 total spots.
        c(13, k) * c(13, 4-k)

        # --- Twos Placement (NOT in P2) ---
        # Place `j` Twos in P3, place the remaining `4-j` Twos in P1.
        # P3 has 13-(4-k) = 9+k remaining spots for Twos. P1 has 14 remaining spots for Twos (Aces were not placed in P1). 
        * c(9+k, j) * c(14, 4-j)

        # --- Threes Placement (NOT in P3) ---
        # Place `i` Threes in P1, place the `4-i` remaining Threes in P2.
        # The remaining (4-i) Threes must be placed in P2.
        # P1 has 14-(4-j) = 10+j remaining spots for Threes. P2 has 13-k remaining spots for Threes.
        * c(14-(4-j), i) * c(13-k, 4-i)
    )
    # Iterate over the number of Aces in P2 (k), Twos in P3 (j), and Threes in P1 (i). Each ranges from 0 to 4 (inclusive).
    for k in range(5)
    for j in range(5)
    for i in range(5)
)

print(f"#{favorable_outcomes = }")
print(f"#{possible_outcomes = }")
print(f"P = {favorable_outcomes / possible_outcomes}")

