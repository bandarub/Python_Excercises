def create_tuple(x: int, y: int, z: int):
    small = min(x,y,z)
    big = max(x,y,z)
    return (small, big , x+y+z)

    

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

