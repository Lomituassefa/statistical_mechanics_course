import random, math

def dist(x, y):
    """
    Distance between points x=(x0,x1) and y=(y0,y1) on a UNIT TORUS
    (periodic boundary conditions), not a plain flat square.
    This means the box "wraps around": the right edge touches the left edge,
    and the top edge touches the bottom edge -- just like Pac-Man.
    """
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)   # take the SHORTER path around the wrap-around
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return math.sqrt(d_x**2 + d_y**2)


def direct_disks(N, sigma):
    """
    Try to place N non-overlapping disks of radius sigma in the unit box,
    using pure brute-force 'direct sampling':
      - place disks one at a time at completely random positions
      - the INSTANT a new disk overlaps an existing one, throw the
        WHOLE configuration away and start again from disk #1
      - keep retrying until one full attempt succeeds with zero overlaps

    This guarantees every successful configuration is drawn EXACTLY
    uniformly from the space of valid (non-overlapping) configurations --
    i.e. it is a direct, unbiased realization of the equiprobability
    postulate. The price is efficiency: as N or eta grows, most attempts
    fail, so it can take many, many restarts to succeed.
    """
    n_iter = 0        # counts how many total attempts (including failures) were made
    condition = False # becomes True only when N disks are placed with no overlap

    while condition == False:
        n_iter += 1

        # --- start a brand-new attempt ---
        # place the very first disk anywhere at random; nothing to check yet
        L = [(random.random(), random.random())]

        # try to add the remaining N-1 disks, one at a time
        for k in range(1, N):
            a = (random.random(), random.random())  # candidate new disk position

            # distance from the candidate to the CLOSEST disk already placed
            min_dist = min(dist(a, b) for b in L)

            if min_dist < 2.0 * sigma:
                # overlap detected (disks closer than 2*sigma = sum of radii)
                # -> abandon this entire attempt immediately
                condition = False
                break   # exits the for-loop; while-loop will restart from scratch
            else:
                # no overlap with anything placed so far -> keep this disk
                L.append(a)
                condition = True  # tentatively true; stays true only if the
                                  # for-loop completes without ever breaking

    # loop exits only once a full configuration of N disks succeeded
    return n_iter, L


# ---------------- main experiment ----------------

N = 16          # number of disks
eta = 0.26      # target packing fraction (fraction of box area/space covered by disks)

# convert packing fraction -> disk radius sigma, for N disks in a unit-area box:
#   eta = N * (pi * sigma^2) / 1.0   =>   sigma = sqrt(eta / (N*pi))
sigma = math.sqrt(eta / N / math.pi)

n_runs = 100   # how many independent successful configurations to generate

print('Note that this program might take a while!')

for run in range(n_runs):
    iterations, config = direct_disks(N, sigma)
    print('run', run)
    # n_iter counts the successful attempt too, so subtract 1 to report
    # only the number of FAILED attempts ("wipe-outs") before success
    print(iterations - 1, 'tabula rasa wipe-outs before producing the following configuration')
    print(config)
    print()