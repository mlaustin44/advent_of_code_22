#include <memory>
#include <vector>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

struct File {
    string name;
    int size;
};

struct Directory {
    shared_ptr<Directory> parent;
    vector<shared_ptr<Directory>> subDirs;
    vector<File> files;
    int size;
    string name;
};

void parseLs(vector<string> contents, shared_ptr<Directory> parent) {
    for (auto& item : contents) {
        if (item[0] == 'd') { //it's a directory
            shared_ptr<Directory> dir = make_shared<Directory>();
            dir->parent = parent;
            dir->subDirs = vector<shared_ptr<Directory>>();
            dir->files = vector<File>();
            string dir_name = item.substr(4, item.size() - 4);
            dir->name = dir_name;
            parent->subDirs.push_back(dir);
        } else { // it's a file
            auto spaceLoc = item.find(' ');
            File file = {
                item.substr(spaceLoc, (item.size() - spaceLoc)),    //name
                stoi(item.substr(0, spaceLoc)), //size
            };
            parent->files.push_back(file);
        }
    }
}

void parseCmds(vector<string> cmds, shared_ptr<Directory> root) {
    shared_ptr<Directory> current_dir = root;
    int cmd_i = 1; // inputs always start with 'cd /'
    while (cmd_i < cmds.size()) {
        string cmd = cmds[cmd_i];
        string cmd_act = cmd.substr(2, 2);
        if (cmd_act == "ls") {
            vector<string> contents;
                cmd_i++;
                cmd = cmds[cmd_i];
                while (cmd[0] != '$') {
                    contents.push_back(cmd);
                    cmd_i++;
                    cmd = cmds[cmd_i];
                }
                parseLs(contents, current_dir);
                cmd_i--;
        } else if (cmd_act == "cd") {
            if (cmd[5] == '.') { //going up a level
                current_dir = current_dir->parent;
            } else {
                string target_dir = cmd.substr(5, (cmd.size() - 4));
                for (auto subdir : current_dir->subDirs) {
                    if (subdir->name == target_dir) {
                        current_dir = subdir;
                    }
                }
            }
            cmd_i++;
        } else {
            cmd_i++;
        }
    }
}

vector<string> parseInput(string fName) {
    vector<string> commands;
    string line;
    fstream file = fstream(fName);
    if (file.is_open()) {
        while(getline(file, line)) {
            commands.push_back(line);
        }

        file.close();
    }
    return commands;
}

int main(int argc, char* argv[]) {
    vector<string> input = parseInput(argv[1]);
    shared_ptr<Directory> root = make_shared<Directory>();
    root->name = "/";
    root->subDirs = vector<shared_ptr<Directory>>();
    root->files = vector<File>();
    parseCmds(input, root);
}