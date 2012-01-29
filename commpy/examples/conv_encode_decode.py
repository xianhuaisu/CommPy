#   Copyright 2012 Veeresh Taranalli <veeresht@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
from commpy.channelcoding.convcode import *

# =============================================================================
# Example showing the encoding and decoding of convolutional codes 
# =============================================================================

# G(D) corresponding to the convolutional encoder
generator_matrix = np.array([[05, 07]])

# Number of delay elements in the convolutional encoder
M = 2

# Traceback depth of the decoder
tb_depth = 5*(M + 1)

# Generate random message bits to be encoded
message_bits = np.random.randint(0, 2, 32)

# Encode message bits
coded_bits = convencode(message_bits, generator_matrix, M)

# Introduce bit errors (channel)
#coded_bits[4] = 0
#coded_bits[7] = 0

# Decode the received bits
decoded_bits = viterbi_decode(coded_bits, generator_matrix, M, tb_depth)
   
print "==== Message Bits ==="
print message_bits
print "==== Coded Bits ====="
print coded_bits
print "==== Decoded Bits ==="
print decoded_bits[tb_depth-1:]

