# Making a circle.

#==============================================================
잘못 생각했던 아이디어:
1. theta의 범위를 계속 지정하려고함.
2. x와 y를 정의하고, return으로 식을 받아내려함. (return으로 equation을 받을 수 없음!)
3. plot은 리스트로 뽑아내서 그리는 것이 좋음. 나는 x^2 + y^2 = 1 이라는 함수를 만들어서 돌리려 했음. 
   f(x) = x^2 + 1 은 돌아가지만, 
   y까지 변수의 제곱인 경우는 plotting을 할 수 없음!
===============================================================#


function C(theta) # theta = list
    for x in theta # theta는 list 이므로 list 자체의 범위를 constraint 할 수 없음. 
        if x < 0 || x > 2*pi # list 안에 있는 원소들의 범위를 지정하기 위해 for loop을 씀.
            println("Error!")
            exit(1)
        end
    end
    
    x = [cos(i) for i in theta] # x = cos(theta) 값을 리스트로 뽑기.
    y = [sin(i) for i in theta]
    return x, y
end

# 접선의 방정식
# : x1*x + y1*y = 1

function T(theta)
    x = [-2:0.001:2...]
    x1 = cos(theta)
    y1 = sin(theta)
    y = [(1 - x1*t)/y1 for t in x]
    return x, y
end

using PyPlot

function main()
    theta = [0:0.001:2*pi...]
    A, B = C(theta)
    print("각을 입력하세요.")
    th = readline(STDIN)
    P, Q = T(float(th))
    figure(figsize=(7,7), dpi=300)
    title("circle")
    xlabel("X")
    ylabel("Y")
    plot(A, B)
    plot(P, Q)
    axis([-2, 2, -2, 2])
    savefig("plot.png")
end

main()     