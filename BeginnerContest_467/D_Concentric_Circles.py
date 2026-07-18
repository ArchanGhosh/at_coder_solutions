T = int(input())

cases = []

for _ in range(T):
    px, py, qx, qy, rx, ry, sx, sy = map(int, input().split())
    
    cases.append({
        "px": px,
        "py": py,
        "qx": qx,
        "qy": qy,
        "rx": rx,
        "ry": ry,
        "sx": sx,
        "sy": sy
    })

for case in cases:
    dx1 = case["qx"] - case["px"]
    dy1 = case["qy"] - case["py"]

    dx2 = case["sx"] - case["rx"]
    dy2 = case["sy"] - case["ry"]

    cross = dx1 * dy2 - dy1 * dx2

    if cross != 0:
        print("Yes")
    else:
        ddx = (case["rx"] + case["sx"]) - (case["px"] + case["qx"])
        ddy = (case["ry"] + case["sy"]) - (case["py"] + case["qy"])

        dot = ddx * dx1 + ddy * dy1

        if dot == 0:
            print("Yes")
        else:
            print("No")
