#python3
import sys


class OverlapCollection:

    def __init__(self, seqs):
        """constructor: saves the sequences list"""
        self.seqs = seqs

    def collection(self):
        """ finds overlapping sequences and prints the pairs"""
        overlap = []  # list to hold pairs of overlapping sequences
        for i in range(0, len(self.seqs), 1):
            first = self.seqs[i]  # saves the primary sequence
            for j in range(0, len(self.seqs), 1):
                if first[1:] == self.seqs[j][0:-1]:  # gets the overlapping seq only if overlap is off by 1nt
                    second = self.seqs[j]
                    overlap.append(first + " -> " + second)  # formatting for printing
        overlap.sort()  # sorts by alphabetical by the primary seq
        for i in overlap:
            print(i)


def main():

    contents = []
    for line in sys.stdin:  # takes STDIN only
        contents.append(line.replace('\n', ''))  # adds each line in file to a list
    construct = OverlapCollection(contents)
    construct.collection()


if __name__ == '__main__':
    main()