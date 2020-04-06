import sys
from scipy.special import comb 

# cases = open("/content/drive/My Drive/Colab Notebooks/ML_hw2_data/coin2.txt", "r")
cases = open(sys.argv[1], "r")
a = int(sys.argv[2])
b = int(sys.argv[3])
for i, case in enumerate(cases):
    case = case.replace('\n',"")
    m = case.count('1')
    N = len(case)
    P = m/N
    likelihood = comb(N, m) * P**m * (1-P)**(N-m)

    print("case {i}: {case}".format(i=i+1, case=case))
    print("Likelihood:{L}".format(L=likelihood))
    print("Beta prior:     a:{a}, b:{b}".format(a=a, b=b))
    a += m
    b += N-m
    print("Beta posterior: a:{a}, b:{b}\n".format(a=a, b=b))   