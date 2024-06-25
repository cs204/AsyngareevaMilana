def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    p = input()
    c = convert(p)
    print(c)

if __name__ == "__main__":
    main()
