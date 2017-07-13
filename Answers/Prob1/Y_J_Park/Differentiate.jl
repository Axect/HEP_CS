# using definition of diff.
function Diff(f, x)
    h = 1e-06
    return (f(x + h) - f(x))/h
end

function y(x)
    return x^2
end

println("when f(x) = sin(x) : ", Diff(sin, 0))
println("when f(x) = x^2 : ", Diff(y, 0))
println("when f(x) = exp(x) : ", Diff(exp, 0))
println("when f(x) = ln(x) : ", Diff(log, 0))

#function A(x)
#    h = 1e-09
#    return ((x+h)^2 - x^2)/h 
#end

#println(A(2))

#function f(x)
#    h = 1e-09
#    f(x) = x^2   
#    return (f(x + h) - f(x))/h
#end

#println(f(2))

# way to reduce the error
function Diff_2(f, x)
    h = 1e-06
    return (f(x + h) - f(x - h))/2h
end

println("when f(x) = sin(x) : ", Diff_2(sin, 0))
println("when f(x) = x^2 : ", Diff_2(y, 0))
println("when f(x) = exp(x) : ", Diff_2(exp, 0))
println("when f(x) = ln(x) : ", Diff_2(log, 0))