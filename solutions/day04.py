import re

def has_fields(p):
    required = {"byr","iyr","eyr","hgt","hcl","ecl","pid"}
    return required & set(p) == required

def valid_fields(p):
    matches = { # today I felt like regexing
        "byr": re.compile(r"(19[2-9]\d|200[0-2])"),
        "iyr": re.compile(r"20(1\d|20)"),
        "eyr": re.compile(r"20(2\d|30)"),
        "hgt": re.compile(r"(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)"),
        "hcl": re.compile(r"#[0-9a-f]{6}"),
        "ecl": re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)"),
        "pid": re.compile(r"\d{9}")
    }
    return all([ matches[k].fullmatch(p[k]) for k in matches ])

if __name__ == "__main__":
    passports = []
    passport = {}
    with open("day04.input") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                for values in line.split(" "):
                    k,v = values.split(":")
                    passport[k] = v
            else:
                passports.append(passport)
                passport = {}
        if passport:
            passports.append(passport)
    
    
    valid = len([ p for p in passports if has_fields(p) ])
    print(valid)

    valid = len([ p for p in passports if has_fields(p) and valid_fields(p) ])
    print(valid)