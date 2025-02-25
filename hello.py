counter = 0

def get_hello():
    global counter
    counter += 1
    return f"Hello, Windsurf! (Shown {counter} times)"

if __name__ == "__main__":
    print(get_hello())
