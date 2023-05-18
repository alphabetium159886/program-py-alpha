import numpy as np
d = 0.0152
sigd = 0.03743
lambdaaa = 2 * d / 50
sigK = 0.3
E_lambda = np.sqrt((sigd/d)**2+(sigK/50)**2)/100
siglambda = lambdaaa * E_lambda

lambda_1 = lambdaaa + siglambda
lambda_2 = lambdaaa - siglambda

print("lambda = ", lambdaaa)
print("E_lambda = ", E_lambda)
print("sigma lambda = ", siglambda)
print("lambda pm sigma-lambda = ", lambda_1, lambda_2)



