class Filereader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "r")
        self._content = []

    def readline(self, line):
        return self.get_content()[line]

    def readlines(self, start, stop):
        return self.get_content()[start:stop]

    def get_length(self):
        return len(self.get_content())

    def get_content(self):
        if not self.file:
            return []
        if not self._content:
            self._content = self.file.read().splitlines()
        return self._content

    def close(self):
        if self.file:
            self.file.close()
