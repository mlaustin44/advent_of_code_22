#include<fstream>
#include<iostream>
#include<vector>
#include<string>

using namespace std;
typedef vector<vector<int>> tmap;

vector<string> parseInput(string fName) {
    vector<string> treeMap;
    string line;
    fstream file = fstream(fName);
    if (file.is_open()) {
        while(getline(file, line)) {
            treeMap.push_back(line);
        }
        file.close();
    }

    return treeMap;
}

void checkVisibility(int r, int c, vector<string>& treeMap, tmap& vMap) {
    int nRow = treeMap.size();
    int nCol = treeMap[0].size();

    if (vMap[r][c] == 1 || vMap[r][c] == 0) {
        return;
    }

    // check each direction until we find visibility
    // left
    for (int i=(c-1); i >= 0; i--) {
        if (vMap[r][i] == -1) { checkVisibility(r, i, treeMap, vMap); }

        if (vMap[r][i] == 1) { //neighbor is visible
            if (treeMap[r][c] > treeMap[r][i]) {
                vMap[r][c] = 1;
                return;
            } else {
                vMap[r][c] = 0;
                break;
            }
        } else if (vMap[r][i] == 0) {
            if (treeMap[r][c] < treeMap[r][i]) { 
                vMap[r][c] = 0;
                break; 
            }
        } 
    }
    // right
    for (int i=(c+1); i < nCol; i++) {
        if (vMap[r][i] == -1) { checkVisibility(r, i, treeMap, vMap); }

        if (vMap[r][i] == 1) { //neighbor is visible
            if (treeMap[r][c] > treeMap[r][i]) {
                vMap[r][c] = 1;
                return;
            } else {
                vMap[r][c] = 0;
                break;
            }
        } else if (vMap[r][i] == 0) {
            if (treeMap[r][c] < treeMap[r][i]) { 
                vMap[r][c] = 0;
                break; 
            }
        } 
    }
    // up
    for (int i=(r+1); i < nRow; i++) {
        if (vMap[i][c] == -1) { checkVisibility(i, c, treeMap, vMap); }

        if (vMap[i][c] == 1) { //neighbor is visible
            if (treeMap[r][c] > treeMap[i][c]) {
                vMap[r][c] = 1;
                return;
            } else {
                vMap[r][c] = 0;
                break;
            }
        } else if (vMap[i][c] == 0) {
            if (treeMap[r][c] < treeMap[i][c]) { 
                vMap[r][c] = 0;
                break; 
            }
        }
    }
    // down
    for (int i=(r-1); i >= 0; i--) {
        if (vMap[i][c] == -1) { checkVisibility(i, c, treeMap, vMap); }

        if (vMap[i][c] == 1) { //neighbor is visible
            if (treeMap[r][c] > treeMap[i][c]) {
                vMap[r][c] = 1;
                return;
            } else {
                vMap[r][c] = 0;
                break;
            }
        } else if (vMap[i][c] == 0) {
            if (treeMap[r][c] < treeMap[i][c]) { 
                vMap[r][c] = 0;
                break; 
            }
        }
    }
}

int solvePart1(vector<string> treeMap) {
    int nVisible = 0;
    int nRow = treeMap.size();
    int nCol = treeMap[0].size();

    vector<vector<int>> vMap(
        nRow,
        vector<int>(nCol, -1)
    );

    // fill in the border trees (which are always visible)
    for(int i=0; i<nRow; i++){
        vMap[i][0] = 1;
        vMap[i][nCol - 1] = 1;
    }
    for(int j=0; j<nCol; j++){
        vMap[0][j] = 1;
        vMap[nRow - 1][j] = 1;
    }

    for(int i=1; i<nRow; i++) {
        for (int j=0; j<nCol; j++) {
            checkVisibility(i, j, treeMap, vMap);
        }
    }

    for (auto& row : vMap) {
        for (auto& elem : row) {
            nVisible += elem;
        }
    }

    return nVisible;
}

int main(int argc, char* argv[]) {
    vector<string> input = parseInput(argv[1]);
    int part1soln = solvePart1(input);
    cout << "Part 1 solution is: " << part1soln << "\n";
}