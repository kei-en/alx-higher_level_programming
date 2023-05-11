#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    """Prints all the names defined in hidden_4 module"""

    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
