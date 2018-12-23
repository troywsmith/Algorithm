def isPrime(n)
    # if n < 2
    #     return false
    # elsif (n>2 and n%2=0)
    #     return false
    # else return 
    i=2
    loop do
        if n%i==0
            puts i
            puts false
        end
        i+=1
        break if i==1000
        
    end
end


isPrime(3)