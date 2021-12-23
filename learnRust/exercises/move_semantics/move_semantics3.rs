// move_semantics3.rs
// Make me compile without adding new lines-- just changing existing lines!
// (no lines with multiple semicolons necessary!)
// Execute `rustlings hint move_semantics3` for hints :)

fn main() {
    let mut vec0 = Vec::new();

    fill_vec(&mut vec0);

    println!("{} has length {} content `{:?}`", "vec1", vec0.len(), vec0);

    vec0.push(88);

    println!("{} has length {} content `{:?}`", "vec0", vec0.len(), vec0);
}

fn fill_vec(vec: &mut Vec<i32>){
    vec.push(22);
    vec.push(44);
    vec.push(66);
}
