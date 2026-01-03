def main():
    scores = [80, 75, 90, 95, 88]
    total = sum(scores)
    average = total / len(scores)

    print("-main/master branch output-")
    print(f"scores: {scores}")
    print(f"sum: {total}")
    print(f"average: {average}")

if __name__ == "__main__":
    main()
