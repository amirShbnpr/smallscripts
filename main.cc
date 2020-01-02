#include <iostream>
#include <fstream> 
#include <vector>
#include <iterator>
#include <string>
#include <algorithm>
#include <boost/algorithm/string.hpp> 
#include <cstdlib> 
using namespace std;

// a class to read a csv file
class CSVReader{
	string fileName;
	string delimeter;

	public:
		CSVReader(string filename, string delm=","):
			fileName(filename), delimeter(delm)
		{}

		vector<vector<string>> getData();
};
// Data Collector
vector<vector<string>> CSVReader::getData(){
	ifstream file(fileName);
	vector<vector<string>> datalist;
	string line = "";
	while (getline(file, line)){
		vector<string> vec;
		boost::algorithm::split(vec, line, boost::is_any_of(delimeter));
		datalist.push_back(vec);
	}
	file.close();
	return datalist;
}

int main(int argc, char* argv[]) { 
    CSVReader reader(argv[1]);
	std::vector<std::vector<std::string> > datalist = reader.getData();
	for(vector<string> vec : datalist){
		for(string data : vec){
			cout << data << " , ";
		}
		cout << endl;
	}
	return 0;
}