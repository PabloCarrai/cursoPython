def mayordedos(v, v1):
    if v > v1:
        return v
    else:
        if v1 > v:
            return v1


def menordedos(v, v1):
    if v < v1:
        return v
    else:
        if v1 < v:
            return {v1}
