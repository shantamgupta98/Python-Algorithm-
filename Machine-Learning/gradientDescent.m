function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)

m = length(y);
J_history = zeros(num_iters, 1);
theta1 = theta(1);
theta2 = theta(2);
disp(theta);

for iter = 1:num_iters
  h=X * theta;
  J_history(iter) = computeCost(X, y, theta);
  theta1 = theta1-alpha*sum((h-y).*X(:,1))/m;
  theta2 = theta2-alpha*sum((h-y).*X(:,2))/m;
  theta(1)=theta1;
  theta(2)=theta2;

end

end
