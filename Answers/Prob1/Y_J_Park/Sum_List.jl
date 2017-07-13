# List
List = [1:1e+08...]
# a loop expression
# s = 0
# for i in List
#     s += i
# end

#println(s)

# module
# A = sum(List)
# println(A)

#time for loop 10times
function F()
    start = time()
    s = 0
    for i in List
        s += i 
    end
    elapsed = time() - start
    return s, elapsed
end

s, _ = F()
t = 0
for j = 1:10 # range(1,10)
    _,elapsed = F()
    t += elapsed
end

println(s)
println("Time : ", t/10, "(10times)")

# taking time module
function M()
    start2 = time()
    A = sum(List)
    elapsed2 = time() - start2
    return A, elapsed2
end

A, _ = M()

t2 = 0
for k = 1:10
    _, elapsed2 = M()
    t2 += elapsed2
end

println(A)
println("Time : ", t2/10) 
