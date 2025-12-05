#include <bits/stdc++.h>
using namespace std;

// Function to check if the given string is a comment or not
void isComment(string line)
{
    // Check for single-line comment
    if (line.size() >= 2 && line[0] == '/' && line[1] == '/' && (line.size() == 2 || line[2] != '/')) {
        cout << "It is a single-line comment";
        return;
    }

    // Check for multi-line comment
    if (line.size() >= 4 && line[0] == '/' && line[1] == '*' &&
        line[line.size() - 2] == '*' && line[line.size() - 1] == '/') {
        cout << "It is a multi-line comment";
        return;
    }

    cout << "It is not a comment";
}

int main()
{
    string line = "/*GeeksForGeeks GeeksForGeeks*/";

    isComment(line);

    return 0;
}
