#!/usr/bin/env bash
CURDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

source $CURDIR/lib/libdir

sudo python $LIBDIR/listener.py --pin=19