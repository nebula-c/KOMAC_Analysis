#include "TGraph.h"
#include "TCanvas.h"
#include "TString.h"
#include "TH1F.h"
#include "TColor.h"
#include "TPad.h"
#include "TPaveLabel.h"

#include "iostream"
#include "fstream"
#include "string"

#include "src/Mg.cpp"

using namespace std;


const int xmax = 70;
const int xmin = 0;
const int ymax = 150;
const int ymin = 0;

const float constmarkersize = 1.;
const float constlinewidth = 1;

TGraph *gRpi, *gRas;

void dose_time()
{
    TCanvas *c1= new TCanvas();
    mymg *mg = new mymg();
    LoadGraph();
    SetGraph(gApr_origin,kBlack);
    SetGraph(gApr_revision,kRed);
    SetGraph(gJun_origin,kBlack);
    SetGraph(gJun_revision,kOrange);
    SetGraph(gJul_RPI_origin,kBlack);
    SetGraph(gJul_RPI_revision,kGreen);
    SetGraph(gJul_RAS_origin,kBlack);
    SetGraph(gJul_RAS_revision,kBlue);
    SetGraph(gSep_origin,kBlack);
    SetGraph(gSep_revision,kViolet);

    // mg->Add(gApr_origin,"2022-04, origin");
    // mg->Add(gApr_revision,"2022-04, revision");
    // mg->Add(gJun_origin,"2022-06, origin");
    // mg->Add(gJun_revision,"2022-06, revision");
    // mg->Add(gJul_RPI_origin,"2022-07(seperated), origin");
    // mg->Add(gJul_RPI_revision,"2022-07(seperated), revision");
    // mg->Add(gJul_RAS_origin,"2022-07, origin");
    // mg->Add(gJul_RAS_revision,"2022-07, revision");
    // mg->Add(gSep_origin,"2022-09, origin");
    // mg->Add(gSep_revision,"2022-09, revision");
    
    // mg->Add(gApr_revision,"2022-04");
    // mg->Add(gJun_revision,"2022-06");
    // mg->Add(gJul_RPI_revision,"2022-07(seperated)");
    // mg->Add(gJul_RAS_revision,"2022-07");
    // mg->Add(gSep_revision,"2022-09");




    // mg->offLegend();
    mg->Draw();
    
}



void LoadGraph()
{
    string mypath = "/home/suchoi/KOMAC/analysis/processed/";

    gRas = onegraph(mypath + "dose/Apr_dose.txt", mypath + "datainfo/"  );
    gRpi = onegraph(mypath + "dose/Apr_dose.txt", mypath + "datainfo/");
}



void eachresult(string dosetxt, string thrstxt, char* output)
{
    TCanvas *c1 = new TCanvas();
    TGraph *g1 = onegraph(dosetxt,thrstxt);

    
    SetGraph(g1,1);
    
    g1->Draw();
    c1->SaveAs(output);
}

TGraph* onegraph(string dosetxt, string thrstxt)
{
    TGraph *g1 = new TGraph();

    ifstream dosefile;
    ifstream thrsfile;
    dosefile.open(dosetxt);
    thrsfile.open(thrstxt);
    
    if(!dosefile) cout << "there is no dosefile" << endl;
    if(!thrsfile) cout << "there is no thrsfile" << endl;
    
    string mydose, mythrs, mynoise, line;
    float totaldose = 0;
    thrsfile >> line;     // for column title
    while(1)
    {
        dosefile >> mydose;
        thrsfile >> line;
        if(dosefile.eof()) break;

        mythrs = line.substr(0,line.find(','));
        double_t x,y;
        if(isaccum)
        {
            x = stof(mydose);
            y = stof(mythrs) * 10;
        }
        else
        {
            totaldose += stof(mydose);
            x = totaldose;
            y = stof(mythrs) * 10;
        }        
        
        g1->SetPoint(g1->GetN(),x,y);    
    }
    
    dosefile.close();
    thrsfile.close();

    return g1;
}

void SetGraph(TGraph *mygraph,int mycolor,int mymarkerstyle = 20,float mymarkersize = constmarkersize, float mylinewidth = constlinewidth)
{
    mygraph->SetMarkerStyle(20);
    mygraph->SetMarkerSize(mymarkersize);
    mygraph->SetLineWidth(mylinewidth);
    mygraph->SetMarkerColor(mycolor);
    mygraph->SetLineColor(mycolor);
    mygraph->GetXaxis()->SetLimits(xmin,xmax);
    mygraph->SetMinimum(ymin);
    mygraph->SetMaximum(ymax);
}
