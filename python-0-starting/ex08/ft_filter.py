def ft_filter(function, iterable): 
    """Return an iterator yielding those items of iterable for which
    function(item) is true.  If function is None, return the items that
    are true."""
    if function is None: 
        for val in iterable:
            if val:
                yield val 
        return

    for s in iterable: 
        if function(s): 
            yield s 

def main():
    ft_filter()

if __name__=="__main__": 
     main() 