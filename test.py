def _count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)

with open(r'./Data.txt', 'rb') as fp:
    c_generator = _count_generator(fp.raw.read)
    # count each \n
    line_count = sum(buffer.count(b'\n') for buffer in c_generator)


