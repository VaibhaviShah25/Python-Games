// Program for a simple calculator
#include <iostream>
using namespace std;
int main () {
int n1,n2,res;
cout << "************************************" << "\n";
cout << "\t" << "SIMPLE CALCULATOR" << "\n";
cout << "************************************" << "\n";
cout << "Enter first number : ";
cin >> n1;
cout << "Enter second number : ";
cin >> n2;
cout << "\n" << "<><><><><><><><><><><><><><><><><><>" << "\n";
res = n1 + n2;
cout << "Sum is " << res << "\n";
res = n1 - n2;
cout << "Difference is " << res << "\n";
res = n1 * n2;
cout << "Product is " << res << "\n";
res = n1 / n2;
cout << "Division is " << res << "\n";
cout << "************************************";
return 0;
}
