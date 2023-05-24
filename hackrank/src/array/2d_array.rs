use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

fn hourglassSum(arr: &[Vec<i32>]) -> i32 {
    let mut res = std::i32::MIN;
    for i in 0..4 {
        for j in 0..4 {
            let sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                + arr[i+1][j+1]
                + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2];
            if sum > res {
                res = sum;
            }
        }
    }
    
    res
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let mut arr: Vec<Vec<i32>> = Vec::with_capacity(6_usize);

    for i in 0..6_usize {
        arr.push(Vec::with_capacity(6_usize));

        arr[i] = stdin_iterator.next().unwrap().unwrap()
            .trim_end()
            .split(' ')
            .map(|s| s.to_string().parse::<i32>().unwrap())
            .collect();
    }

    let result = hourglassSum(&arr);

    writeln!(&mut fptr, "{}", result).ok();
}
