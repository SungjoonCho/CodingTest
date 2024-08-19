
#include <iostream>
#include <algorithm> => sort, unique 등등
#include<vector> => 자유롭게 indexing하고 수정, 맨 뒤에 추가하는 면에서 편함
#include<queue> => indexing은 방법 없는 것 같고, 선입선출 기능 구현에 편리함
#include<string>
#include<map> => 파이썬 딕셔너리랑 비슷 



시작할 때 main 문 안에 넣어주면 시간 단축에 좋다 함
ios::sync_with_stdio(false);
cin.tie(0);




배열 선언 : int arr[3];
vector 선언 : vector<int> v;
2차원 vector 선언 : vector<vector<int>> v;
queue 선언 : queue<int> q;



문자열 슬라이싱 : string.substr(i,3) // 시작 인덱스, 개수
단순히 str[i] 이렇게 해버리면 char가 반환되어서 string이랑 비교할 때 힘들 수 있음

문자열 비교 : == , > , < 
문자열 연결 : +

string to int => stoi(str)
    stod stof stol

int to string => to_string(a)

선언할 떄 주의
    long int
    unsigned long
    int 붙이나 안붙이나 상관없음

    double


배열에서 최대값 선택
int maximum = *std::max_element(arr, arr+n); // n은 원소 개수

vector에서 최대값 선택
int maximum = *std::max_element(vector.begin(), vector.end());

vector에서 최소값 선택
int maximum = *std::min_element(vector.begin(), vector.end());

최대 최소 비교
min(a,b) max(a,b)




절대값
abs(a)

나누기 (몫)
/ 만 해도 됨
int a = b/c 하면 어차피 int에 들어가니까 소수점 버려짐

나누기 (나머지)
% 




배열 sort (오름차순)
sort(arr, arr+n);

배열 sort (내림차순)
sort(arr, arr+n, greater<int>());




vector sort
sort(v.begin(), v.end());

vector sort (조건1, 2 있을 때)
bool compare(string a, string b){
    
    int size_a(a.size());
    int size_b(b.size());
    
    string tem_a = a;
    string tem_b = b;    
    
    // 문자열 길이 맞춰주기
    if(size_a != size_b){
        for(int i=1; i<size_b; i++){
            tem_a += a;
        }
        
        for(int i=1; i<size_a; i++){
            tem_b += b;
        }
    }
    
    return tem_a < tem_b;    
}
sort(v.begin(), v.end(), compare);




vector 사용법
v.push_back(a);
v[i] = 3;
v.erase(v.begin());
v.pop_back();
v.empty()
v.size()




queue 사용법
q.push(a);
q.pop();
q.empty()
q.size();
v.insert(v.begin()+i, cur);  => 원하는 인덱스 i 자리에 cur을 집어넣는다




아래처럼 구조체 이용해서 queue 만들면 좋음 y,x처럼 필요한거를 구조체에 추가만 하면 됨
struct COORD{
    int y;
    int x;
};
queue<COORD> q;
q.push({r,c});




map 사용법 (파이썬 딕셔너리랑 비슷)
map<string, vector<string>> myMap;
myMap[curStr].push_back(a);
myMap[curStr].erase(v.begin() + i);


