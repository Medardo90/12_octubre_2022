# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 22:02:18 2022

@author: Patricio Haro
"""
#include<iostream>
#include<string.h>
#include<conio.h>
using namespace std;

void Pr(){
	cout<<"Productos: "<<endl; 
	cout<<"Galleta $50  01"<<endl<<"Chocolate $60 02"<<endl<<"Gaseosa $80 03"<<endl;
	cout<<"Salir 04"<<endl; 
}

int seleccion(){
	int a; 
	cin>>a; 
	return a; 
		}

void datos(int i,int csh[]){
	if(i==1){
		cout<<"Saldo disponible: "<<"Oscar 19 "<<csh[i]<<endl; 
	}
	if(i==2){
		cout<<"Saldo disponible: Marta 19 "<<csh[i]<<endl; 
	}
}

int cobro(int i,int csh[],string n[]){
	if(i==1){
		csh[i] = csh[i]-50; 
		cout<<"Cobrando "<<endl<<"Saldo actual: "<<n[i]<<" "<<csh[i]<<endl; 
	}
	if(i==2){
		csh[i] = csh[i]-60;  
		cout<<"Cobrando "<<endl<<"Saldo actual: "<<n[i]<<" "<<csh[i]<<endl;
	}
	if(i==3){
		csh[i] = csh[i]-80; 
		cout<<"Cobrando "<<endl<<"Saldo actual: "<<n[i]<<" "<<csh[i]<<endl;
	}
}

int main(){
	int s = 0,c,csh[3],d; 
	string n[2]; 
	n[1] = "Oscar"; 
	csh[1] = 200; 
	n[2] = "Marta "; 
	csh[2] = 100;
	do{
		Pr();
		cout<<"Ingrese su seleccion: ";  
		cin>>c; 
		cout<<endl; 
		system("cls"); 
		cout<<"Clientes: "<<endl<<"1. Oscar"<<endl<<"2. Marta "<<endl<<"Indentifiquese: "; 
		cin>>d; 
		cout<<endl; 
		system("cls"); 
		datos(d,csh); 
		cobro(c,csh,n); 
		system("pause"); 
		system("cls"); 
	}while(s!=1);
	}
