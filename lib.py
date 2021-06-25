class Meeting:
    name = ""
    day = ""
    start = ""
    end = ""
    first = ""
    always = ""

    def __init__(self, name = 0, day = 0, start = 0, end = 0, first = 0, always = 0) -> None:
        self.name = name
        self.day = day
        self.start = start
        self.end = end
        self.first = first
        self.always = always

    def toPrint(self) -> str:
        res = f"Name: {self.name}"
        res += f" | Day of the week: {self.day}"
        res += f" | Starting Hour: {self.start}"
        res += f" | Ending hour: {self.end}"
        res += f" | First Loadout: {self.first}"
        res += f" | Every time loadout: {self.always}"

        return res

    def toRegister(self):
        res = ""
        res += self.name + "|"
        res += self.day + "|"
        res += self.start + "|"
        res += self.end + "|"
        res += self.first + "|"
        res += self.always

        return res

    def equals(self, meeting):
        return meeting.toPrint() == self.toPrint()