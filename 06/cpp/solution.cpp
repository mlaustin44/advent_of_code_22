#include <fstream>
#include <iostream>
#include <string>
#include <set>

using namespace std;

string parseInput(string fName) {
    string line;
    fstream file = fstream(fName);
    if (file.is_open()) {
        getline(file, line);
        file.close();
    }
    return line;
}

int solvePart1(string input) {
    for (int i=4; i<input.size(); i++) {
        // a set _only_ contains unique objects
        set<char> window(input.begin() + i - 4, input.begin() + i);
        // so if the set size is 4, we know all the elements are unique
        if (window.size() == 4) { return i; }
    }
    return -1;
}

int main(int argc, char* argv[]) {
    string input = parseInput(argv[1]);
    int part1soln = solvePart1(input);
    cout << "Part 1 solution is: " << part1soln << "\n";
}