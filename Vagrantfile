$setup = <<-SCRIPT
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get -y install build-essential autoconf libtool libelf-dev
# Mahimahi dependencies
sudo apt-get -y install autotools-dev dh-autoreconf iptables protobuf-compiler libprotobuf-dev pkg-config libssl-dev dnsmasq-base ssl-cert libxcb-present-dev libcairo2-dev libpango1.0-dev iproute2 apache2-dev apache2-bin
# mm-live dependencies
sudo apt-get install -y npm
# iperf
sudo apt-get install -y iperf
# Rust bindgen dependencies
sudo apt-get -y install llvm-3.9-dev libclang-3.9-dev clang-3.9
curl https://sh.rustup.rs -sSf > rust.install.sh
chmod u+x ./rust.install.sh
chown vagrant:vagrant ./rust.install.sh
su -c "./rust.install.sh -y -v --default-toolchain nightly" vagrant
# mahimahi setup
sudo sysctl -w net.ipv4.ip_forward=1
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.post_up_message = ""\
    "Welcome to the CCP VM."\
    "Run `make run` to run the experiment."\
    "Add your own congestion control algorithm, and modify `scripts/exp.py` to run it"
  config.vm.synced_folder ".", "/ccp"
  config.vm.provision "shell", inline: $setup
end
