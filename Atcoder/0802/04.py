def calculate_final_tension(first_tension, presents):
    current_tension = first_tension

    for p, a, b in presents:
        if p >= current_tension:
            current_tension += a
        else:
            current_tension -= b
            if current_tension < 0:
                current_tension = 0
    return current_tension

def main():
    try:
        n = int(input())
        presents = []
        for _ in range(n):
            p, a, b = map(int, input().split())
            presents.append((p, a, b))

        q = int(input())
        for _ in range(q):
            x = int(input())
            final_tension = calculate_final_tension(x, presents)
            print(final_tension)
    except (EOFError, ValueError) as e:
        pass

if __name__ == "__main__":
    main()