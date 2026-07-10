import random, math

n_trials = 400000
n_hits = 0
sum_obs = 0.0
sum_obs_sq = 0.0

for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    Obs = 0.0
    if x**2 + y**2 < 1.0:
        n_hits += 1
        Obs = 4.0
    sum_obs += Obs
    sum_obs_sq += Obs**2

mean_obs = sum_obs / n_trials
mean_obs_sq = sum_obs_sq / n_trials
variance = mean_obs_sq - mean_obs**2
std_dev = math.sqrt(variance)

print("4 * n_hits / n_trials (pi estimate):", 4.0 * n_hits / float(n_trials))
print("<Obs>:", mean_obs)
print("<Obs^2>:", mean_obs_sq)
print("<Obs^2> - <Obs>^2:", variance)
print("sqrt(<Obs^2> - <Obs>^2):", std_dev)