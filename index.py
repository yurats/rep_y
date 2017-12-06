import os

class index():
    def __init__(self):
        self.dictionary = {}
        self.fnames = list(filter(lambda x: ".txt" in x, os.listdir()))

    def generate_index(self):
        for fname in self.fnames:
            f = open(fname, "r")
            f_line = f.read()
            f_list = f_line.split()
            for word in f_list:
                if word in self.dictionary:
                    if fname in self.dictionary[word]:
                        self.dictionary[word][fname] += 1
                    else:
                        self.dictionary[word][fname] = 1
                else:
                    self.dictionary[word] = {fname: 1}
        dd = self.dictionary
        for word in dd:
            for fname in self.fnames:
                if fname not in self.dictionary[word]:
                    self.dictionary[word][fname] = 0

    def query(self, string = "aaa sss"):
        word_list = string.split()
        fnames_score = []
        for fname in self.fnames:
            fscore = 1
            for word in word_list:
                if word in self.dictionary:
                    fscore *= (self.dictionary[word][fname])
                else:
                    fscore = 0
            fnames_score += [[fname, fscore]]
        fnames_score.sort(key = lambda x: x[1])
        return fnames_score
def main():
    obj = index()
    obj.generate_index()
    x = obj.query("aaa sss")
    print(x[-1])

if __name__ == "__main__":
    main()