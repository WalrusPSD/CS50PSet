def main():
    extension_input = input("File name: ")
    extension(extension_input)

def extension(extension_input):
    input_split = extension_input.split(".")
    concat = input_split[-1]
    lower_concat = concat.strip().lower()
    join(lower_concat)

def join(concat):
    if concat == "gif":
        print("image/gif")
    elif concat == "jpg" or concat == "jpeg":
        print("image/jpeg")
    elif concat == "png":
        print("image/png")
    elif concat == "pdf":
        print("application/pdf")
    elif concat == "txt":
        print("text/plain")
    elif concat == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")
main()
