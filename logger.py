def log_message(message):
    with open("log.txt", "a") as f:
        f.write(message + "\n")
