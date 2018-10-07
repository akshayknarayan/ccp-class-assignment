extern crate clap;
extern crate generic_cong_avoid;
extern crate portus;
#[macro_use]
extern crate slog;
extern crate your_code; // TODO change

use your_code::YourAlg;

// TODO you will have to modify this function to call your algorithm
fn main() {
    let matches = clap::App::new("Your_Name")
        .version("0.1.0")
        .author("someone")
        .arg(clap::Arg::with_name("num-connections")
             .long("num-connections")
             .required(true))
        .get_matches();

    let num_conns: u32 = matches.value_of("num-connections").unwrap().parse().unwrap();
    let logger = portus::algs::make_logger();
    info!(logger, "Starting Your_Name";
        "num-connections" => num_conns,
    );

    generic_cong_avoid::start::<YourAlg>("netlink", logger, Default::default());
}
