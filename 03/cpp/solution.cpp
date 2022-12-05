#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector< vector< char >> parseInput(string inFile) {
    //read in the input file
    vector<vector<char>> input;
    vector<char> pack;
    string line;
    fstream file = fstream(inFile);
    if (file.is_open()) {
        while (getline(file, line)) {
            for (int i = 0; i < line.size(); i++) {
                pack.push_back(line[i]);
            }
            input.push_back(pack);
            pack.clear();
        }
        file.close();
    }
    return input;
}

int itemToPriority(char c) {
    int ic = (int)c; // cast to int, get ASCII code
    if (ic < 91) { // upper case
        return (ic - 'A' + 27);
    } else { // lower case
        return (ic - 'a' + 1);
    }
    return -1;
}

int solvePart1(vector<vector<char>> input) {
    int part1score = 0;

    for (auto& pack : input) {
        int half = pack.size() / 2;
        // create a map of all the items in the second compartment of the pack
        unordered_map<char, int> backHalf;
        for (int i=half; i<pack.size(); i++) {
            backHalf[pack[i]] = 1;
        }
        // iterate through first compartment, checking if those items are present in the 2nd
        for (int i=0; i<half; i++) {
            auto found = backHalf.find(pack[i]);
            if (found != backHalf.end()) {
                part1score += itemToPriority(pack[i]);
                backHalf.erase(pack[i]); // hack to avoid double counting an item
            }
        }
    }

    return part1score;
}

int solvePart2(vector<vector<char>> input) {
    int part2score = 0;

    // iterate through lines 3 at a time
    for (int i=0; i<input.size(); i += 3) {
        // create 3 empty vectors, one per line, with an element per possible charecter (52)
        vector<vector<int>> counts;
        for (int i=0; i<3; i++) {
            vector<int> linecount(53, 0);
            counts.push_back(linecount);
        }
        // go through individual lines in the set
        for (int j=0; j < 3; j++) {
            vector<char> currentLine = input[i+j];
            // for each charecter in the line, set the corresponding array element to 1 (avoid double counting - 1 is max per line!)
            for (int k=0; k<currentLine.size(); k++) {
                int currentChar = itemToPriority(currentLine[k]);
                counts[j][currentChar] = 1;
            }
        }
        // for each charecter, if it was in all 3 lines in the set then add its value to the total score
        for (int k=0; k<=53; k++) {
            if (
                (counts[0][k] == 1) &&
                (counts[1][k] == 1) &&
                (counts[2][k] == 1)
            ) { part2score += k; }
        }
    }

    return part2score;
}

int main(int argc, char* argv[]) {
    auto input = parseInput(argv[1]);
    int part1soln = solvePart1(input);
    cout << "Part 1 solution: " << part1soln << "\n";
    int part2soln = solvePart2(input);
    cout << "Part 2 solution: " << part2soln << "\n";
}