// AoC 2022 Day 2 - M Austin

#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>


using namespace std;

#define ROCK 1
#define PAPER 2
#define SCISSORS 3

int scoreMatch(int thierMove, int yourMove) {
    int outcome = 0;
    // check for draws
    if (thierMove == yourMove) {
        outcome = 3;
    } else if (thierMove == 1) { //move1 is rock
        outcome = (yourMove == 2) ? 6 : 0;
    } else if (thierMove == 2) { //move1 is paper
        outcome = (yourMove == 3) ? 6 : 0;
    } else if (thierMove == 3) { //move1 is scissors
        outcome = (yourMove == 1) ? 6 : 0;
    }
    return (outcome + yourMove); //need to add the points for the original move
}

int letterToValue(char c) {
    switch (c) {
        case 'X':
        case 'A':
            return 1;
        case 'Y':
        case 'B':
            return 2;
        case 'Z':
        case 'C':
            return 3;
    }
    return INT_MIN;
}

vector<vector< int >> parseInput(string inFile) {
    //read in the input file
    vector<vector<int>> moves;
    vector<int> row;
    string line;
    fstream file = fstream(inFile);
    if (file.is_open()) {
        while (getline(file, line)) {
            row.push_back(letterToValue(line[0]));
            row.push_back(letterToValue(line[2]));
            moves.push_back(row);
            row.clear();
        }
        file.close();
    }
    return moves;
}

int main(int argc, char* argv[]) {
    int totalScore = 0;
    
    auto input = parseInput(argv[1]);
    for (auto& row : input) {
        totalScore += scoreMatch(row[0], row[1]);
    }
    cout << totalScore << "\n";
}