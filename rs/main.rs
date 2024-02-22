// BOGO sort
// BOGO sort is a sorting algorithm that shuffles the list until it is sorted.
// The average time complexity is O(n*n!)
// The worst case is O(∞)

use rand::seq::SliceRandom;
use std::io;

fn is_sorted(arr: &[i32]) -> bool {
    for i in 1..arr.len() {
        if arr[i - 1] > arr[i] {
            return false;
        }
    }
    true
}

fn bogo_sort(arr: &mut [i32]) {
    while !is_sorted(arr) {
        arr.shuffle(&mut rand::thread_rng());
    }
}

fn main() {
    // read user input
    let mut list: Vec<i32> = Vec::new();
    println!("Enter input (1 element/line): ");
    loop {
        let mut x = String::new();
        io::stdin().read_line(&mut x).expect("Failed to read line");
        let x = x.trim();
        if x == "done" || x == "exit" {
            break;
        } else {
            match x.parse::<i32>() {
                Ok(n) => list.push(n),
                Err(_) => println!("Invalid input, try again"),
            }
        }
    }

    // start sorting
    bogo_sort(&mut list);
    println!("Sorted array: {:?}", list);
}
