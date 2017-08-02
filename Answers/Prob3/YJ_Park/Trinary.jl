type Trinary
    A::Int64
end

function add(a::Trinary, b::Trinary)::Trinary
    c = Trinary(0)
    c.A = (a.A + b.A)%3
    return c
end

function mul(a::Trinary, b::Trinary)::Trinary
    c = Trinary(0)
    c.A = (a.A * b.A)%3 
    return c
end

function square(a::Trinary)::Trinary
    return mul(a,a)
end



