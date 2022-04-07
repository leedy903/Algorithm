/*
 * EXAMPLE
 */

#include <iostream>
#include <vector>

using namespace std;

#define MAX 987654321
#define INF 987654321

int n;  // number of cities
double dist[MAX][MAX];  // array to save the distance between the two cities
// path: path which made until now
// visited: visiting checklist
// currentLength: path's length which made until now
// return the shortest path's length among the pathes which will visit rest of the city
double shortestPath(vector<int>& path, vector<bool>& visited, double currentLength) {
    if(path.size() == n) {
        return currentLength + dist[path[0]][path.back()];
    }
    double ret = INF;
    for(int next = 0; next < n; ++next) {
        if(visited[next]) continue;
        int here = path.back();
        path.push_back(next);
        visited[next] = true;
        // recursion
        double cand = shortestPath(path, visited, currentLength + dist[here][next]);
        ret = min(ret, cand);
        visited[next] = false;
        path.pop_back();
    }
    return ret;
} 