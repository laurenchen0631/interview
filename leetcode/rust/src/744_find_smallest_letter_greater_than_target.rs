pub fn next_greatest_letter(letters: Vec<char>, target: char) -> char {
    let i = letters.partition_point(|&c| c <= target);
    letters[i % letters.len()]
}