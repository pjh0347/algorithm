# Consider the polynomials
#
# f(x) = 0x^2 + 5*x + 3
# g(x) = 2x^2 + 1*x + 7
# h(x) = 15x^6 + 4x^3  ==>  {6: 15, 3: 4} 

# The product f(x)*g(x) is calculated as shown below:
#
# f(x) * g(x) = (5*x + 3) * (2x^2 + 1*x + 7)
#             = (5*x) * (2x^2 + 1*x + 7) + (3) * (2x^2 + 1*x + 7)
#             = (10x^3 + 5*x^2 + 35x) + (6x^2 + 3*x + 21)
#             = 10x^3 + 11x^2 + 38x + 21

# Create the function `poly_mult` that computes the following
#
# poly_mult({1:5, 0:3}, {2:2, 1:1, 0:7}) = {3:10, 2:11, 1:38, 0:21}


f_x = {1:5, 0:3} # A dictionary represents the 
                 # polynomial expresion: 5*x + 3
g_x = {0:7, 1:1, 2:2}

def poly_mult(f_x, g_x):
    result = {}
    for f in f_x.keys():
        for g in g_x.keys():
            k = f + g
            v = f_x[f] * g_x[g]
            print f, g, k, v
            if result.has_key(k):
                result[k] += v
            else:
                result[k] = v
    return result

print poly_mult(f_x, g_x)

