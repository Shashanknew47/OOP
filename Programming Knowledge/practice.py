from functools import reduce


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f'{k}={v}' for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_

        args_str = ','.join(all_args)

        print('{0} ({1}) took {2:.6f}s to run.'.format(
            fn.__name__, args_str, elapsed))

        return result

    return inner


@timed
def add(a, b):
    return a+b


def calfre(n):
    if n <= 2:
        return 1
    else:
        return calfre(n-1) + calfre(n-2)


@timed
def fab_calfre(n):
    return calfre(n)


di = {}


def calfrememo(n):
    if n in di:
        return di[n]
    elif n <= 2:
        di[n] == 1
        return 1
    else:
        x = calfrememo(n-1) + calfrememo(n-2)
        return x


@timed
def fab_calfrememo(n):
    return calfrememo


fab_calfre(37)
fab_calfrememo(37)
