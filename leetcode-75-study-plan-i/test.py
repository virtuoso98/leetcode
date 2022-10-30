def cross_product (s1, s2):
    sx1, sy1 = s1
    sx2, sy2 = s2
    return sx1 * sy2 - sx2 * sy1
def is_colinear (p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    cp = cross_product((x2 - x1, y2 - y1), (x3 - x1, y3 - y1))
    return cp == 0.0
def solution (X, Y):
    # write your code in Python 3.6
    if len(X) < 3:
        return []
    ix = 0
    # get the pairwise distance between the rest of the array and the chosen first point
    dists = [0 for i in range(len(X))]
    for i in range(1, len(X)):
        dist = ((X[i] - X[ix])  2 + (Y[i] - Y[ix])  2) ** 0.5
        dists[i] = dist
    # min0, min1 = dists[0], dists[1]
    # for i in range(len(dists)):
    #     dists[]
    # scan the remaining array twice to find the two points with the smallest pairwise distance to form
    # a triangle, while not breaching colinearity
    print(dists)
    ix1 = 1
    for i in range(2, len(dists)):
        if dists[i] < dists[ix1]:
            ix1 = i
    ix2 = 1
    for i in range(1, len(dists)):
        # check that point 2 is not the same as point 1, and three points aren't co-linear
        if dists[i] < dists[ix2] and ix2 != ix1 and (not is_colinear((X[ix], Y[ix]), (X[ix1], Y[ix1]), (X[ix2], Y[ix2]))):
            ix2 = i
    if ix1 == 1:
        i2_start = 2
    else:
        i2_start = 1
    ix2 = i2_start
    for i in range(i2_start, len(dists)):
        # check that point 2 is not the same as point 1, and three points aren't co-linear
        if (dists[i] < dists[ix2]) and (i != ix1) and (not is_colinear((X[ix], Y[ix]), (X[ix1], Y[ix1]), (X[ix2], Y[ix2]))):
            ix2 = i
    return [ix, ix1, ix2]