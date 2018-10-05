extern crate generic_cong_avoid;
extern crate slog;

use generic_cong_avoid::{GenericCongAvoidAlg, GenericCongAvoidMeasurements};

// TODO rename me!
pub struct YourAlg;

impl GenericCongAvoidAlg for YourAlg {
    type Config = ();
    
    fn name() -> String {
        String::from("YourAlg")
    }

    fn new(_cfg: Self::Config, _logger: Option<slog::Logger>, _init_cwnd: u32, _mss: u32) -> Self {
        unimplemented!()
    }

    fn curr_cwnd(&self) -> u32 {
        unimplemented!()
    }

    fn set_cwnd(&mut self, _cwnd: u32) {
        unimplemented!()
    }

    fn increase(&mut self, _m: &GenericCongAvoidMeasurements) {
        unimplemented!()
    }

    fn reduction(&mut self, _m: &GenericCongAvoidMeasurements) {
        unimplemented!()
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn cwnd() {
        let mut x = YourAlg{};
        x.set_cwnd(42);
        assert_eq!(42, x.curr_cwnd());
    }
}
