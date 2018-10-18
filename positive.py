def main():
    i = get_revenue()
    print(f"${i}")


def get_revenue():
    while True:
        n = int(input("Revenue: "))
        if n >= 0:
            return n


if __name__ == "__main__":
    main()
