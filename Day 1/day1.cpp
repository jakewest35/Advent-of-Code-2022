#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const* argv[]) {
  ifstream file("input.txt");
  string line = "";
  vector<int> totals;
  int sum = 0;
  while (file) {
    getline(file, line);
    if (line != "")
      sum += stoi(line);
    else {
      totals.push_back(sum);
      sum = 0;
    }
  }
  sort(totals.begin(), totals.end());
  int top_three_total = totals[totals.size() - 1] + totals[totals.size() - 2] +
                        totals[totals.size() - 3];
  cout << top_three_total << endl;

  return 0;
}
