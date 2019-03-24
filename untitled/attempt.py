# returns the hand that givenhand can defeat
def winsagainst(givenhand):
    answers = dict({"R": "S", "P": "R", "S": "P"})
    return answers.get(givenhand)


# returns the winning hand of a Rock paper scissors match
def getwinner(handa, handb):
    if handa != handb:
        return handa if handb == winsagainst(handa) else handb
    else:
        return None


def handformationchange(n, a, formations):
    if n == 1:
        return 0
    else:
        formations = list(formations)
        roundwinners = list()
        autowinner = formations[n - 1] if (n % 2) else None
        handchange = 0
        poiposchange = 0
        if autowinner is not None:
            n -= 1

        for x in range(0, n - 1, 2):
            if (x == a) or ((x + 1) == a):
                poi = x if a % 2 == 0 else x + 1
                other = x + 1 if poi == x else x
                oldhand = formations[poi]
                formations[poi] = winsagainst(formations[other])
                if oldhand is not None and oldhand != formations[poi]:
                    handchange = 1

            winner = getwinner(formations[x], formations[x + 1])
            if winner is not None:
                roundwinners.append(winner)
                poiposchange += 1 if x < a else 0
            else:
                poiposchange += 2 if x < a else 0

        if autowinner is not None:
            roundwinners.append(autowinner)
        print("Round winners %s and POI at %d" % (formations, a))
        return handchange + handformationchange(len(roundwinners), a - poiposchange, roundwinners)


def main():
    newFormations = "PPSRP"
    newFormations = list(newFormations)
    a = 2
    n = 6
    newFormations.insert(a ,None)
    print(handformationchange(n, a, newFormations))


if __name__ == '__main__':
    main()
