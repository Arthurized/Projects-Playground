def one():
    """Two objects move in straight lines at constant velocities on a plain.
    Object 1 starts at (x₁, y₁) with v₁; Object 2 starts at (x₂, y₂) with v₂.
     Find the earliest time at which the distance between them is the smallest."""

    k1 = list(map(int, input().split())) # start position of object 1
    v1 = list(map(int, input().split())) # velocity of object 1
    k2 = list(map(int, input().split())) # start position of object 2
    v2 = list(map(int, input().split())) # velocity of object 2
    if v1[0] == v2[0] and v1[1] == v2[1]:
        print(0)
        return
    r = 10 ** 30
    l = 0
    ansl = ((k2[0] - k1[0]) ** 2 + (k2[1] - k1[1]) ** 2) ** 0.5
    qx1 = k1[0] + v1[0] * r
    qy1 = k1[1] + v1[1] * r
    qx2 = k2[0] + v2[0] * r
    qy2 = k2[1] + v2[1] * r
    ansr = ((qx2 - qx1) ** 2 + (qy2 - qy1) ** 2) ** 0.5
    while r - l > 0.0000001:
        mid = (r + l) / 2
        qx1 = k1[0] + v1[0] * mid
        qy1 = k1[1] + v1[1] * mid
        qx2 = k2[0] + v2[0] * mid
        qy2 = k2[1] + v2[1] * mid
        d = ((qx2 - qx1) ** 2 + (qy2 - qy1) ** 2) ** 0.5
        if d <= ansl and d <= ansr:
            if ansl > ansr:
                l = mid
                ansl = d
            else:
                r = mid
                ansr = d
        elif d <= ansl:
            l = mid
        else:
            r = mid
    print(l)

one()
