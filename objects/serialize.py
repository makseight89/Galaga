import constans as c


def serialize_to_txt(score):
    data = {"value": score.value}
    with open(c.TXT_FILE_PATH, "a") as file:
        file.write(str(data) + "\n")


def deserialize_from_txt():
    try:
        with open(c.TXT_FILE_PATH, "r") as file:
            data = file.read()
            print(f"Type of data is {type(data)}")
            print(f"{data=}")
    except FileNotFoundError as e:
        print(f"Error: File not found: {c.TXT_FILE_PATH}")
