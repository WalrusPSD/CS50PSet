def main():
    user_input = input("Greeting: ")
    input_formatted = user_input.strip().lower()
    find(input_formatted)

def find(n):
    if "hello" in n:
        print("$0")
    elif n[0] == "h":
        print("$20")
    else:
        print("$100")
main()
