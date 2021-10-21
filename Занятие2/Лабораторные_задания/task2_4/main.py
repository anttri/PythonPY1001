if __name__ == "__main__":
    phrase = 'Hello,world'
    hi = len(phrase)
    count_stairs = range(hi)
    for index in count_stairs:
        print(' ' * (index + 5), phrase[index])


