clear all
clc
%%  导入数据
% （1）在工作区右键，点击新建（Ctrl+N)，输入变量名称为X
% （2）双击进入X，输入或拷贝数据到X
% （3）关掉这个窗口，点击X变量，右键另存为，保存为mat文件
% （4）注意，代码和数据要放在同一个目录下哦，且Matlab的当前文件夹也要是这个目录。
load matlab1.mat
%%  数据预处理_正向化
[n,m] = size(y);
disp(['共有' num2str(n) '个评价对象, ' num2str(m) '个评价指标']) 
Judge = input(['这' num2str(m) '个指标是否需要经过正向化处理，需要请输入1 ，不需要输入0：  ']);

if Judge == 1
    Position = input('请输入需要正向化处理的指标所在的列，例如[2,3,6]： '); %[2,3,4]
    disp('请输入需要处理的这些列的指标类型（1：极小型， 2：中间型， 3：区间型） ')
    Type = input('例如[1,3,2]：  '); %[2,1,3]
    % 注意，Position和Type是两个同维度的行向量
    for i = 1 : size(Position,2)%对每一列进行正向化处理
        y(:,Position(i)) = Positivization(y(:,Position(i)),Type(i),Position(i));
    % 第一个参数是要正向化处理的那一列向量 X(:,Position(i))
    % 第二个参数是对应的这一列的指标类型（1：极小型， 2：中间型， 3：区间型）
    % 第三个参数是告诉函数我们正在处理的是原始矩阵中的哪一列
    % 返回值返回正向化之后的指标
    end
    disp('正向化后的矩阵 X =  ')
    disp(y)
end

%% 数据预处理_标准化
Z = y ./ repmat(sum(y.*y) .^ 0.5, n, 1);
disp('标准化矩阵 Z = ')
disp(Z)

%% 指标权重赋值
disp("请输入是否需要增加权重向量，需要输入1，不需要输入0")
Judge = input('请输入是否需要增加权重： ');
if Judge == 1
    disp(['有多少个指标就输入多少个权重数(权重和为1)，如[0.25,0.25,0.5]']);
    weigh = input(['请输入输入' num2str(m) '个权重: ']);
        if abs(sum(weigh) - 1)<0.000001 && size(weigh,1) == 1 && size(weigh,2) == m   % 这里要注意浮点数的运算是不精准的。
        else
            weigh = input('你输入的有误，请重新输入权重行向量: ');
        end
else
    weigh = ones(1,m) ./ m ; %如果不需要加权重就默认权重都相同，即都为1/m
end

%% 计算与最大值的距离和最小值的距离，并算出得分
D_P = sum([(Z - repmat(max(Z),n,1)) .^ 2 ] .* repmat(weigh,n,1) ,2) .^ 0.5;   % D+ 与最大值的距离向量
D_N = sum([(Z - repmat(min(Z),n,1)) .^ 2 ] .* repmat(weigh,n,1) ,2) .^ 0.5;   % D- 与最小值的距离向量
S = D_N ./ (D_P+D_N);    % 未归一化的得分
disp('最后的得分为：')
stand_S = S / sum(S)% 归一化的得分
[sorted_S,index] = sort(stand_S ,'descend')%对得分进行排序并返回原来的位置
plot(sorted_S,'r-o')
xmin=1;xmax = size(sorted_S,1);
ymin = 0;ymax = max(sorted_S)+min(sorted_S);
axis([xmin xmax ymin ymax]); % 设置坐标轴在指定的区间
grid on
xlabel('方案');ylabel('分数');%坐标轴表示对bai象标签
title('TOPSIS算法最终评分排序')