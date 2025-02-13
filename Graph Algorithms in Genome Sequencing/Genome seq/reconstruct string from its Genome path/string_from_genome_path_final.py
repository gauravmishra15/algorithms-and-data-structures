# Python3
import sys

class geneReconstruction:

    
    def __init__(self, contents):

        self.contents = contents
        self.contentsLen = len(contents)

    def newString(self):

        string = self.contents[0]  # starts the return string with the first full kmer
        for i in range(1, self.contentsLen, 1):
            string += self.contents[i][-1]  # adds the last nt from each of the following kmers to build the string
        return string


def main():

    # contents = ['ACCGA', 'CCGAA', 'CGAAG', 'GAAGC', 'AAGCT']  # sample input
    contents = []
    for line in sys.stdin:  # takes STDIN only
        contents.append(line.replace('\n', ''))  # adds each line in file to a list
    geneRecon = geneReconstruction(contents)
    print(geneRecon.newString())


if __name__ == '__main__':
    main()