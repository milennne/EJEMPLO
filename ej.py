from timeit import default_timer  as timer

n=10**3
start=timer()
for i in range (0,n):
    for j in range (0,n):
        print(f"i={i} and j={j}")
        #pass

end=timer()
proc_time=end-start
print(f"Processing time -> {proc_time}")