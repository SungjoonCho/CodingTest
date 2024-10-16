// 장애물 인식 프로그램 (Softeer)

#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int N;
vector<int> answer;
int visited[26][26];

string mat[26];

int dys[4] = {0,-1,0,1};
int dxs[4] = {1,0,-1,0};

struct COORD{
    int y;
    int x;
};

bool in_range(int y, int x){
    return 0<=y && y<N && 0<=x && x<N;
}

int bfs(int r, int c){

    int cnt = 0;

    queue<COORD> q;
    q.push({r,c});
    visited[r][c] = 1;
    cnt++;

    while(q.size() > 0){
        COORD curItem = q.front();
        q.pop();

        int cy = curItem.y;
        int cx = curItem.x;

        for(int i=0; i<4; i++){
            int ny = cy + dys[i];
            int nx = cx + dxs[i];

            if(in_range(ny, nx) == false || visited[ny][nx] == 1 || mat[ny][nx] == '0'){
                continue;
            }

            q.push({ny,nx});
            visited[ny][nx] = 1;
            cnt++;      
        }

            
    }
    // cout << cnt << endl;

    return cnt;
}
        
        


int main(int argc, char** argv)
{
    cin >> N;

    
    for(int i=0; i<N; i++){
        cin >> mat[i];
    }

    // visited 초기화
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            visited[i][j] = 0;
        }
    }

    // for(int i=0; i<N; i++){
    //     cout << mat[i] << endl;
    // }


    // 하나씩 확인
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(mat[i][j] == '1' && visited[i][j] == 0){
                answer.push_back(bfs(i,j));
            }
        }
    }
    
    sort(answer.begin(), answer.end());

    cout << answer.size() << endl;
    for(int i=0; i<answer.size(); i++){
        cout << answer[i] << endl;
    }

    return 0;
}
