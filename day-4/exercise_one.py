import random


def main():
    random_side = random.randint(0, 1)
    if random_side == 1:
        print("Heads")
    else:
        print("Tails")


if __name__ == "__main__":
    main()
