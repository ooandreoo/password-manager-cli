import csv

def read_active_passwords(rows=10, page=0):
    start = page * rows
    data = []
    with open("./data/passwords.csv", newline="") as f:
        reader = csv.DictReader(f)
        for _ in range(start):
            next(reader, None)
        count = 0
        for row in reader:
            if row["active"] == "1":
                count+=1
                data.append(row["platform"]+" | "+row["user"]+" | "+row["password"])
            if count == rows:
                break
    return data

def read_active_passwords_word_matched(word):
    data = []
    with open("./data/passwords.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["active"] == "1" and word.lower() in row["platform"].lower():
                data.append(row["platform"]+" | "+row["user"]+" | "+row["password"])
    return data

