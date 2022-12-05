#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

struct elfPair {
    int elf1start;
    int elf1end;
    int elf2start;
    int elf2end;
};

vector< elfPair> parseInput(string inFile) {
    //read in the input file
    vector<elfPair> input;
    string line;
    fstream file = fstream(inFile);
    if (file.is_open()) {
        while (getline(file, line)) {
            elfPair currentPair;
            // parse the input by splitting on symbols
            // could be done cleaner with a regex
            auto commaPos = line.find(',');
            auto hyphen1pos = line.find('-');
            auto hyphen2pos = line.find('-', commaPos);
            currentPair.elf1start = stoi(line.substr(0,hyphen1pos));
            currentPair.elf1end = stoi(line.substr(hyphen1pos+1, commaPos));
            currentPair.elf2start = stoi(line.substr(commaPos+1,hyphen2pos));
            currentPair.elf2end = stoi(line.substr(hyphen2pos+1, line.size()));
            input.push_back(currentPair);
        }
        file.close();
    }
    return input;
}

int solvePart1(vector<elfPair> input) {
    int containedCount = 0;
    for (auto& pair : input) {
        if ( // case where elf2 is totally contained in elf1
            (pair.elf2start >= pair.elf1start) && 
            (pair.elf2end <= pair.elf1end)) {
                containedCount++;
        } else if (
            (pair.elf1start >= pair.elf2start) &&
            (pair.elf1end <= pair.elf2end)) {
                containedCount++;
        }
    }
    return containedCount;
}

int solvePart2(vector<elfPair> input) {
    int overlapCount = 0;

    for (auto& pair : input) {
        vector<int> cleaned(100, 0);
        for (int i=pair.elf1start; i<pair.elf1end+1; i++) {
            cleaned[i] += 1;
        }
        for (int j=pair.elf2start; j<pair.elf2end+1; j++) {
            cleaned[j] += 1;
        }
        for (int k=0; k<100; k++) {
            if (cleaned[k] > 1) { 
                overlapCount++;
                break;
            }
        }
    }
    return overlapCount;
}

int main(int argc, char* argv[]) {
    auto input = parseInput(argv[1]);
    auto part1soln = solvePart1(input);
    cout << "Part 1 solution: " << part1soln << "\n";
    auto part2soln = solvePart2(input);
    cout << "Part 2 solution: " << part2soln << "\n";

}