// AoC 2022 Day 1 - M Austin

#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

vector<vector< int >> parseInput(string inFile) {
    //read in the input file
    vector<vector<int>> elves;
    vector<int> cals;
    string line;
    fstream file = fstream(inFile);
    if (file.is_open()) {
        while (getline(file, line)) {
            if (line == "") {
                elves.push_back(cals);
                cals.clear();
            } else {
                cals.push_back(stoi(line));
            }
        }
        elves.push_back(cals);
        file.close();
    }
    return elves;
}

int solvePart1(vector<vector<int>> input) {
    int maxCals = 0;
    for (auto& elf : input) {
        int elfSum = 0;
        for (auto& food : elf) {
            elfSum += food;
        }
        if (elfSum > maxCals) { maxCals = elfSum; }
    }
    return maxCals;
}

int solvePart2(vector<vector<int>> input) {
    vector<int> sumCals;
    for (auto& elf : input) {
        int elfSum = 0;
        for (auto& food : elf) {
            elfSum += food;
        }
        sumCals.push_back(elfSum);
    }
    sort(sumCals.begin(), sumCals.end());
    reverse(sumCals.begin(), sumCals.end());
    return (sumCals[0] + sumCals[1] + sumCals[2]);
}

int main(int argc, char* argv[]) {
    auto parsed = parseInput(argv[1]);
    int part1soln = solvePart1(parsed);
    int part2soln = solvePart2(parsed);
    cout << "Part 1 solution: " << part1soln << "\n";
    cout << "Part 2 solution: " << part2soln << "\n";
    return 0;
}