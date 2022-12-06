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

int solve(string input, int windowSize) {
    for (int i=windowSize; i<input.size(); i++) {
        // a set _only_ contains unique objects
        set<char> window(input.begin() + i - windowSize, input.begin() + i);
        // so if the set size is 4, we know all the elements are unique
        if (window.size() == windowSize) { return i; }
    }
    return -1;
}

int main(int argc, char* argv[]) {
    string input = parseInput(argv[1]);
    int part1soln = solve(input, 4);
    cout << "Part 1 solution is: " << part1soln << "\n";
    int part2soln = solve(input, 14);
    cout << "Part 2 solution is: " << part2soln << "\n";
}