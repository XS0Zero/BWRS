function [pzz,TTT1]=czyl(pars,Vz,rho0z,Tz,Ss,Zs,alphas)
dV=diff(Vz);
rho0z1=rho0z*0.318;
% drho0z=diff(rho0z);
g=9.8;
for i=1:(length(Tz)-1)
    zup1=interp1(Ss,Zs,i);         
    Tei=pars.Tint1+pars.DT*zup1;            %�ز��¶�
    Re=rho0z(i)*Vz(i)*2*pars.Rvi(1)/pars.miu;      %��ŵ��
    f=1/((4*log(pars.im/(2*3.715*pars.Rvi(1))+(6.943/Re)^0.9)^2));
    dpdzfr=f*rho0z1(i)*Vz(i)^2/2/pars.Rvi(1);
    alpha=interp1(Ss,alphas,zup1);           %��ǰλ�þ�б��
    dp(i)=-(rho0z1(i)*g*cos(alpha)+dpdzfr-rho0z1(i)*Vz(i)*(dV(i)));
    dT(i)=(-((g*cos(alpha)-Vz(i)*(dV(i))+...
        2*pi*pars.Rmax*pars.ke*pars.Ua*(Tz(i)-Tei)/(pars.wi*(pars.ke+pars.Rmax*pars.Ua*pars.ft)))/pars.cp))*1.06;
end
for i=1:(length(Tz))
    if i==1
       paz(1)=pars.pint;
       TTT(1)=pars.Tint;
    elseif i==2
       paz(2)=pars.pint+dp(1);
       TTT(2)=pars.Tint+dT(1);
    else
       paz(i)=paz(i-1)+dp(i-1);
       TTT(i)=TTT(i-1)+dT(i-1);
    end
end
pzz=flipud(paz');
TTT1=flipud(TTT')';
end