function Harmonic(n)
    h = "hbar"
    E_n = (1/2 + n) # regardless without ()
    if n < 0
        print("error!")
        exit(1)
    end
    return "$E_n$h" # 앞에 $는 위에 지정한 문자를 받아옴, h가 string 이므로 string 안에 앞에 지정한 문자를 받아옴.
end

function Real(E_n)
    hbar = 6.582119514*1e-16
    E_n = E_n[1:end-4]
    return float(E_n)*hbar
end

function main()
    print("n을 입력하세요: ")
    #n = readline(STDIN) #
    E_n = Harmonic(float(n))
    println(E_n)
    println(Real(E_n))
end

main()