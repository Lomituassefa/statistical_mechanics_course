import random

x, y = 1.0, 1.0
delta = 4.0
n_trials = 4096
n_hits = 0
n_accept = 0  # NEW: counts accepted moves
for i in range(n_trials):
    del_x, del_y = random.uniform(-delta, delta), random.uniform(-delta, delta)
    if abs(x + del_x) < 1.0 and abs(y + del_y) < 1.0:
        x, y = x + del_x, y + del_y
        n_accept += 1  # NEW: increment only when the move was actually accepted
    if x**2 + y**2 < 1.0: n_hits += 1
print(4.0 * n_hits / float(n_trials))
print("acceptance rate:", n_accept / float(n_trials))  # NEW: print the acceptance rate