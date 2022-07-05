/*
Skeleton code for linear hash indexing
*/

#include <string>
#include <ios>
#include <fstream>
#include <vector>
#include <string>
#include <string.h>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <cmath>
#include "classes.h"

using namespace std;

int main() {
    
    char input;
    LinearHashIndex emp_index("EmployeeIndex");
    // Loop to lookup IDs until user is ready to quit
    while (true)
    {
        int inputStr;
        int flag = 0;
        cout << "Please choose query type l:look up record, c:create index , e:exit"
             << "\n";
        cin >> input;
        switch (input)
        {
        case 'c':
        case 'C':
            emp_index.createFromFile("Employee.csv");
            cout << "Index file Generated!"
                 << "\n";
            break;
        case 'l':
        case 'L':
            cout << "Enter employee ID"
                 << "\n";
            cin >> inputStr;
            emp_index.findRecordById(inputStr);
            break;
        case 'E':
        case 'e':
            flag = 1;
            break;
        default:
            break;
        }
        if (flag == 1)
        {
            break;
        }
    }

    return 0;

}

