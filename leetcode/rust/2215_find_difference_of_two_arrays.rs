use std::collections::HashSet;

impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        let set1 = nums1.iter().collect::<HashSet<_>>();
        let set2 = nums2.iter().collect::<HashSet<_>>();
        
        vec![
            set1.difference(&set2).map(|&x| *x).collect::<Vec<_>>(),
            set2.difference(&set1).map(|&x| *x).collect::<Vec<_>>()
        ]
    }
}

#[cfg(test)]
mod test {
    use super::Solution::find_difference;

    #[test]
    fn test_find_difference() {
        assert_eq!(find_difference(vec![1, 2, 3], vec![1, 2, 4]), vec![vec![3], vec![4]]);
        assert_eq!(find_difference(vec![1, 2, 3], vec![1, 2, 3]), vec![vec![], vec![]]);
        assert_eq!(find_difference(vec![1, 2, 3], vec![1, 2, 3, 4]), vec![vec![], vec![4]]);
        assert_eq!(find_difference(vec![1, 2, 3, 4], vec![1, 2, 3]), vec![vec![4], vec![]]);
    }
}