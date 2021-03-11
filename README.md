# Variable-Encoding
A simple and space efficient arbitrary length variable encoding scheme

In all variable length encodings I've seen, the length of the code grows with some multiple of the length of the message. This approach is more space efficient, with the length of the message encoded in binary recursively. 
