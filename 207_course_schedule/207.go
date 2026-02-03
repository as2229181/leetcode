func isCycleBfs(adj map[int][]int, V int, inDegree []int) bool {
    queue := []int{}
    count := 0
    for i, val := range inDegree{
        if val == 0 {
            queue = append(queue, i)
            count++
        }
    }
    for len(queue) > 0 {
        crs := queue[0]
        queue = queue[1:]
        for _ , v := range adj[crs]{
            inDegree[v] --
            if inDegree[v] == 0 {
                queue = append(queue, v)
                count ++
            }
        }
    }
    if count == V{
        return true
    }
    return false
}
func canFinish(numCourses int, prerequisites [][]int) bool {
    adj := make(map[int][]int)
    inDegree := make([]int, numCourses)
    for _, prereq := range(prerequisites) {
        crs := prereq[0]
        pre := prereq[1]
        adj[pre] = append(adj[pre], crs)
        inDegree[crs] ++
    }
    return isCycleBfs(adj, numCourses, inDegree)

}