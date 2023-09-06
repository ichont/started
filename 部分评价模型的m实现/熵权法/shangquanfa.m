clc;clear;
%读取数据
data=[900.2	554.2	4	4	7	5	16	66	85	5980
600	250	4	4	6	7	9.6	65	70	1699
270	100	4	4	9	9	24.62	50	70	5699
300	200	1	3	6	7	6.35	65	30	2299
846	622	4	4	8	5	16.5	67	80	6099
378	208	4	4	6	6	9.8	65	60	1599
655	437	4	4	6	7	8.8	68.6	67	2799
844	604	4	4	7	6	5.16	67	80	4999
800	400	4	4	6	8	14	69	90	2299
230	60	4	2	5	7	5.9	60	43	609

]
data=data(:,3:end); %只取指标数据
%指标正向    化处理后数据为data1
data1=data;
%%越小越优型处理
index=[3,4];%越小越优指标位置
for i=1:length(index)
  data1(:,index(i))=max(data(:,index(i)))-data(:,index(i));
end
%%某点最优型指标处理
index=[5];
a=90;%最优型数值
for i=1:length(index)
  data1(:,index(i))=1-abs(data(:,index(i))-a)/max(abs(data(:,index(i))-a));
end
 
%数据标准化 mapminmax对行进行标准化，所以转置一下
data2=mapminmax(data1',0.002,1); %标准化到0.002-1区间
data2=data2';
 
%得到信息熵
[m,n]=size(data2);
p=zeros(m,n);
for j=1:n
    p(:,j)=data2(:,j)/sum(data2(:,j));
end
for j=1:n
   E(j)=-1/log(m)*sum(p(:,j).*log(p(:,j)));
end
 
%计算权重
w=(1-E)/sum(1-E);