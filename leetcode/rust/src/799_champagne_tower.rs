impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let mut query_row = query_row as usize;
        let mut tower = vec![vec![0.0; query_row+1]; query_row+1];
        tower[0][0] = poured as f64;

        for r in 0..query_row + 1 {
            for c in 0..r + 1 {
                let q = (tower[r][c] - 1.0) / 2.0;
                if q > 0.0 {
                    tower[r + 1][c] += q;
                    tower[r + 1][c + 1] += q;
                }
            }
        }

        return tower[query_row][query_glass as usize].min(1.0);
    }
}