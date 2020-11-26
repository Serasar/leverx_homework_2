class Version:
    def __init__(self, version):
        self.version = version
        self.version_int = 0
        self.STRING_WORTH = {"a": 1, "b": 2, "alpha": -2, "beta": -1, "r": -5}
        self.MAJOR_WORTH = 100
        self.MINOR_WORTH = 10
        self.PATCH_WORTH = 0.1
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
        # Process major version
        self.version_int += int(main_part[0]) * self.MAJOR_WORTH
        # Process minor version
        if int(main_part[1]) < 10:
            self.version_int += int(main_part[1]) * self.MINOR_WORTH
        else:
            self.version_int += int(main_part[1])
        # Process patch version
        if main_part[2][-1].isalpha():
            self.version_int += self.STRING_WORTH[main_part[2][-1]] * self.PATCH_WORTH
            main_part[2] = main_part[2][:-1]
            self.version_int += int(main_part[2]) * self.PATCH_WORTH
        else:
            self.version_int += int(main_part[2]) * self.PATCH_WORTH
        # Process suffix part
        if suffix != [""]:
            for symbol in suffix:
                if symbol.isalpha():
                    self.version_int += self.STRING_WORTH[symbol] * self.PATCH_WORTH
                else:
                    self.version_int += int(symbol) * self.PATCH_WORTH

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
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()
