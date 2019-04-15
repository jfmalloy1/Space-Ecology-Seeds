import csv

def find_seeds(species_abbrev, domain ,seeds):
    with open("seeds.dat", "w") as outfile:
        for s in seeds[0]:
            outfile.write(s + " ",)


def file_analysis():
    #list species abbreviations and domains
    species_abbrev = []
    domain = []
    #seeds for each organism (will be a 2D array)
    seeds = [[] for i in range(478)]
    with open("s1.txt") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter="\t")
        lc = 0
        for line in csv_reader:
            #line 9 - species abbreviation
            if (lc == 9):
                #starting at 6th element (avoiding labels)
                species_abbrev = line[5:]
            #line 10 - domain
            if (lc == 10):
                domain = line[5:]
            #find seed sets for each organism
            if (lc >= 14):
                for s in range(len(line)):
                    if (s > 5) and (float(line[s]) > 0):
                        seeds[s-6].append(line[0])
            lc += 1
        return species_abbrev, domain, seeds

def main():
    species_abbrev, domain, seeds = file_analysis()
    find_seeds(species_abbrev, domain ,seeds)

if __name__ == "__main__":
    main()
