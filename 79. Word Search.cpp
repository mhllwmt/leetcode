class Solution {
public:
    bool vis[201][201];
    const int dx[4] = {0, 0, -1, 1};
    const int dy[4] = {1, -1, 0, 0};
    bool exist(vector<vector<char>>& board, string word) {
        memset(vis, 0, sizeof(vis));
        if(board.size()==0)
            return false;
        for(int i=0; i<board.size(); i++)
            for(int j=0;j<board[0].size(); j++)
                if(dfs(board, word, i, j, 0))
                    return true;
        return false;
    }


    bool dfs(vector<vector<char>>& board, string word, int x, int y, int num){
        int dx[4] = {0, 0, -1, 1};
        int dy[4] = {1, -1, 0, 0};
        if (num == word.size())
            return true;
        vis[x][y] = 1;
        for (int i=0; i<4; i++) {
            int tx = x + dx[i];
            int ty = y + dy[i];
            if(tx>=0 && tx<board.size() && ty>=0 && ty<=board[0].size() && board[tx][ty] == word[num])
                if(dfs(board, word, tx, ty, num+1))
                    return true;
        }
        vis[x][y] = 0;
        return false;
    }
};