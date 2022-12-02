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

int scoreMatchPart1(int thierMove, int yourMove) {
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

int scoreMatchPart2(int thierMove, int result) {
    int score = 0;
    if (result == 1) { // lose
        if (thierMove == 1) { score += SCISSORS; } //rock, we pick scissors
        else if (thierMove == 2) { score += ROCK; } //paper, we pick rock
        else if (thierMove == 3) { score += PAPER; } //scissors, we pick paper
    } else if (result == 2) { // draw
        score += 3; //for a draw
        score += thierMove; //to get a draw, we need the same choice as them
    } else if (result == 3) { // win
        score += 6; // for a win
        if (thierMove == 1) { score += PAPER; } //rock, we pick paper
        else if (thierMove == 2) { score += SCISSORS; } //paper, we pick scissors
        else if (thierMove == 3) { score += ROCK; } //scissors, we pick rock
    }

    return score;
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
    auto input = parseInput(argv[1]);

    // Part 1
    int part1score = 0;
    for (auto& row : input) {
        part1score += scoreMatchPart1(row[0], row[1]);
    }
    cout << "Part 1 score is: " << part1score << "\n";
    // Part 2
    int part2score = 0;
    for (auto& row : input) {
        part2score += scoreMatchPart2(row[0], row[1]);
    }
    cout << "Part 2 score is: " << part2score << "\n";

}