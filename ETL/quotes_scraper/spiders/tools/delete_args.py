class ReplaceW:
    def __init__(self, contents):
        self.contents = contents

    def word_modify(self):
        self.contents = self.contents.replace(',', '')
        self.contents = self.contents.replace('.', '')
        self.contents = self.contents.replace('·', '')
        self.contents = self.contents.replace(':', '')
        self.contents = self.contents.replace(';', '')
        self.contents = self.contents.replace('"', '')
        self.contents = self.contents.replace("'", '')
        self.contents = self.contents.replace("-", '')
        self.contents = self.contents.replace('_', '')
        self.contents = self.contents.replace('–', '')
        self.contents = self.contents.replace("\n", '')
        self.contents = self.contents.replace('\\', '')
        self.contents = self.contents.replace('  ', ' ')
        self.contents = self.contents.replace('[', '')
        self.contents = self.contents.replace(']', '')
        self.contents = self.contents.replace('(', '')
        self.contents = self.contents.replace(')', '')
        self.contents = self.contents.replace('{', '')
        self.contents = self.contents.replace('}', '')
        self.contents = self.contents.replace('*', '')
        self.contents = self.contents.replace('“', '')
        self.contents = self.contents.replace('”', '')
        self.contents = self.contents.replace('¿', '')
        self.contents = self.contents.replace('?', '')
        self.contents = self.contents.replace('<', '')
        self.contents = self.contents.replace('>', '')
        self.contents = self.contents.replace('VEA EL VIDEO', '')
        self.contents = self.contents.replace('VEA LA ENTREVISTA', '')
        return self.contents