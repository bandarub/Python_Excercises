def oldest_person(people: tuple):
    old = 2024
    per = ''
    for person in people:
        if old > person[1]:
            old = person[1]
            per = person[0]
    return per


    

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]
    print(oldest_person(people))

