# Variable-Encoding
A simple and space efficient arbitrary length variable encoding scheme

In all variable length encodings I've seen, the length of the code grows with some multiple of the length of the message. This approach is more space efficient, with the length of the message encoded in binary recursively. 

# Background

The goal is to create a lossless (injective) encoding scheme that maps bitstrings to bitstrings. The constraint is that not only should a message be recoverable from its encoding, but a sequence of messages should be recoverable from the concatenated sequence of its encodings. The identity function doesn't satisfy this constraint because, e.g. the sequence '010' could be the encoding of ['0','10'] or ['01','0']. 

# This Scheme

The idea of this scheme is to encode each message as [prefix] + [message] + [continue]. [message] is the message itself, [continue] is a bit set to 0 at the end of the message, and [prefix] encodes the length of the message (in binary) recursively, using the scheme itself. The only difference is that encodings occuring in the prefex use a [continue] bit of 1, so that the decoder knows it just read the length of the next section, not the actual content of the message.

The length of the next segment is always positive, so [prefix] can be an encoding of the length of the next segment without the leading 1. This allows the algorithm to terminate, since a length 1 segment has length [1], and when we get rid of the leading 1, this becomes the empty string. So the first bit of every encoding is always the continue bit. If the encoding is [0], the message is the empty string and the decoder can move on to the next message in the sequence.

