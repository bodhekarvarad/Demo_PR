#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Trans {
public:
    char ip_state;
    char op_state;
    char ip_symb;
    Trans() : ip_state('\0'), op_state('\0'), ip_symb('\0') {}
};

int main() {
    int nos, ips, notr;
    char istate, fstate;
    vector<char> states;
    vector<char> ipsmb;
    vector<Trans> tr;

    cout << "Enter the no. of states: ";
    cin >> nos;
    states.resize(nos);
    for (int i = 0; i < nos; ++i) {
        cout << "Enter state " << i + 1 << ": ";
        cin >> states[i];
    }

    cout << "Enter initial state: ";
    cin >> istate;
    cout << "Enter final state: ";
    cin >> fstate;

    cout << "Enter no. of i/p symbol: ";
    cin >> ips;
    ipsmb.resize(ips);
    for (int i = 0; i < ips; ++i) {
        cout << "Enter i/p symbol " << i + 1 << ": ";
        cin >> ipsmb[i];
    }

    cout << "Enter no. of transitions: ";
    cin >> notr;
    tr.resize(notr);

    // consume the newline left in the buffer
    string line;
    getline(cin, line);

    for (int i = 0; i < notr; ++i) {
        cout << "Enter transition " << i + 1 << " (format examples: A a B  OR  A-a-B): ";
        getline(cin, line);

        // collect the non-space, non-dash characters
        vector<char> parts;
        for (char c : line) {
            if (c != ' ' && c != '\t' && c != '-') parts.push_back(c);
        }

        if (parts.size() >= 3) {
            tr[i].ip_state = parts[0];
            tr[i].ip_symb  = parts[1];
            tr[i].op_state = parts[2];
        } else {
            cout << "Invalid transition format. Please re-enter this transition.\n";
            --i; // repeat this index
        }
    }

    cout << "\nTransitions entered:\n";
    for (int i = 0; i < notr; ++i) {
        cout << tr[i].ip_state << " - " << tr[i].ip_symb << " -> " << tr[i].op_state << '\n';
    }

    cout << "\nEnter string: ";
    string s;
    cin >> s;

    // simulate
    char current = istate;
    size_t k = 0;
    while (k < s.size()) {
        bool moved = false;
        for (int i = 0; i < notr; ++i) {
            if (tr[i].ip_state == current && tr[i].ip_symb == s[k]) {
                current = tr[i].op_state;
                k++;
                moved = true;
                break; // restart scanning transitions for next symbol
            }
        }
        if (!moved) break; // no valid transition for current symbol
    }

    if (k == s.size() && current == fstate) {
        cout << "String is accepted.\n";
    } else {
        cout << "String is not accepted.\n";
    }

    return 0;
}
