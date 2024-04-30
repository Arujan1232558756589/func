import itertools

# Define your data stream source (e.g., a generator function)
def data_stream():
    for i in itertools.count(1):
        yield i

# Define your processing steps
def filter_even_numbers(stream):
    for num in stream:
        if num % 2 == 0:
            yield num

def square_numbers(stream):
    for num in stream:
        yield num ** 2

def take_n(stream, n):
    return itertools.islice(stream, n)

# Create the pipeline
stream = data_stream()
pipeline = take_n(square_numbers(filter_even_numbers(stream)), 5)

# Execute the pipeline
for result in pipeline:
    print(result)