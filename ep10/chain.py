x = 2.0
target = 6.0
w = 0.0

prediction = w * x
diff = prediction - target
mistake = diff * diff
print("forward: ", prediction, diff, mistake)

grad_mistake = 1.0
grad_diff = 2 * diff * grad_mistake
grad_prediction = 1.0 * grad_diff
grad_w = x * grad_prediction
print("backward:", grad_mistake, grad_diff, grad_prediction, grad_w)
