import csv

#Find seeds within each domain
def domain_seeds(seeds, domain, d):
    d_seeds = []
    #loop through all seeds
    for i in range(len(seeds)):
        #if a seed is from a particular domain
        if domain[i] == d:
            for s in seeds[i]:
                #make sure it is not already in overall seed set
                if s not in d_seeds:
                    #append to seed set for that particular domain
                    d_seeds.append(s)
    return (d_seeds)

#General function to return seeds
def find_seeds(species_abbrev, domain ,seeds):
    #list of all seeds (no repeats)
    all_seeds = []
    with open("all_seeds.txt", "w") as outfile:
        for s in seeds:
            for c in s:
                if c not in all_seeds:
                    all_seeds.append(c)
                #all seeds written to a file
                outfile.write(c + " ",)
            outfile.write("\n")

    #bacteria seeds (nonoverlapping)
    return all_seeds, domain_seeds(seeds, domain, "Bacteria"), domain_seeds(seeds, domain, "Archaea"),domain_seeds(seeds, domain, "Animals")

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

def write_files(seeds, name):
    with open(name, "w") as outfile:
        for s in seeds:
            outfile.write(s + " ",)

def prep_netexp(seeds):
    return

def main():
    species_abbrev, domain, seeds = file_analysis()
    #seeds for bacteria, archaea, and eukaroya domains
    all_seeds, b_seeds, a_seeds, e_seeds = find_seeds(species_abbrev, domain ,seeds)
    write_files(all_seeds, "all_compounds.txt")
    write_files(b_seeds, "bacteria.txt")
    write_files(a_seeds, "archaea.txt")
    write_files(e_seeds, "animals.txt")

    #make seed sets (6 organisms - randomly select two from each domain)
    


if __name__ == "__main__":
    main()
