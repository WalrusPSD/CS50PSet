def main():
    face_input = input("Input test: ")
    convert(face_input)

def convert(face_input):
    face_input = face_input.replace(":)", "🙂")
    face_input = face_input.replace(":(", "🙁")
    print(face_input)

main()
