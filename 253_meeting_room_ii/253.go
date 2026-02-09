/**
 * Definition of Interval:
 * type Interval struct {
 *    start int
 *    end   int
 * }
 */

 func minMeetingRooms(intervals []Interval) int {
    start := make([]int, len(intervals))
    end := make([]int, len(intervals))

    for i, interval := range(intervals) {
        start[i] = interval.start
        end[i] = interval.end
    }
    sort.Ints(start)
    sort.Ints(end)

    count := 0
    end_pointer := 0

    for s:=0; s < len(start); s++ {
        if start[s] < end[end_pointer] {
            count ++
        } else {
           end_pointer ++
        }

    }
    return count
}
