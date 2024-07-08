function pars=get_model_param(drcs1,data,Drcs1)
%---------------------可变参数----------------------%
    pars.md1=drcs1{1}/1000;    %环空保护液密度
    pars.thyl=drcs1{2};         %套管压力
    pars.ygyl=drcs1{3};         %油管压力
    pars.Rti=drcs1{4}(end)/2;         %套管内径
    pars.DW=drcs1{4};
    pars.Rto=drcs1{5}(end)/2;         %套管外径 
    pars.Rvo=(flipud(drcs1{6}'/2))';         %油管外径 
    pars.Rvi=(flipud(drcs1{7}'/2))';         %油管内径
    pars.RRO=Drcs1{5}/2;
    pars.Ls=(flipud(drcs1{8}'))';
    pars.LS=(flipud(Drcs1{4}'))';
    pars.Rmax=drcs1{13};         %井筒内径
    pars.Q=Drcs1{1}*10^4;                  %日产量m3/d
    pars.deP=(Drcs1{2}-Drcs1{3});
    SSN=1-pars.deP/100;
    pars.TT=drcs1{15};            %井底温度
    pars.pint=SSN*drcs1{16};             %井底压强地层压力
    pars.rhov11=drcs1{17};
    pars.QQ1=drcs1{19};
    pars.fkl=drcs1{20};
    pars.LLS=drcs1{21};
    pars.fs=drcs1{22};%正弦屈曲载荷
    pars.fh=drcs1{23};%螺旋屈曲载荷
    pars.Tint1=drcs1{24};
    [Ss,~,~,Zs,~,~]=deal_input_data(data);
    pars.DT=(pars.TT-pars.Tint1)/Zs(end);
    Zs1=interp1(Ss,Zs,sum(pars.Ls));           %当前位置井斜角  
    pars.Tint=pars.Tint1+pars.DT*Zs1;            %井底温度
    for i=1:length(pars.rhov11)
        pars.rhov1(i)=pars.rhov11(i)/(pi*(pars.Rvo(i)^2-pars.Rvi(i)^2));
    end
    pars.rhov=mean(pars.rhov1);
    pars.NNx=drcs1{18};
%---------------------不可变参数----------------------%
    ssd2=length(pars.Ls);
    mesh=zeros(ssd2,1);
    for i=1:ssd2
         mesh(i)=round((pars.Ls(i)/50));
    end
    pars.mesh=mesh;                   %各个分段网格划分
    pars.Ev=231e9;           %油管模量
    pars.Ua=6.66;              %井筒总导热系数
%   pars.Ua=23.26;              %井筒总导热系数
    pars.Zg=1.59;                  %天然气压缩因子
    pars.M=0.016;               %天然气摩尔质量
%     pars.M=0.032;               %天然气摩尔质量
%     pars.cp=2227;               %天然气等压比热容
    pars.cp=2227;               %天然气等压比热容
    pars.c=0.1;                 %结构阻尼系数
    pars.miuv=0.3;              %油管泊松比
    pars.miut=0.3;              %套管泊松比
    pars.ksi=0.3;               %油管和套管之间的摩擦系数
    pars.rhoe=2640;             %地层岩石密度
    pars.ce=837;              %地层比热容
%   pars.ke=2.06;               %地层导热系数
    pars.ke=2.06; 
    pars.Rg=8.314;              %气体常数
    pars.gama=0.6;             %流体相对密度
    pars.pc=6.49;                  %临界压力 MPa
    pars.Tc=190.9;                  %临界温度  K
    pars.PC=(4.666+0.103*pars.gama-0.25*pars.gama^2)*1e6;   %天然气视临界压力， Pa
    pars.TC=93.3+181*pars.gama-7*pars.gama^2;             %天然气视临界温度， K 
%     if  pars.gama>=0.7
%          pars.PC=(4.881-0.3861*pars.gama)*1e6;   %天然气视临界压力， Pa
%          pars.TC=92.2+176.6*pars.gama;             %天然气视临界温度， K 
%     else
%          pars.PC=(4.778-0.248*pars.gama)*1e6;   %天然气视临界压力， Pa
%          pars.TC=92.2+176.6*pars.gama;             %天然气视临界温度， K 
%     end
    
    pars.alphae=pars.ke/(pars.ce*pars.rhoe);
%     pars.tD=pars.alphae/pars.Rmax^2;
%     pars.ft=0.9821*log(1+1.81*sqrt(pars.tD));
    t=3600;
    pars.tD=pars.alphae*t/pars.Rmax^2;
    if pars.tD<=1.5
      pars.ft=1.1281*(sqrt(pars.tD)-0.3*pars.tD);
    else
      pars.ft=(0.4036+0.5*log(pars.tD))*(1+0.6/pars.tD); 
    end
    pars.im=0.04;               %油管绝对粗糙度
%     pars.miu=2.555e-5;          %动力粘度
    pars.miu=2.555e-5;          %动力粘度
    %计算井段流体状态的井底初始条件

%     pars.rhoint=600;
    pars.rhoint=(3484.48*pars.gama*pars.pint/10^(6))/(pars.Zg*(pars.Tint+273));          %井底流体密度
    pars.wi=((pars.Q/(24*60*60))*1.29*pars.gama);                 %流体质量流量  Kg/s
%     pars.rhoint=28.96*0.77*pars.pint/pars.Zg/(pars.Tint+273)/8314;
%     pars.Vint=pars.Zg*pars.wi/(pi*pars.Rvi(end)^2)/pars.rhoint;      %井底初始流体速度
%     pars.Vint=pars.Zg*pars.wi/86400/pi/4*0.0647^2/pars.rhoint;  
%     pars.Vint=5e-9*400000*pars.Zg*(pars.Tint+273)/220/0.0647^2;
    pars.Vint=5e-9*(pars.Q*pars.Zg*(pars.Tint+273))/((pars.Rvi(end)*2)^2*pars.pint/10^(6));
%     pars.Vint=20;
     %接触力参数
    pars.khit=1.1e6;
    pars.chit=12e3;              %接触刚度和阻尼
end