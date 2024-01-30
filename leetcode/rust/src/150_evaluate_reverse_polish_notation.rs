impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = vec![];
        for token in tokens {
            match token.as_str() {
                "+" | "-" | "*" | "/" => {
                    let b = stack.pop().unwrap();
                    let a = stack.pop().unwrap();
                    match token.as_str() {
                        "+" => stack.push(a + b),
                        "-" => stack.push(a - b),
                        "*" => stack.push(a * b),
                        "/" => stack.push(a / b),
                        _ => {}
                    }
                }
                _ => stack.push(token.parse::<i32>().unwrap()),
            }
        }
        stack[0]
    }
}