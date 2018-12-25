fn main() {

    let mut a = 1;
    let mut b = 2;
    let mut c = 0;
    let mut sum = 2;

    while true {
        c = a + b;
        if c >= 4_000_000 {
            break;
        }
        if c % 2 == 0 {
            sum += c;
        }
        a = b;
        b = c;
    }
        
    println!("{}", sum);
}
