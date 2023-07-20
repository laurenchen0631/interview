pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
    let mut stack = vec![];
    for n in asteroids {
        if n > 0 {
            stack.push(n);
            continue;
        }

        let mut exploded = false;
        while !stack.is_empty() && stack.last().unwrap() > &0 {
            let last = stack.pop().unwrap();
            if last >= -n {
                if last > -n {
                    stack.push(last);
                }
                exploded = true;
                break;
            }
        }

        if !exploded {
            stack.push(n);
        }
    }
    return stack;
}
