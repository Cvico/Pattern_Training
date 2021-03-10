/*

  root -l -b -q 'pattern_dumper.cc("createdPatterns_MB.root")' > createdPatterns_MB.txt

  Currently used in CMSSW:
  root -l -b -q 'pattern_dumper.cc("PseudoBayesPatterns_uncorrelated_v0.root")' > PseudoBayesPatterns_uncorrelated_v0.txt

  Using Carlos' code:
  root -l -b -q 'pattern_dumper.cc("MBTrainTraining_uncorrelated.root")' > MBTrainTraining_uncorrelated.txt

*/

#include <vector>

using namespace std;

void pattern_dumper(TString file_name){

  TFile *file = new TFile(file_name);

  std::vector<std::vector<std::vector<int>>> *my_vec;

  my_vec = (std::vector<std::vector<std::vector<int>>>*) file->Get("allPatterns");

  for (int p = 0; p < my_vec->size(); ++p){

    std::vector<std::vector<int>> pattern;
    pattern = my_vec->at(p);

    std::vector<int> seeds;
    seeds = pattern.at(0);
    cout << "(" << seeds.at(0) << ", ";
    cout << seeds.at(1) << ", ";
    cout << seeds.at(2) << "), [";
    
    
    std::vector<std::vector<int>> hits;
    for (int i = 1; i < pattern.size(); ++i){
      hits.push_back(pattern.at(i));
      cout << "(" << hits.at(i-1).at(0) << ", ";
      cout << hits.at(i-1).at(1) << ", ";
      cout << hits.at(i-1).at(2) << "), ";
    }
    cout << "]" << endl;
  }
}
