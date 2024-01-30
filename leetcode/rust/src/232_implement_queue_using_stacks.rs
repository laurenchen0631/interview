struct MyQueue {
    stack: Vec<i32>,
    q_stack: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {
    fn new() -> Self {
        MyQueue {
            stack: Vec::new(),
            q_stack: Vec::new(),
        }
    }
    
    fn push(&mut self, x: i32) {
        self.stack.push(x);
    }

    fn transfer_stack(&mut self) {
        while !self.stack.is_empty() {
            self.q_stack.push(self.stack.pop().unwrap());
        }
    }
    
    fn pop(&mut self) -> i32 {
        if self.q_stack.is_empty() {
            self.transfer_stack();
        }
        self.q_stack.pop().unwrap()
    }
    
    fn peek(&mut self) -> i32 {
        if self.q_stack.is_empty() {
            self.transfer_stack();
        }
        *self.q_stack.last().unwrap()
    }
    
    fn empty(&self) -> bool {
        self.stack.is_empty() && self.q_stack.is_empty()
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */