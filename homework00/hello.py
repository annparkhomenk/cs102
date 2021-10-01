def get_greeting(name: str) -> str:
    if name == "World":
        return "Hello, World!"
    elif name == "Anonymous":
        return "Hello, Anonymous!"


if __name__ == "__main__":
    message = get_greeting("World")
    print(message)
