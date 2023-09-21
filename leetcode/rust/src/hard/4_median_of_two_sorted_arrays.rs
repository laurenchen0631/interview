impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let m = nums1.len();
        let n = nums2.len();

        if (m + n) % 2 == 0 {
            return (Self::find_kth(&nums1, &nums2, (m + n) / 2) + Self::find_kth(&nums1, &nums2, (m + n) / 2 - 1)) as f64 / 2.0;
        } else {
            return Self::find_kth(nums1.as_slice(), nums2.as_slice(), (m + n) / 2) as f64;
        }
    }

    fn find_kth(nums1: &[i32], nums2:  &[i32], k: usize) -> i32 {
        if nums1.is_empty() {
            return nums2[k];
        }
        if nums2.is_empty() {
            return nums1[k];
        }

        let m = nums1.len() / 2;
        let n = nums2.len() / 2;
        if m + n < k {
            if nums1[m] > nums2[n] {
                return Self::find_kth(nums1, &nums2[n + 1..], k - n - 1);
            }
            else {
                return Self::find_kth(&nums1[m + 1..], nums2, k - m - 1);
            }
        }
        else {
            if nums1[m] > nums2[n] {
                return Self::find_kth(&nums1[..m], nums2, k);
            }
            else {
                return Self::find_kth(nums1, &nums2[..n], k);
            }
        }

    }
}