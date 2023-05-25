/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

fn dynamicArray(n: i32, queries: &[Vec<i32>]) -> Vec<i32> {
    let mut res: Vec<i32> = Vec::new();
    let mut arr: Vec<Vec<i32>> = vec![Vec::new(); n as usize];
    let mut last = 0;
    for query in queries {
        println!("{:?}", query);
        let t = *query.get(0).unwrap();
        let x = *query.get(1).unwrap();
        let y = *query.get(2).unwrap();

        let i = ((x ^ last) % n) as usize;
        if t == 1 {
            arr[i].push(y);
        }
        else {
            let j = (y as usize) % arr[i].len();
            last = arr[i][j];
            res.push(last);
        }
    }

    res
}
