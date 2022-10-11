#include "TGraph.h"
#include "TMultiGraph.h"
#include "TH1F.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TLegend.h"

#include "iostream"
#include "fstream"
#include "string"

using namespace std;

TMultiGraph *mg1 = new TMultiGraph();

void MakeGraph(TGraph *mygraph, TString filename);
void AddMG_1(TGraph *myGraph, Color_t mycolor);
void AddMG_2(TGraph *myGraph, Color_t mycolor);
void Fitting(TGraph *g1, TGraph *g2);
TGraph *SubGraph(TGraph *g1, TGraph *g2, Color_t mycolor);
TGraph *DivGraph(TGraph *g1, TGraph *g2, Color_t mycolor);

void Thrsplot()
{
    TCanvas *c1 = new TCanvas();
    TGraph *R16 = new TGraph();
    TGraph *R5 = new TGraph();
    TGraph *R17 = new TGraph();
    TGraph *R19 = new TGraph();
    TGraph *R42 = new TGraph();
    TGraph *R41 = new TGraph();
    TGraph *R38 = new TGraph();
    TGraph *QR16 = new TGraph();
    TGraph *QR5 = new TGraph();
    TGraph *QR17 = new TGraph();
    TGraph *QR19 = new TGraph();
    TGraph *QR42 = new TGraph();
    TGraph *QR41 = new TGraph();
    TGraph *QR38 = new TGraph();


// ITS Plenary
    MakeGraph(R16,"r16");
    MakeGraph(R5,"r5");
    MakeGraph(R17,"r17");
    MakeGraph(R19,"r19");
    MakeGraph(R42,"r42");
    MakeGraph(R41,"r41");
    MakeGraph(R38,"r38");
    
    AddMG_1(R16,kBlue);
    AddMG_1(R5 ,kGreen);
    AddMG_1(R17,kRed);
    AddMG_1(R19,kCyan);
    AddMG_1(R42,kMagenta);
    AddMG_1(R41,kYellow+1);
    AddMG_1(R38,kBlack);


// Qualitification Task Force
    MakeGraph(QR16,"qr16");
    MakeGraph(QR5,"qr5");
    MakeGraph(QR17,"qr17");
    MakeGraph(QR19,"qr19");
    MakeGraph(QR42,"qr42");
    MakeGraph(QR41,"qr41");
    MakeGraph(QR38,"qr38");

    AddMG_2(QR16,kBlue);
    AddMG_2(QR5,kGreen);
    AddMG_2(QR17,kRed);
    AddMG_2(QR19,kCyan);
    AddMG_2(QR42,kMagenta);
    AddMG_2(QR41,kYellow+1);
    AddMG_2(QR38,kBlack);

//Sub
    TGraph *Sub_16 = SubGraph(R16,QR16,kBlue);
    TGraph *Sub_5 = SubGraph(R5,QR5,kGreen);
    TGraph *Sub_17 = SubGraph(R17,QR17,kRed);
    TGraph *Sub_19 = SubGraph(R19,QR19,kCyan);
    TGraph *Sub_42 = SubGraph(R42,QR42,kMagenta);
    TGraph *Sub_41 = SubGraph(R41,QR41,kYellow+1);
    TGraph *Sub_38 = SubGraph(R38,QR38,kBlack);

//Div
    TGraph *Div_16 = DivGraph(R16,QR16,kBlue);
    TGraph *Div_5 = DivGraph(R5,QR5,kGreen);
    TGraph *Div_17 = DivGraph(R17,QR17,kRed);
    TGraph *Div_19 = DivGraph(R19,QR19,kCyan);
    TGraph *Div_42 = DivGraph(R42,QR42,kMagenta);
    TGraph *Div_41 = DivGraph(R41,QR41,kYellow+1);
    TGraph *Div_38 = DivGraph(R38,QR38,kBlack);

    mg1->Add(Sub_16);
    mg1->Add(Sub_5);
    mg1->Add(Sub_17);
    mg1->Add(Sub_19);
    mg1->Add(Sub_42);
    mg1->Add(Sub_41);
    mg1->Add(Sub_38);

    mg1->Add(Div_16);
    mg1->Add(Div_5);
    mg1->Add(Div_17);
    mg1->Add(Div_19);
    mg1->Add(Div_42);
    mg1->Add(Div_41);
    mg1->Add(Div_38);

    mg1->GetXaxis()->SetLimits(0,350);
    mg1->SetMinimum(0);
    mg1->SetMaximum(150);
    mg1->GetHistogram()->SetTitle("Threshold-Dose Plots(Prague)");
    // mg1->GetHistogram()->SetTitle("Division(A/B)");
    mg1->Draw("apl");

    TLegend *l1 = new TLegend();
    l1->AddEntry(R38,"ITS Plenary(A)");
    l1->AddEntry(QR38,"Qualification Task Force(B)");
    l1->AddEntry(Sub_38,"Subtracion(A-B)");
    l1->AddEntry(Div_38,"Division(A/B)");
    l1->Draw();
}

void AddMG_1(TGraph *myGraph, Color_t mycolor)
{
    myGraph->SetMarkerStyle(8);
    myGraph->SetMarkerSize(0.5);
    myGraph->SetMarkerColor(mycolor);
    myGraph->SetLineColor(mycolor);
    myGraph->SetLineWidth(2);
    myGraph->SetLineStyle(7);

    mg1->Add(myGraph);
}

void AddMG_2(TGraph *myGraph, Color_t mycolor)
{
    myGraph->SetMarkerStyle(8);
    myGraph->SetMarkerSize(0.5);
    myGraph->SetMarkerColor(mycolor);
    myGraph->SetLineColor(mycolor);
    myGraph->SetLineWidth(2);
    myGraph->SetLineStyle(5);

    mg1->Add(myGraph);
}

void MakeGraph(TGraph *mygraph, TString filename)
{
    fstream myfile;
    filename = filename + ".txt";
    myfile.open(filename);

    std::string x;
    std::string y;
    
    while(myfile)
    {
        myfile >> x;
        myfile >> y;
        mygraph->SetPoint(mygraph->GetN(),stof(x),stof(y));
        
        if(myfile.eof())
            break;
    }
}

TGraph *SubGraph(TGraph *g1, TGraph *g2, Color_t mycolor)
{
    TGraph *returnG = new TGraph();
    for(int i=0; i<g1->GetN(); i++)
    {
        returnG->SetPoint(i,g1->GetPointX(i),g1->GetPointY(i)-g2->GetPointY(i));
    }
    returnG->SetMarkerStyle(8);
    returnG->SetMarkerSize(0.5);
    returnG->SetMarkerColor(mycolor);
    returnG->SetLineColor(mycolor);
    returnG->SetLineWidth(2);
    returnG->SetLineStyle(3);
    return returnG;
}

TGraph *DivGraph(TGraph *g1, TGraph *g2, Color_t mycolor)
{
    TGraph *returnG = new TGraph();
    for(int i=0; i<g1->GetN(); i++)
    {
        returnG->SetPoint(i,g1->GetPointX(i),g1->GetPointY(i)/g2->GetPointY(i));
    }
    returnG->SetMarkerStyle(8);
    returnG->SetMarkerSize(0.5);
    returnG->SetMarkerColor(mycolor);
    returnG->SetLineColor(mycolor);
    returnG->SetLineWidth(2);
    returnG->SetLineStyle(1);
    return returnG;
}