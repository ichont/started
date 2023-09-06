%data是n个对象、m个评价指标 n行m列数据
%data是唯一需要从外界输入的数据
function  result=SQ(data);
R = data;
[rows,cols]=size(R);   % 输入矩阵的大小,rows为行数（对象个数），cols为列数（指标个数）
 
Rmin = min(R);         %矩阵中最小行
Rmax = max(R);         %矩阵中最大行
A = max(R) - min(R);   %分母 矩阵中最大行减最小行
 
y = R - repmat(Rmin,rows,1);      %分子 R矩阵每一行减去最小行
for j = 1 : cols                  %该循环用于正向指标标准化处理 分子/分母
     y(:,j) = y(:,j)/A(j);
end
 
S = sum(y,1);                     %列之和（用于列归一化）
 
for i = 1 : cols                  %该循环用于列的归一化
    Y(:,i) = y(:,i)/S(i); 
end
 
Y;                                %打印矩阵正向指标标准化处理结果
 
k=1/log(rows);                    % 求k
lnYij1=zeros(rows,cols);           % 初始化lnYij1
% 计算lnYij1
for i=1:rows                         %循环遍历取对数
    for j=1:cols
        if Y(i,j)==0;
            lnYij1(i,j)=0;
        else
            lnYij1(i,j)=log(Y(i,j));  %log取对数
        end
    end
end
ej1=-k*(sum(Y.*lnYij1,1));             % 计算正向指标标准化熵值ej1
 
weights1=(1-ej1)/(cols-sum(ej1));  %正向指标权重weights1
 
 
%结构体定义
result(1).guiyihua = Y;            %矩阵归一化结果赋给result
result(1).shangzhi = ej1;          %熵值赋给result
result(1).weight = weights1;       %权重赋给result
