#!/usr/bin/python3

# The names of the binary should be with reference to the main repo directory (..)
def algs():
    return {
        'reno': {
            'binary': './generic-cong-avoid/target/debug/reno',
            'args': '--ipc=netlink',
        },
        'cubic': {
            'binary': './generic-cong-avoid/target/debug/cubic',
            'args': '--ipc=netlink',
        },
        # TODO add your algorithm below.
        # the name you pick should not have '-' in it
    }
