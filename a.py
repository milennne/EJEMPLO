from timeit import default_time as timer

def logarithms(n):
    i=1
    while i<=n:
        i=i+2
        print(i)
        #pass

n=10**3
start=timer()
logarithms(n)
end=timer()

proc_time=end
print(f"Processing time -> {proc_time}")
