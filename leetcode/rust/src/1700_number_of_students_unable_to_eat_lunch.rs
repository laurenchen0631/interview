impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {
        let mut students = students.into_iter().rev().collect::<Vec<i32>>();
        let mut sandwiches = sandwiches.into_iter().rev().collect::<Vec<i32>>();
        let mut i = 0;
        while i < students.len() {
            if students.last().unwrap() == sandwiches.last().unwrap() {
                students.pop();
                sandwiches.pop();
                i = 0;
            } else {
                let student = students.pop().unwrap();
                students.insert(0, student);
                i += 1;
            }
        }
        students.len() as i32
    }
}