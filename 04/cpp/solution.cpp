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
            auto commaPos = line.find(',');
            auto hyphen1pos = line.find('-');
            auto hyphen2pos = line.find('-', commaPos);
            currentPair.elf1start = stoi(line.substr(0,hyphen1pos));
            currentPair.elf1end = stoi(line.substr(hyphen1pos+1, commaPos));
            currentPair.elf2start = stoi(line.substr(commaPos+1,hyphen2pos));
            currentPair.elf2end = stoi(line.substr(hyphen2pos+1, line.size()));
            cout << currentPair.elf2end << "\n";
            input.push_back(currentPair);
        }
        file.close();
    }
    return input;
}

int main(int argc, char* argv[]) {
    auto input = parseInput(argv[1]);
    cout << input.size() << "\n";
}