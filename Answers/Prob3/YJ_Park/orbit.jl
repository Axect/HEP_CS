const G= 6.67259e-11
const m = 5.9736e+24
const M = 1.9891e+30
const AU = 1.49597870691e+11
const tstep = 43200
const N = 730 * 10

using(PyPlot)

type Vector
    x::Float64
    y::Float64
    z::Float64
end

function Initialize()
    A = Vector(-9.851920196143998e-01 * AU, 1.316466809434336e-01 * AU, -4.877392224782687e-06 * AU)
    B = Vector(-9.864337701483683e-01 * AU, 1.230799243164879e-01 * AU, -4.374019384763304e-06 * AU)
    return A, B
end

function Plus(A::Vector, B::Vector)::Vector
    C = Vector(0,0,0)
    C.x = A.x + B.x
    C.y = A.y + B.y
    C.z = A.z + B.z
    return C
end

function Add(A::Vector, B::Vector)
    A.x += B.x
    A.y += B.y
    A.z += B.z
end

function Mul(A::Vector, F::Float64)::Vector
    B  = Vector(0,0,0)
    B.x = F * A.x
    B.y = F * A.y
    B.z = F * A.z
    return B
end

function Norm(A::Vector)::Float64
    return sqrt(A.x^2 + A.y^2 + A.z^2)
end

function Running(r::Vector, v::Vector)
    a = Mul(r, float(-G*M/(Norm(r)^3)))
    Add(v, Mul(a, float(tstep)))
    Add(r, Mul(v, float(tstep)))
end

# kinetic energy
function Kinetic(v::Vector)::Float64
   return 1/2*m*Norm(v)^2
end

function Potential(r::Vector)::Float64
    return -G*M*m/Norm(r)
end

function Calc(i1::Vector, i2::Vector)
    C_x = zeros(N+1)
    C_y = zeros(N+1)
    C_z = zeros(N+1)
    KE = zeros(N+1)
    PE = zeros(N+1)
    TE = zeros(N+1)
    C_x[1] = i1.x; C_x[2] = i2.x ;
    C_y[1] = i1.y; C_y[2] = i2.y ;
    C_z[1] = i1.z; C_z[2] = i2.z ;
    PE[1] = Potential(i1); PE[2] = Potential(i2);
    v1 = Plus(Mul(i2, 1./tstep), Mul(i1, -1./tstep))
    KE[1] = Kinetic(v1)
    TE[1] = PE[1]+KE[1]
    r = i2; v=v1;
    #println(r.x/AU, v.x/AU)
    start = time()
    for i=3:N+1
        Running(r, v)
        C_x[i] = r.x ;
        C_y[i] = r.y ;
        C_z[i] = r.z ;
        KE[i-1] = Kinetic(v)
        PE[i] = Potential(r)
        TE[i-1] = KE[i-1]+PE[i-1]
    end
    Running(r, v)
    KE[N+1] = Kinetic(v)
    TE[N+1] = KE[N+1] + PE[N+1]
   elapsed = time() - start
    println("걸린시간 : ", elapsed)
    
    return C_x, C_y, C_z, KE, PE, TE
end

function main()
    i1, i2 = Initialize()
    C1_x, C1_y, C1_z, KE1, PE1, TE1 = Calc(i1, i2)
    l1, l2 = Vector(C1_x[N+1], C1_y[N+1], C1_z[N+1]), Vector(C1_x[N], C1_y[N], C1_z[N])
    C2_x, C2_y, C2_z, KE2, PE2, TE2 = Calc(l1, l2)

    R1 = Vector(C2_x[N+1], C2_y[N+1], C2_z[N+1])
    println("오차 : ",Plus(i1, Mul(R1, -1.)))

    T = [1:N+1...];
    figure(figsize=(10,6), dpi=600)
    plot(T, C1_x)
    plot(T, C1_y)
    plot(T, C1_z)
    xlabel("Time(12hour)")
    ylabel("Coordinate(m)")
    title("Orbit", fontsize=14)
    savefig("Orbit.png")

    figure(figsize=(10,6), dpi=600)
    plot(T, KE1)
    plot(T, PE1)
    plot(T,TE1)
    xlabel("Time(12hour)")
    ylabel("Energy")
    title("Orbit", fontsize=14)
    savefig("Energy.png")

    figure(figsize=(10,6), dpi=600)
    plot(T, C2_x)
    plot(T, C2_y)
    plot(T, C2_z)
    xlabel("Time(12hour)")
    ylabel("Coordinate(m)")
    title("Orbit", fontsize=14)
    savefig("Orbit_Reverse.png")

    figure(figsize=(10,6), dpi=600)
    plot(T, KE2)
    plot(T, PE2)
    plot(T,TE2)
    xlabel("Time(12hour)")
    ylabel("Energy")
    title("Orbit", fontsize=14)
    savefig("Energy_Reverse.png")
end
