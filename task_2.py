class Version:
    def __init__(self, version):
        self.version = version
        self.version_int = 0
        self.STRING_WORTH = {"a": 1, "b": 2, "alpha": -20, "beta": -10, "r": -50}
        self.version_to_int()

    def version_to_int(self):
        main_part, suffix = "", ""
        if "-" in self.version:
            main_part, suffix = self.version.split("-")
            suffix = suffix.replace("rc", "r")
        else:
            main_part = self.version
        main_part, suffix = main_part.split("."), suffix.split(".")
        # Process main part
        self.version_int += int(main_part[0]) * 100
        if int(main_part[1]) < 10:
            self.version_int += int(main_part[1]) * 10
        else:
            self.version_int += int(main_part[1])
        for symbol in main_part[2]:
            if symbol.isalpha():
                self.version_int += self.STRING_WORTH[symbol] * 0.1
            else:
                self.version_int += int(symbol) * 0.1
        # Process suffix part
        if suffix != [""]:
            for symbol in suffix:
                if symbol.isalpha():
                    self.version_int += self.STRING_WORTH[symbol] * 0.1
                else:
                    self.version_int += int(symbol) * 0.1

    def __eq__(self, other):
        return self.version_int == other.version_int

    def __ne__(self, other):
        return self.version_int != other.version_int

    def __le__(self, other):
        return self.version_int <= other.version_int

    def __ge__(self, other):
        return self.version_int >= other.version_int

    def __lt__(self, other):
        return self.version_int < other.version_int

    def __gt__(self, other):
        return self.version_int > other.version_int


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for version_1, version_2 in to_test:
        Version(version_1).version_to_int
        Version(version_2).version_to_int
    assert Version(version_1) < Version(version_2), "le failed"
    assert Version(version_2) > Version(version_1), "ge failed"
    assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()
