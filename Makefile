all: build

########################################
# check that all the submodules are here
########################################

mahimahi/src/frontend/delayshell.cc ccp-kernel/libccp/ccp.h:
	$(error Did you forget to git submodule update --init --recursive ?)

#########################
# compile all the things!
#########################

clean:
	$(MAKE) -C ccp-kernel clean
	$(MAKE) -C mahimahi clean

ccp-kernel/ccp.ko:
	$(MAKE) -C ccp-kernel

mahimahi/configure:
	cd mahimahi && autoreconf -i

mahimahi/Makefile: mahimahi/configure
	cd mahimahi && ./configure

mahimahi/src/frontend/mm-delay: mahimahi/src/frontend/delayshell.cc mahimahi/Makefile
	$(MAKE) -C mahimahi

mahimahi: mahimahi/src/frontend/mm-delay
	sudo $(MAKE) -C mahimahi install

./generic-cong-avoid/target/debug/reno ./generic-cong-avoid/target/debug/cubic:
	cd generic-cong-avoid && cargo build

cubic: ./generic-cong-avoid/target/debug/cubic
reno: ./generic-cong-avoid/target/debug/reno 

# TODO
# if necessary, add a target to build your binary here
# and add your target to the build target below

build: ccp-kernel/ccp.ko mahimahi/src/frontend/mm-delay ./generic-cong-avoid/target/debug/reno

##################
# run experiments 
##################

results:
	mkdir -p results

run: build results
	python3 scripts/exp.py
