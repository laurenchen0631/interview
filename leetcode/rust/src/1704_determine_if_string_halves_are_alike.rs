impl Solution {
    pub fn halves_are_alike(s: String) -> bool {
        let mut vowel_count = 0;
        for (i, c) in s.chars().enumerate() {
            if i < s.len() / 2 {
                if Self::is_vowel(c) {
                    vowel_count += 1;
                }
            } else {
                if Self::is_vowel(c) {
                    vowel_count -= 1;
                }
            }
        }
        vowel_count == 0
    }

    fn is_vowel(c: char) -> bool {
        match c {
            'a' | 'e' | 'i' | 'o' | 'u' => true,
            'A' | 'E' | 'I' | 'O' | 'U' => true,
            _ => false,
        }
    }
}