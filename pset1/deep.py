def deep():
    choice = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    match choice.lower().strip():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

deep()
