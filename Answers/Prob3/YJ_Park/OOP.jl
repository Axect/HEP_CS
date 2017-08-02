type Vector
    x::Float64
    y::Float64
    z::Float64
end

function Add(u::Vector, v::Vector)
   u.x += v.x
   u.y += v.y
   u.z += v.z
   return u
end

function Norm(u::Vector)
    return sqrt(u.x^2 + u.y^2 + u.z^2)
end

const G = 1
const M = 2
const m = 3
const h = 1e-04

function Mul(r::Vector, f::float64)
    r.x *= f
    r.y *= f
    r.z *= f
    return r
end

function Run(r::Vector, v::Vector, a::Vector)
    a = Mul(r, GM/(Norm(r))^3)
    v = Add(v, Mul(a, h))
    r = Add(r, Mul(v, h))
end

function Plus(u::Vector)
    u.x += 1
    u.y +=1
    u.z +=1
end

function main()
    A = Vector(1., 2., 3.)
    B = Vector(4., 5., 6.)
    println(A)
    Add(A, B)
    println(A)
    Plus(A)
    println(A)
end

main()

type Coor
    x::Int64
    y::Int64
end

function Sym(a::Coor)
    print("origin reflection: e, x-axis reflection: f, y-axis reflection: g → ")
    n = readline(STDIN)
    if n == "e"
        a.x = -a.x ;
        a.y = -a.y ;
    elseif n == "f"
        a.y = -a.y ;
    elseif n == "g"
        a.x = -a.x ;
    end
end

w = Coor(1,2)
Sym(w)
print(w)