#include <iostream>
#include <string>
#include <cstdlib>   // exit
using namespace std;

int addr = 100;

// Produce three-address code for assignment:  a = b
void handleAssignment(const string &expr) {
    size_t pos = expr.find('=');
    if (pos == string::npos) {
        cout << "Invalid assignment expression.\n";
        return;
    }
    string lhs = expr.substr(0, pos);
    string rhs = expr.substr(pos + 1);
    // trim whitespace (simple)
    auto trim = [](string s) {
        size_t a = s.find_first_not_of(" \t");
        if (a == string::npos) return string("");
        size_t b = s.find_last_not_of(" \t");
        return s.substr(a, b - a + 1);
    };
    lhs = trim(lhs);
    rhs = trim(rhs);

    cout << "Three address code:\n";
    cout << "t = " << rhs << '\n';
    cout << lhs << " = t\n";
}

// Find the first operator of any from ops in the string and return index or npos
size_t find_first_of_ops(const string &s, const string &ops) {
    for (size_t i = 0; i < s.size(); ++i)
        if (ops.find(s[i]) != string::npos) return i;
    return string::npos;
}

// Produce three-address code for a single-step arithmetic operation with simple precedence
void handleArithmetic(string expr) {
    // Remove spaces
    string e;
    for (char c : expr) if (c != ' ' && c != '\t') e.push_back(c);

    // precedence: first '*' and '/', then '+' and '-'
    size_t pos = find_first_of_ops(e, "*/");
    if (pos == string::npos) pos = find_first_of_ops(e, "+-");

    if (pos == string::npos || pos == 0 || pos == e.size() - 1) {
        cout << "Invalid arithmetic expression.\n";
        return;
    }

    string left = e.substr(0, pos);
    char op = e[pos];
    string right = e.substr(pos + 1);

    cout << "Three address code:\n";
    cout << "t = " << left << ' ' << op << ' ' << right << '\n';
    cout << "result = t\n";
}

// Produce three-address code for relational expressions and generate conditional labels
void handleRelational(const string &id1, const string &op, const string &id2) {
    // validate operator:
    const string validOps[] = {"<", ">", "<=", ">=", "==", "!="};
    bool ok = false;
    for (auto &v : validOps) if (op == v) { ok = true; break; }
    if (!ok) {
        cout << "Expression error: invalid relational operator\n";
        return;
    }

    cout << '\n';
    cout << addr << "\tif " << id1 << " " << op << " " << id2 << " goto " << (addr + 3) << '\n';
    addr++;
    cout << addr << "\tT := 0\n";
    addr++;
    cout << addr << "\tgoto " << (addr + 2) << '\n';
    addr++;
    cout << addr << "\tT := 1\n";
    // addr stays at last used (optional)
}

int main() {
    int ch;
    while (true) {
        cout << "\n1. assignment\n";
        cout << "2. arithmetic\n";
        cout << "3. relational\n";
        cout << "4. Exit\n";
        cout << "Enter the choice: ";
        if (!(cin >> ch)) break;

        if (ch == 1) {
            cout << "Enter the expression with assignment operator (example: x=a+b): ";
            string exp;
            // consume newline then read full line
            cin >> ws;
            getline(cin, exp);
            if (exp.empty()) { cout << "Empty input.\n"; continue; }
            handleAssignment(exp);
        }
        else if (ch == 2) {
            cout << "Enter the expression with arithmetic operator (example: a+b or a*b+c): ";
            string ex;
            cin >> ws;
            getline(cin, ex);
            if (ex.empty()) { cout << "Empty input.\n"; continue; }
            handleArithmetic(ex);
        }
        else if (ch == 3) {
            cout << "Enter the relational expression (example: a <= b): ";
            string id1, op, id2;
            // read three tokens (operator can be <=, >=, ==, !=)
            cin >> id1 >> op >> id2;
            handleRelational(id1, op, id2);
        }
        else if (ch == 4) {
            cout << "Exiting.\n";
            exit(0);
        }
        else {
            cout << "Invalid choice.\n";
        }
    }

    return 0;
}
